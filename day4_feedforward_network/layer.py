import numpy as np

class Layer:
    def __init__(self, activation, input_shape):
        self.activation = activation
        self.input_shape = input_shape
        self.weights = np.random.uniform(size=input_shape)