'''fetches stock data from api'''
import urllib.request
import sys
import constants
import utils


def fetch(symbols_file, output_path):
    '''fetches stock data from api, then outputs as raw csv file'''
#    base_path = os.path.dirname(os.path.realpath('__file__'))

    # read from symbols file
    with open(utils.format_path(symbols_file), 'r') as data:
        read_data = data.read()
        formatted_data = str(read_data).split()

        # fetch stock data for each symbol
        for item in formatted_data:
            param_list = [
                constants.TIME_SERIES_DAILY_ADJUSTED, 'symbol=' + item,
                constants.OUTPUTSIZE_COMPACT, constants.DATATYPE_CSV, constants.API_KEY
            ]

            url = utils.url_builder(constants.BASEURL, param_list)
            utils.make_dir_if_not_exists(output_path)
            urllib.request.urlretrieve(url, utils.format_path(
                output_path) + '/' + item + '.csv')
            print('fetched ' + utils.format_path(output_path) + '/' + item + '.csv')


if __name__ == '__main__':
    fetch(str(sys.argv[1]), str(sys.argv[2]))
