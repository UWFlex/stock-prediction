'''trains a neural network model in TensorFlow'''
import sys
import time
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import format_path, make_dir_if_not_exists, remove_dir

# pylint: skip-file

def train_batch(symbols_file, data_path, export_dir):
    '''prep data for training'''
    # read from symbols file
    symbols = []
    with open(format_path(symbols_file), 'r') as data:
        read_data = data.read()
        symbols = str(read_data).split()

    for symbol in symbols:
        print('training neural network model for ' + symbol)
        train_data = pd.read_csv(format_path(data_path + '/train/' + symbol + '.csv'), index_col='date')
        test_data = pd.read_csv(format_path(data_path + '/test/' + symbol + '.csv'), index_col='date')

        model_dir = format_path(export_dir + '/' + symbol)
        remove_dir(model_dir)
        train(train_data, test_data, format_path(model_dir))

        print('training finished for ' + symbol)

def train(data_train, data_test, export_dir):
    '''trains a neural network'''
    start_time = time.time()

    # Build X and y
    y_train = data_train[['label']].transpose().values.flatten()
    data_train = data_train.drop(['label'], axis=1)
    X_train = data_train.values

    y_test = data_test[['label']].transpose().values.flatten()
    data_test = data_test.drop(['label'], axis=1)
    X_test = data_test.values

    # number of training examples
    # n = data.shape[0]
    p = X_train.shape[1]

    # Placeholder, None means we don't yet know the number of observations flowing through
    X = tf.placeholder(dtype=tf.float32, shape=[None, p], name='X')
    Y = tf.placeholder(dtype=tf.float32, shape=[None], name='Y')

    # Model architecture parameters
    n_neurons_1 = 64
    n_neurons_2 = 32
    n_neurons_3 = 16
    n_target = 1

    # Initializers
    sigma = 1
    weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
    bias_initializer = tf.zeros_initializer()

    # Layer 1: Variables for hidden weights and biases
    W_hidden_1 = tf.Variable(weight_initializer([p, n_neurons_1]))
    bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
    # Layer 2: Variables for hidden weights and biases
    W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
    bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
    # Layer 3: Variables for hidden weights and biases
    W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
    bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))

    # Output layer: Variables for output weights and biases
    W_out = tf.Variable(weight_initializer([n_neurons_3, n_target]))
    bias_out = tf.Variable(bias_initializer([n_target]))

    # Hidden layer
    hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
    hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
    hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))

    # Output layer (must be transposed)
    out = tf.add(tf.matmul(hidden_3, W_out), bias_out, name='out')

    # Cost function
    mse = tf.reduce_mean(tf.squared_difference(out, Y), name='mse')

    # Optimizer
    opt = tf.train.AdamOptimizer().minimize(mse)

    # Make Session
    net = tf.Session()

    # Run initializer
    net.run(tf.global_variables_initializer())

    # Setup plot
    plt.ion()
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    line1, = ax1.plot(y_test)
    line2, = ax1.plot(y_test * 0.5)
    plt.show()

    # Fit neural net
    batch_size = 1
    mse_train = []
    mse_test = []

    # Run
    epochs = 20
    for e in range(epochs):

        # Shuffle training data
        shuffle_indices = np.random.permutation(np.arange(len(y_train)))
        X_train = X_train[shuffle_indices]
        y_train = y_train[shuffle_indices]

        # Minibatch training
        for i in range(0, len(y_train) // batch_size):
            start = i * batch_size
            batch_x = X_train[start:start + batch_size]
            batch_y = y_train[start:start + batch_size]

            # Run optimizer with batch
            net.run(opt, feed_dict={X: batch_x, Y: batch_y})

        # MSE train and test
        mse_train.append(net.run(mse, feed_dict={X: X_train, Y: y_train}))
        mse_test.append(net.run(mse, feed_dict={X: X_test, Y: y_test}))

        print('Epoch ' + str(e))
        print('MSE Train: ', mse_train[-1])
        print('MSE Test: ', mse_test[-1])

        # Prediction
        pred = net.run(out, feed_dict={X: X_test})
        rel_error = abs(np.mean(((pred - y_test) / y_test)))
        print('Relative error: ' + str("{:.2%}".format(rel_error)))

        line2.set_ydata(pred)
        plt.title('Epoch ' + str(e) + ', Batch ' + str(i))
        plt.pause(0.001)

    # Print final MSE after Training
    pred_final = net.run(out, feed_dict={X: X_test})
    rel_error = abs(np.mean(((pred_final - y_test) / y_test)))
    mse_final = net.run(mse, feed_dict={X: X_test, Y: y_test})
    print('Final MSE test: ' + str(mse_final))
    print('Final Relative error: ' + str("{:.2%}".format(rel_error)))
    print('Total training set count: ' + str(len(y_train)))
    print('Total test set count: ' + str(len(y_test)))

    savemodel(net, export_dir)

    elapsed = time.time() - start_time
    print('time elapsed: ' + str(round(elapsed, 2)) + " seconds")


def savemodel(sess, export_dir):
    saver = tf.train.Saver()
    saver.save(sess, export_dir + '/MSFT')
    print('Saved model to ' + export_dir)


if __name__ == '__main__':
    train_batch(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
