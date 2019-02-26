from keras.preprocessing.text import one_hot, text_to_word_sequence
import hn_data
import numpy as np

# Load the data, and turn it into data for keras/numpy.
raw_data = hn_data.load_data()

# We want to come up with a vocabulary of all words found in titles.
vocab = []
for item in raw_data:
    title_words = text_to_word_sequence(item['title'])
    vocab.extend(title_words)

# Now that we've found all unique words, we can turn our data in numpy arrays.
vocab_size = len(set(vocab))
vocab_size = round(vocab_size * 1.3)
training_inputs = []
training_outputs = []

# For each word in each title, we'll try to compute the impact it has on
# a post's score.
for item in raw_data:
    title_words = text_to_word_sequence(item['title'])
    title_words = set(title_words)
    for word in title_words:
        training_outputs.append(np.array([item['points']]))
        training_inputs.append(np.array([
            item['time'],
            item['comments_count'],
            one_hot(word, vocab_size)[0]
        ]))
