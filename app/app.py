import requests

def read_args_from_request(request):
    return request.get_data(as_text=True)

def run(args):
    url = args
    resp = requests.get(url)
    return len(resp.text.split())
