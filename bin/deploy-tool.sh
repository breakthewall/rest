#!/bin/bash

tool_url=$1
if [[ "$tool_url" == "" ]]; then
  echo
  echo "Usage:"
  echo
  echo "   `basename $0` <tool-url> [branch]"
  echo
  exit 1
fi


branch=$2
if [[ "$branch" == "" ]]; then
  branch="master"
fi

tool_name=`echo "${tool_url##*/}"`
length=${#tool_name}
tool_name=${tool_name:0: length - 4}

cd app && git clone -b $branch --single-branch $tool_url
# Context in worker not the same as in flask
cd $tool_name && ln -sf . $tool_name


echo
echo "Build with:"
echo
echo "     ./bin/build-worker-image.sh ${tool_name} [from_image_name]"
echo
echo "Run with:"
echo
echo "     ./bin/start-worker.sh ${tool_name} [nb_of_worker]"
echo
echo "Stop with:"
echo
echo "     ./bin/stop-worker.sh ${tool_name}"
echo
