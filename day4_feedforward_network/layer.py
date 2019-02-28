import numpy as np

class Layer:
    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.weights = np.random.rand(input_shape)