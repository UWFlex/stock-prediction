'''reads csv file'''
import csv
import sys
import utils

def read(csv_relative_path):
    '''csv_relative_path is the path to the csv file from project root'''
    csv_file_path = utils.format_path(csv_relative_path)
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)

if __name__ == "__main__":
    print(read(sys.argv[1]))
