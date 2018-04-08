'''scales data to work better with neural network activation functions'''
import time
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from utils import get_filename_list, format_path, make_dir_if_not_exists

def fill_missing(data):
    '''
    fills last observed forward,
    after that, perform back fill,
    then fill remaining NaN with 0s
    '''

    # last observed carries forward
    data.fillna(method='ffill', inplace=True)

    # fill forward
    data.fillna(method='bfill', inplace=True)

    data.fillna(value=0, inplace=True)

    return data

def scale(train_data, test_data):
    '''scales data using sklearn MinMaxScaler'''
    scaler = MinMaxScaler()
    scaler.fit(train_data)
    train_data_np = scaler.transform(train_data)
    test_data_np = scaler.transform(test_data)
    train_data = pd.DataFrame(train_data_np, index=train_data.index, columns=train_data.columns)
    test_data = pd.DataFrame(test_data_np, index=test_data.index, columns=test_data.columns)
    return train_data, test_data

def split(data, train_ratio):
    '''split into training and testing data sets'''

    # num of rows in data
    rows = data.shape[0]

    # training parameters
    split_point = int(train_ratio * rows)

    # split into two dataframes
    data_train = data.iloc[:split_point, :]
    data_test = data.iloc[split_point:, :]

    return data_train, data_test

def construct_label(data):
    '''appends the label column by shifting it down (1 day ahead)'''
    data['label'] = data['adjusted']
    data['label'] = data['label'].shift(-1)
    return data.drop(data.index[len(data)-1])


def preprocess(data, train_ratio):
    '''perform preprocessing on data'''

    data = construct_label(data)

    # fill missing values
    data = fill_missing(data)

    # split into training and testing
    train_data, test_data = split(data, train_ratio)

    # scale train and test dataset
    train_data, test_data = scale(train_data, test_data)

    return train_data, test_data

def preprocess_batch(input_path, output_path, train_ratio):
    '''perform preprocessing on all input data csvs'''
    start = time.time()
    files = get_filename_list(input_path, 'csv')

    for file in files:
        symbol = file.split('.')[0]

        print("preprocessing " + symbol)

        data = pd.read_csv(format_path(input_path + '/' + file), index_col='date')

        train_data, test_data = preprocess(data, train_ratio)

        formatted_output = format_path(output_path)
        make_dir_if_not_exists(formatted_output + '/train')
        make_dir_if_not_exists(formatted_output + '/test')
        train_data.to_csv(formatted_output + '/train' + '/' + symbol + '.csv')
        test_data.to_csv(formatted_output + '/test' + '/' + symbol + '.csv')
        print('saved csv files to ' + formatted_output + '{train, test}/' + symbol + '.csv')

    print("preprocessing complete")
    elapsed = time.time() - start
    print('time elapsed: ' + str(round(elapsed, 2)) + " seconds")
