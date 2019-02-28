class Network:
    def __init__(self, layers=[]):
        self.layers = []
        self.layers.extend(layers)

    def add(self, layer):
        self.layers.append(layer)