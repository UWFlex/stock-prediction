# pylint: disable=R0914
'''fetches stock data joined with technical indicators'''
from functools import reduce
import sys
import time
import pandas as pd
import constants
import utils
import fetch_stock
import fetch_indicators

def fetch(symbols_file, indicators_file, output_path):
    '''fetches stock data combined with technical indicators, output as csv'''

    # read from symbols file
    stocks = []
    with open(utils.format_path(symbols_file), 'r') as data:
        read_data = data.read()
        stocks = str(read_data).split()

    # read from indicators file
    indicators = []
    with open(utils.format_path(indicators_file), 'r') as data:
        read_data = data.read()
        indicators = str(read_data).split()

    stocks_config = {
        'function': constants.TIME_SERIES_DAILY_ADJUSTED,
        'output_size': constants.OUTPUTSIZE_FULL,
        'data_type': constants.DATATYPE_JSON,
        'api_key': constants.API_KEY
    }

    indicators_config = {
        'interval': constants.INTERVAL,
        'time_period': constants.TIME_PERIOD,
        'series_type': constants.SERIES_TYPE,
        'api_key': constants.API_KEY
    }

    for stock in stocks:
        start = time.time()

        stock_data = fetch_stock.fetch(stock, stocks_config)

        time.sleep(1)

        dfs = []
        dfs.append(stock_data)
        for indicator in indicators:
            indicator_data = fetch_indicators.fetch(indicator, stock, indicators_config)

            time.sleep(1)

            dfs.append(indicator_data)

        stock_indicators_joined = reduce(
            lambda left, right:
            pd.merge(
                left,
                right,
                left_index=True,
                right_index=True,
                how='outer'
            ), dfs)

        stock_indicators_joined.index.name = 'date'

        # print(stock_indicators_joined)

        print('fetched and joined data for ' + stock)

        formatted_output_path = utils.format_path(output_path)
        utils.make_dir_if_not_exists(output_path)
        stock_indicators_joined.to_csv(formatted_output_path + '/' + stock + '.csv')
        print('saved csv file to ' + formatted_output_path + '/' + stock + '.csv')

        elapsed = time.time() - start
        print('time elapsed: ' + str(round(elapsed, 2)) + " seconds")

if __name__ == '__main__':
    fetch(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
