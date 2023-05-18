#!/bin/sh

docker stop 360-webview && docker rm 360-webview
docker build . -t 360-webview
docker run -d -it --name 360-webview --restart always -p 9001:9001 360-webview

# mkdir 360-webview
# cd 360-webview
# wget https://files.krystianch.com/pgrid-feit-012-v1.tar.gz
# tar -xvf pgrid-feit-012-v1.tar.gz
# rm pgrid-feit-012-v1.tar.gz
# docker stop 360-webview && docker rm 360-webview
# docker run -d -it --name 360-webview --restart always -p 9001:9001 -v $(pwd)/img:/python-docker/data/img clovers1254/360-webview