#!/bin/bash
#gunicorn main:aioapp -c gunicorn.conf.py -k aiohttp.worker.GunicornWebWorker
docker run --restart always -d --name flask_app -p 8000:8000 -v `pwd`/logs:/var/www/app/logs hyhlinux/flask_app
#docker run -d --name flask_app  -v `pwd`/logs:/var/www/app/logs hyhlinux/flask_app
