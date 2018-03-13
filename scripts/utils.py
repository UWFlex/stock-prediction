'''common util functions'''
import os

def format_path(path_from_root):
    '''generates absolute path from relative path'''
    base_path = os.path.dirname(os.path.realpath('__file__'))
    absolute_path = os.path.join(base_path, path_from_root)
    return absolute_path

def get_csv_file_list_in_dir(directory):
    '''generates a list of csv files in given directory'''
    filenames = os.listdir(directory)
    return [filename for filename in filenames if filename.endswith('csv')]
