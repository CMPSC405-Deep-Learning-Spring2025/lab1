import numpy as np

# Activation function (can use any activation function)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Loss function
def mse_loss(y_true, y_pred):
  return ((y_true - y_pred) ** 2).mean()

# TODO: Initialize weights and biases

# TODO: Feed-forward step

# TODO: Backpropagation step (training)

# TODO: Read data from data/data.csv

# TODO: Train and test neural network