#!/bin/bash

CWD=$(pwd)
echo $CWD

mkdir cache
mkdir vocabularies

cp ./lovcrawlpy/cfg.py.template ./lovcrawlpy/cfg.py
sed -i "s#__PROJECT_FOLDER__#$CWD#g" ./lovcrawlpy/cfg.py
