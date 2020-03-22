#!/bin/bash

tool_url=$1
tool_name=`echo "${tool_url##*/}"`
length=${#tool_name}
tool_name=${tool_name:0: length - 4}

cd ./app
git clone -b dev $tool_url
cd -

echo "
#!/bin/bash
docker network connect ${tool_name} flask
COMPOSE_PROJECT_NAME=${tool_name} docker-compose up -d worker
" > start-${tool_name}.sh

echo "
#!/bin/bash
docker network disconnect ${tool_name} flask
COMPOSE_PROJECT_NAME=${tool_name} docker-compose stop worker
" > stop-${tool_name}.sh

chmod u+x start-${tool_name}.sh stop-${tool_name}.sh

echo
echo "Run with:"
echo
echo "     ./start-${tool_name}.sh"
echo
echo "Stop with:"
echo
echo "     ./stop-${tool_name}.sh"
echo
