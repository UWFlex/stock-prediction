''' gived a stock data csv file, created a normalized data file'''
from sklearn import preprocessing
# import array
import numpy
import csv_reader


def normalize_col(in_data):
    ''' takes a list of data and returns a list of normalizated data '''

    in_data_normed = preprocessing.normalize(in_data, norm='l1')
    return in_data_normed


def normalize(input_path, output_path):
    ''' normalizes the file'''
    in_data = numpy.array(csv_reader.read(input_path))
    print(in_data[1:])


if __name__ == '__main__':
    STUFF = numpy.array([[6, 69, 10, 420, -1, -68, -453, 146]])
    STUFF_AFTER = normalize_col(STUFF)
    normalize('output/dev/raw/AMZN.csv', 'output/dev/normalized/AMZN.csv')
