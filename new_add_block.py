import os
import sys
import shutil
import argparse
from jinja2 import Template

folder = ['inc', 'src', 'test']


def parser_create():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', nargs=2)
    parser.add_argument('-d', '--delete', nargs=2)
    return parser


def root_folder_create():
    for counter in range(0, len(folder)):
        if not (os.path.exists(folder[counter])):
            os.mkdir(folder[counter])
            counter += 1


def block_create(name_block):
    for counter in range(0, len(folder)):
        os.chdir(folder[counter])
        if not (os.path.exists(name_block)):
            os.mkdir(name_block)
        counter += 1
        os.chdir('..')


def block_fill(name_block):
    for counter in range(0, len(folder)):
        os.chdir(folder[counter]+"/"+name_block)
        if counter == 0:
            simple_end = ".h"
            internal_end = "_internal.h"
        elif counter == 1:
            simple_end = ".c"
            internal_end = "_internal.c"
        elif counter == 2:
            simple_end = "_test.c"
            internal_end = "_test_runner.c"
        if not(os.path.exists(name_block+".c")):
            file_c = open(name_block+simple_end, "w")
            file_c.close()
        if not(os.path.exists(name_block+"_internal.c")):
            file_internal_c = open(name_block+internal_end, "w")
            file_internal_c.close()
        os.chdir('../..')


def project_create(project, block):
    os.chdir('..')
    if not (os.path.exists(project)):
        os.mkdir(project)
    os.chdir(project)
    root_folder_create()
    block_create(block)
    block_fill(block)

parser = parser_create()
args = parser.parse_args()

print(args)
project_create(args.add[0], args.add[1])
