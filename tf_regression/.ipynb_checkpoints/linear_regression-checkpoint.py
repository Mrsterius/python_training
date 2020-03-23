import tensorflow as tf

import numpy as np

import matplotlib.pyplot as plt

learning_rate = 0.01

# steps of looping through all your data to update the parameters

training_epochs = 100

# a training set

x_train = np.linspace(0, 10, 100)

y_train = x_train + np.random.normal(0,1,100)

# set up placeholders for input and output

X = tf.placeholder(tf.float32)

Y = tf.placeholder(tf.float32)

# Define h(x) = x*w1 + w0

def h(X, w1, w0):

       return tf.add(tf.multiply(X, w1), w0)

# set up variables for weights

w0 = tf.Variable(0.0, name="weights")

w1 = tf.Variable(0.0, name="weights")

y_predicted = h(X, w1, w0)

# Define the cost function

costF = 0.5*tf.square(Y-y_predicted)

# Define the operation that will be called on each iteration

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(costF)

sess = tf.Session()

init = tf.global_variables_initializer()

sess.run(init)

# Loop through the data training

for epoch in range(training_epochs):

       for (x, y) in zip(x_train, y_train):

              sess.run(train_op, feed_dict={X: x, Y: y})

# get values of the final weights

w_val_0 = sess.run(w0)

w_val_1 = sess.run(w1)

sess.close()

# plot the data training

plt.scatter(x_train, y_train)

# plot the best fit line

y_learned = x_train*w_val_1 + w_val_0

plt.plot(x_train, y_learned, 'r')

plt.show()