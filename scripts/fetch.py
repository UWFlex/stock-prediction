"""fetches stock data from api"""
import urllib.request
import os
import sys
import constants

def url_builder(params):
    """formats url"""
    url = constants.BASEURL
    separator = '&'
    rest_of_url = separator.join(params)
    url = url + rest_of_url
    return url

def fetch(symbols_file, output_path):
    """fetches stock data from api, then outputs as raw csv file"""
    base_path = os.path.dirname(os.path.realpath('__file__'))
    print(base_path)

    # read from symbols file
    with open(os.path.join(base_path, symbols_file), 'r') as data:
        read_data = data.read()

        formatted_data = str(read_data).split()

        # fetch stock data for each symbol
        for item in formatted_data:
            param_list = [
                constants.TIME_SERIES_DAILY_ADJUSTED, 'symbol=' + item,
                constants.OUTPUTSIZE_COMPACT, constants.DATATYPE_CSV, constants.API_KEY
            ]

            url = url_builder(param_list)

            urllib.request.urlretrieve(url, os.path.join(os.path.join(base_path, output_path), item + '.csv'))

            print(os.path.join(os.path.join(base_path, output_path), item + '.csv'))

if __name__ == "__main__":
    fetch(str(sys.argv[1]), str(sys.argv[2]))
