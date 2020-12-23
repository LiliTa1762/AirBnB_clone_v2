#!/usr/bin/python3
""" Fabric script
    contains the function 1-pack_web_static.py """

from fabric.api import *
import time

file_name = "web_static_"
file_name += time.strftime("%Y%m%d%H%M%S")
file_name += ".tgz"

def do_pack():
    local("mkdir versions")
    try:
        local("tar -czvf {} web_static/".format("versions/"filename))
        return "web_static/{}".format(file_name)
    except:
        return
