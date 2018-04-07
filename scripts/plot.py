'''plotting data'''
import sys
import pandas as pd
import matplotlib.pyplot as plt
from utils import format_path

def plot_closing_adj(symbol):
    '''plots the daily adjusted closing price vs. time'''
    data = pd.read_csv(format_path('output/raw/') + symbol + '.csv', index_col='date')
    print('plotting data for ' + symbol + '...')
    print('data dimensions ' + str(data.shape))
    plt.plot(data.index.values, data['adjusted'].values)
    plt.show()

if __name__ == 'main':
    plot_closing_adj(str(sys.argv[0]))
