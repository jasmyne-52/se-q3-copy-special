#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Jasmyne Ford w/h/f JT and classmates"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    files = os.listdir(dirname)
    double_under_regex = r'__\w*__'
    paths = []

    for f in files:
        if re.search(double_under_regex, f):
            paths.append(os.path.abspath(os.path.join(dirname, f)))
    return paths


def create_dir(path):
    """ Checks to see if a dir exists, if not create it """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError:
            print(f"Creation of dir {path} failed")
            return False
    return True


def copy_to(path_list, dest_dir):
    """ Copies files to a given directory """
    create_dir_status = create_dir(dest_dir)
    if not create_dir_status:
        return
    for f in path_list:
        shutil.copyfile(f, os.path.join(dest_dir, os.path.basename(f)))


def zip_to(path_list, dest_zip):
    """ Given a list of paths, zip those files into given zip dir """
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    print(" ".join(cmd))
    subprocess.run(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to get special files from')
    ns = parser.parse_args(args)

    path_list = get_special_paths(ns.from_dir)

    for path in path_list:
        print(path)

    if ns.todir:
        copy_to(path_list, ns.todir)
    if ns.tozip:
        zip_to(path_list, ns.tozip)

    # sys.exit(status)


if __name__ == "__main__":
    main(sys.argv[1:])
