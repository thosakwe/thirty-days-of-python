from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import RMSprop
import numpy as np

# z = 3x + 5y + 2
xy_train = np.random.uniform(size=(1000, 2))
z_train = xy_train * (3, 5)
z_train = np.sum(z_train, axis=1) + 2

# Make our model
model = Sequential()
model.add(Dense(1))

model.compile(loss='mse',
              optimizer=RMSprop(lr=0.01),
              metrics=['mse'])
model.fit(xy_train, z_train, epochs=100)

while True:
    x = float(input("Enter an x: "))
    y = float(input("Enter a y: "))
    arr = np.array([x, y])
    arr = np.reshape(arr, (1, 2))
    actual = arr * (3, 5)
    actual = np.sum(actual, axis=1) + 2
    out = model.predict(arr)[0][0]
    out = round(out)
    print("Computed (rounded): " + str(out))
    print("Actual: " + str((3 * x) + (5 * y) + 2))
    print("Actual (numpy): " + str(actual))
