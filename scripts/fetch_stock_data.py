'''fetches stock data from api'''
import urllib.request
import sys
import json
import pandas as pd
import constants
import utils


def fetch(symbol, config):
    '''fetches stock data from api, return as a pandas dataframe'''

    # fetch stock data for a symbol
    param_list = [
        'function=' + config['function'],
        'symbol=' + symbol,
        'outputsize=' + config['outputsize'],
        'datatype=' + config['datatype'],
        'apikey=' + config['apikey']
    ]

    raw_url = utils.url_builder(constants.BASEURL, param_list)

    with urllib.request.urlopen(raw_url) as url:
        data = json.loads(url.read().decode())
        dataframe = pd.DataFrame(data['Time Series (Daily)'])
        # print(dataframe)
        return dataframe


if __name__ == '__main__':
    fetch(str(sys.argv[1]), sys.argv[2])
