#!/bin/bash

# Read tools lists
function read_tools() {
  tools_names=($(awk '{print $1}' $1))
  tools_repos=($(awk '{print $2}' $1))
  tools_branches=($(awk '{print $3}' $1))
}

function print() {
  local msg=$1
  local msglen=${#msg}
#  banner=$(printf '%*s\n' "$((COLUMNS-2))" '' | tr ' ' '-')
  local banner=$(printf '%*s' $((msglen+2)) "" | tr ' ' '-')
  tput bold
  printf '\n'
  # printf '|'"$banner"'\n'
  # printf '| '"$msg"'\n'
  # printf '|'"$banner"'\n'
  printf "$msg"'\n'
  printf '\n'
  tput sgr0
}
