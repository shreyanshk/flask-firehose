#!/bin/sh
nginx -c /app/nginx.conf
python3 server.py
