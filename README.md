# rest

REST manager of tools. It contains a Flask service and is able to deploy tool as workers. Source code may be found at the following location: [GitHub](https://github.com/brsynth/rest).

## Prerequisites

* Docker - [Install](https://docs.docker.com/install/)
* Redis service. If none of such a service is available into your environment, you can deploy one by using [GitHub](https://github.com/brsynth/redis).

## Flask service
### Start
Flask service is assumed by gunicorn and can be run with:

```
./bin/start-flask [redis_hostname (default='redis')]
```
### Stop
```
./bin/stop-flask
```

## Restful tool
### Install
Assumed you have a tool in rest mode, you can deploy it into this framework with:
```
./bin/deploy-tool <rest-tool_url> [branch (default='master')] [tool_name (default is extracted from rest-tool_url)]
```
### Build Docker image
```
./bin/build-worker-image <tool_name> [from_image_name]
```
### Run tool in rest mode
The restful service is assumed by rq and can be run with:
```
./bin/start-worker <tool_name> [nb_of_workers] [redis_hostname (default='redis')]
```
### Stop tool
```
./bin/stop-worker <tool_name>
```


## Authors

* **Joan Hérisson**
* Melchior du Lac

## License
rest is released under the [MIT](https://github.com/brsynth/rest/blob/master/LICENSE.txt) license.
