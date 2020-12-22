#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

printf '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
</head>
<body>
    Testing Nginx configuration
</body>
</html>
' | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -Rh ubuntu:ubuntu /data/

LOCATION_ALIAS="\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
ARG_SED="/listen 80 default_server;/a \\$LOCATION_ALIAS\n\n"
sudo sed -i "${ARG_SED}" /etc/nginx/sites-available/default

sudo service nginx restart
