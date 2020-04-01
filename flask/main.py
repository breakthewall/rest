from redis import Redis
from rq import Queue
import time
import json
from importlib import import_module
import os


def read_args_from_request(request):

    # Result
    args = {}

    # Gather files and Read buffers (needed by 'enqueue')
    for key in request.files:
        if key.startswith("_file_"):
            args[key] = request.files[key].read()

    # De-jsonify and add to args
    args.update(json.load(request.files['data']))

    return args


from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/<tool>', methods=['POST'])
def main(tool):

    if request.method == "POST":

        args = read_args_from_request(request)

        q = Queue(tool, connection=Redis(host=os.getenv('REDIS'), port=6379))
        # tool_module = import_module(".worker", "tools."+tool)
        # async_results = q.enqueue(tool_module.run, args, job_timeout=1800)
        from worker import run as worker_run
        async_results = q.enqueue(worker_run, args, job_timeout=1800)

        # app.logger.info(str(async_results))

        result = None
        while result is None:
            result = async_results.return_value
            #app.logger.info(async_results.return_value)
            app.logger.info(async_results.get_status())
            if async_results.get_status()=='failed':
                return Response('Job failed \n '+str(result), status=400)
            time.sleep(2.0)

        return result

    return "OK"


#
# if __name__== "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
