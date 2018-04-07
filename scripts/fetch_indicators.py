'''fetches technical indicators from api'''
import sys
import pandas as pd
import constants
import utils


def fetch(indicator, symbol, config):
    '''fetches stock data from api, then outputs as a pandas dataframe'''

    print("fetching indicator " + indicator + " for " + symbol)
    # fetch stock data for each symbol
    dataframe = pd.DataFrame([])

    params = [
        'function=' + indicator,
        'symbol=' + symbol,
        'interval=' + config['interval'],
        'time_period=' + config['time_period'],
        'series_type=' + config['series_type'],
        'apikey=' + config['api_key']
    ]
    url = utils.url_builder(constants.BASEURL, params)

    json_data = utils.get_json_from_url(url)

    dataframe = {}
    try:
        dataframe = pd.DataFrame(list(json_data.values())[1]).transpose()
    except IndexError:
        dataframe = pd.DataFrame()

    return dataframe

if __name__ == '__main__':
    fetch(str(sys.argv[1]), str(sys.argv[2]), sys.argv[3])
