#!/usr/bin/python3
""" Fabric script
    contains the function 1-pack_web_static.py """

from fabric.api import *
import time


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder

    Returns:
        str: the file path or None if fails
    """
    file_name = "web_static_"
    file_name += time.strftime("%Y%m%d%H%M%S")
    file_name += ".tgz"

    local("mkdir -p versions")
    try:
        local("tar -czvf {} web_static/".format("versions/" + filename))
        return "web_static/{}".format(file_name)
    except:
        return
