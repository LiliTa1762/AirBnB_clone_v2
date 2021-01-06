#!/usr/bin/env bash
# Prepare the web servers for deploy

sudo apt-get -y update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
sudo echo "To test NGINX CONFIG" | sudo tee /data/web_static/releases/test/index.html

# ln create symbolic links
# s override, f remove existence file
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# -h if the directory contains symbolic links
# -R To recursively operate on all files and directories
sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart
