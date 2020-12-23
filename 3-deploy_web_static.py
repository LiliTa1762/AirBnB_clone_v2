#!/usr/bin/python3
""" Fabric script
    contains the function 1-pack_web_static.py """

from fabric.api import *
import time

from os import path

env.hosts = ['34.73.70.74', '35.185.4.177']


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
        local("tar -czvf {} web_static/".format("versions/" + file_name))
        return "web_static/{}".format(file_name)
    except:
        return


def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static folder

    Returns:
        str: the file path or None if fails
    """
    if not path.exists(archive_path):
        return False

    dest_path = "/data/web_static/releases/"
    file_name = archive_path.split("/")[1]
    file_without = file_name.split(".")[0]

    try:
        # sending files
        put(archive_path, "/tmp/")
        # unzip and move
        run("sudo tar -xzvf /tmp/" + archive_path + " -C " + dest_path)
        dest_and_archive = dest_path + archive_path
        run("sudo mv " + dest_and_archive + " " + dest_path + file_without)
        run("sudo rm -r /tmp/" + archive_path)

        # new symbolic link
        run("sudo rm /data/web_static/current")
        path_new_code = dest_path + file_without
        run("sudo ln -sf " + path_new_code + " /data/web_static/current")
        run("sudo ")
        return True
    except:
        return False


def deploy():
    new_path = do_pack()
    if new_path:
        return do_deploy(new_path)
    return False
