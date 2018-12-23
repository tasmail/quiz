#!/bin/bash

set -e

VERSION=""

if [ $# -gt 0 ]; then
	VERSION=":${1}"
fi

cp ../requirements.txt ./

docker build -t tas/quiz${VERSION}  ./

rm requirements.txt
