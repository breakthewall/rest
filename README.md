# rest

REST manager of tools. It contains a Flask service and is able to deploy tools as workers. Source code may be found at the following location: [GitHub](https://github.com/brsynth/rest).

## Prerequisites

* Docker - [Install](https://docs.docker.com/install/)
* Redis service. If none of such a service is available within your environment, you can deploy one by using [GitHub](https://github.com/brsynth/redis).

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
Tools to be installed by filling up `tools/tools.lst` and by running:
```
./bin/install-tools
```
A single restful tool can be installed with:
```
./bin/install-tool <tool_name> <tool_repo> <tool_branch>
```
### Build Docker image
```
./bin/build-worker-image <tool_name> [base_image_name]
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
