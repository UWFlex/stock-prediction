'''writes to csv file'''
import csv
import sys
import utils

def write(csv_relative_path, data):
    '''csv_relative_path is the path to the csv file from project root'''
    csv_file_path = utils.format_path(csv_relative_path)
    with open(csv_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    print(write(sys.argv[1], sys.argv[2]))
