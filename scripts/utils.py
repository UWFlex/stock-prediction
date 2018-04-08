'''common util functions'''
import os
from os.path import dirname, abspath
import urllib.request
import json
import shutil

def format_path(path_from_root) -> str:
    '''generates absolute path from relative path'''
    base_path = abspath(dirname(dirname(__file__)))
    absolute_path = os.path.join(base_path, path_from_root)
    return absolute_path


def get_filename_list(path_from_root, suffix) -> list:
    '''generates a list of csv files in given directory'''
    filenames = os.listdir(format_path(path_from_root))
    return [filename for filename in filenames if filename.endswith(suffix)]


def url_builder(url, params) -> str:
    '''formats url'''
    separator = '&'
    rest_of_url = separator.join(params)
    url = url + rest_of_url
    return url


def make_dir_if_not_exists(path_from_root):
    '''creates directory if not exists'''
    directory = format_path(path_from_root)
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_dir(path_from_root):
    '''removes directory'''
    shutil.rmtree(format_path(path_from_root), ignore_errors=True)

def get_json_from_url(url):
    '''fetch data as json from url'''
    with urllib.request.urlopen(url) as url2:
        data = json.loads(url2.read().decode())
        return data
