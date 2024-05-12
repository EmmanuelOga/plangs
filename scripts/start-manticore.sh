#!/bin/sh

docker run -e EXTRA=1 --name manticore -v "$(pwd)"/data:/var/lib/manticore -p 127.0.0.1:9306:9306 -p 127.0.0.1:9308:9308 -d manticoresearch/manticore