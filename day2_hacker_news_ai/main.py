from keras import optimizers
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.preprocessing.text import one_hot, text_to_word_sequence
import hn_data
import numpy as np
import requests
import tensorflow as tf
# import random


# Mute Tensorflow
tf.logging.set_verbosity(tf.logging.ERROR)

# Load the data, and turn it into data for keras/numpy.
raw_data = hn_data.load_data()

# We want to come up with a vocabulary of all words found in titles.
vocab = []


def add_to_vocab(item):
    title_words = text_to_word_sequence(item['title'])
    vocab.extend(title_words)


for item in raw_data:
    add_to_vocab(item)

# Now that we've found all unique words, we can turn our data in numpy arrays.
x_train = []
y_train = []

# For each word in each title, we'll try to compute the impact it has on
# a post's score.


def none_to_zero(x):
    if x is None:
        return 0
    else:
        return x


def normalize_item(item):
    title_words = text_to_word_sequence(item['title'])
    title_words = set(title_words)
    vocab_size = len(set(vocab))
    training_inputs = []
    training_outputs = []
    for word in title_words:
        training_outputs.append([none_to_zero(item['points'])])
        training_inputs.append(np.array([
            item['time'],
            item['comments_count'],
            one_hot(word, round(vocab_size * 1.3))[0]
        ]))
    return title_words, training_inputs, training_outputs


for item in raw_data:
    _, xs, ys = normalize_item(item)
    x_train.extend(xs)
    y_train.extend(ys)

# TODO: Reservoir sampling, split the data up

# Make our model. We'll assume this is a linear problem,
# so we only need one layer.
model = Sequential()
model.add(Dense(1, activation='linear'))
model.compile(loss='msle',
              optimizer=optimizers.Adam(lr=0.01),
              metrics=['accuracy'])

# Now, train the model.
model.fit(np.array(x_train), np.array(y_train), epochs=10)

while True:
    item_id = int(input("Enter the id of an item: "))
    r = requests.get(f"https://api.hnpwa.com/v0/item/{item_id}.json")
    item = r.json()
    add_to_vocab(item)
    score_sum = 0
    words, xs, ys = normalize_item(item)

    for x in xs:
        x = np.array([x])
        computed = model.predict(x)[0][0]
        print(computed)
        score_sum += computed

    computed_score = round(score_sum / len(xs))
    print(f"Predicted score: {computed_score}")
    print(f"Actual score: {item['points']}")
