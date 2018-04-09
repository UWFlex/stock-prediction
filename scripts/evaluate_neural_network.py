'''evaluates a neural network model'''
import tensorflow as tf
import numpy as np
import pandas as pd
from utils import format_path

# pylint: disable=C0103

def evaluate(symbol, model_dir, data_test):
    '''evaluates model'''
    print('Evaluating model ' + symbol)

    y_test = data_test[['label']].transpose().values.flatten()
    data_test = data_test.drop(['label'], axis=1)
    X_test = data_test.values

    sess = tf.Session()

    saver = tf.train.import_meta_graph(model_dir + '/' + symbol + '.meta')
    saver.restore(sess, tf.train.latest_checkpoint(model_dir))

    graph = tf.get_default_graph()
    X = graph.get_tensor_by_name("X:0")
    Y = graph.get_tensor_by_name("Y:0")
    out = graph.get_tensor_by_name("out:0")
    mse = graph.get_tensor_by_name("mse:0")

    # Print final MSE after Training
    pred = sess.run(out, feed_dict={X: X_test})
    rel_error = abs(np.mean(((pred - y_test) / y_test)))
    mse_result = sess.run(mse, feed_dict={X: X_test, Y: y_test})
    print('MSE on test set: ' + str(mse_result))
    print('Relative error: ' + str("{:.2%}".format(rel_error)))
    return mse_result, rel_error


def evaluate_batch(symbols_file, data_path):
    '''prep data for evaluating'''
    symbols = []
    with open(format_path(symbols_file), 'r') as data:
        read_data = data.read()
        symbols = str(read_data).split()

    for symbol in symbols:
        test_data = pd.read_csv(format_path(data_path + '/' + symbol + '.csv'), index_col='date')

        model_dir = format_path('output/models/' + symbol)

        evaluate(symbol, model_dir, test_data)

    print('batch evaluation finished')
