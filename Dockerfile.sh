#!/bin/sh

docker stop 360-webview && docker rm 360-webview
docker build . -t 360-webview
docker run -d -it --name 360-webview --restart always -p 9001:9001 360-webview