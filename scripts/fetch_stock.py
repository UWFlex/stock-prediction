'''fetches stock data from api'''
import sys
import re
import pandas as pd
import constants
import utils

def fetch(symbol, config):
    '''fetches stock data from api, return as a pandas dataframe'''

    print('***fetching stock data for ' + symbol + '***')

    # fetch stock data for a symbol
    param_list = [
        'function=' + config['function'],
        'symbol=' + symbol,
        'outputsize=' + config['output_size'],
        'datatype=' + config['data_type'],
        'apikey=' + config['api_key']
    ]

    url = utils.url_builder(constants.BASEURL, param_list)

    json_data = utils.get_json_from_url(url)
    dataframe = {}

    try:
        dataframe = pd.DataFrame(list(json_data.values())[1]).transpose()
    except IndexError:
        print(json_data)
        dataframe = pd.DataFrame()

    pattern = re.compile('[a-zA-Z]+')
    dataframe.columns = dataframe.columns.map(lambda a: pattern.search(a).group())
    # print(dataframe)
    return dataframe

if __name__ == '__main__':
    fetch(str(sys.argv[1]), sys.argv[2])
