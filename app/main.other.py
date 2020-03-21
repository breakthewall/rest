# from redis import Redis
# from rq import Queue
# import time
# import json
from importlib import import_module

from flask import Flask, request
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/<tool>', methods=['POST'])
def main(tool):

    tool_module = import_module(tool)

    if request.method == "POST":

        params = tool_module.read_args_from_request(request)
        return tool_module.run.delay(params)

        #
        # q = Queue(tool, connection=Redis(host='redis', port=6379))
        # async_results = q.enqueue(tool_module.run, params)
        # result = None
        # while result is None:
        #     result = async_results.return_value
        #     app.logger.info(async_results.return_value)
        #     app.logger.info(async_results.get_status())
        #     if async_results.get_status()=='failed':
        #         return Response('Job failed \n '+str(result), status=400)
        #     time.sleep(2.0)
        #
        # return result

    return "OK"



#
# if __name__== "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
