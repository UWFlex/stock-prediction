'''fetches technical indicators from api'''
import sys
import pandas as pd
import constants
import utils


def fetch(symbol, config):
    '''fetches stock data from api, then outputs as a pandas dataframe'''

    # read from indicators file
    indicators = []
    with open(utils.format_path('input/technical_indicators'), 'r') as data:
        read_data = data.read()
        indicators = str(read_data).split()

    # fetch stock data for each symbol
    for indicator in indicators:
        params = [
            'function=' + indicator,
            'symbol=' + symbol,
            'interval=' + config['interval'],
            'time_period=' + config['time_period'],
            'series_type=' + config['series_type'],
            'apikey=' + config['apikey']
        ]
        url = utils.url_builder(constants.BASEURL, params)

        json_data = utils.get_json_from_url(url)
        dataframe = pd.DataFrame(list(json_data.values())[1])
        # print(dataframe)
        return dataframe

if __name__ == '__main__':
    fetch(str(sys.argv[1]), sys.argv[2])
