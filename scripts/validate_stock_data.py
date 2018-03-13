'''validates stock data, rejecting rows that are invalid'''
import sys
from os.path import join
import csv_reader
import csv_writer
import utils

def validate_one(input_file, output_file):
    '''
    filter by row not containing empty string or None
    output valid results in output/[dev,production]/valid
    '''
    print('validating ' + input_file)
    csv_data = csv_reader.read(input_file)
    valid_csv_data = list(filter(lambda row: '' not in row and None not in row, csv_data))
    csv_writer.write(output_file, valid_csv_data)
    print('writing validated csv to ' + output_file)

def validate(input_dir, output_dir):
    '''calls validate_one on all csv files in input_dir'''
    utils.make_dir_if_not_exists(output_dir)
    files = utils.get_csv_file_list_in_dir(input_dir)
    for csv_file_name in files:
        validate_one(join(input_dir, csv_file_name), join(output_dir, csv_file_name))

if __name__ == '__main__':
    validate(sys.argv[1], sys.argv[2])
