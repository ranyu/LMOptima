from __future__ import print_function
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.datasets.data_utils import get_file
import numpy as np
import random, sys

'''
    Example script to generate text from Nietzsche's writings.

    At least 20 epochs are required before the generated text
    starts sounding coherent.

    It is recommended to run this script on GPU, as recurrent
    networks are quite computationally intensive.

    If you try this script on new data, make sure your corpus 
    has at least ~100k characters. ~1M is better.
'''

path = './PC-DBG-head'
#path = get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")
text = open(path).read().lower().split()
print('corpus length:', len(text))

chars = set(text)
#print (chars)
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i : i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# build the model: 2 stacked LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(len(chars), 256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, 256, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(256, len(chars)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

# helper function to sample an index from a probability array
def sample(a, diversity=0.75):
    if random.random() > diversity:
        return np.argmax(a)
    while 1:
        i = random.randint(0, len(a)-1)
        if a[i] > random.random():
            return i

# train the model, output generated text after each iteration
fw = open('RESULT.r','w')
for iteration in range(1, 60):
    print()
    #print('-' * 50)
    #fw.write('-' * 50)
    #print('Iteration', iteration)
    fw.write('Iteration:'+str(iteration)+'\n')
    model.fit(X, y, batch_size=128, nb_epoch=1)

    start_index = random.randint(0, len(text) - maxlen - 1)

    for diversity in [0.2, 0.4, 0.6, 0.8]:
        print()
       # print('----- diversity:', diversity)
        fw.write('----- diversity: '+str(diversity)+'\n')

        generated = []
        sentence = text[start_index : start_index + maxlen]
        #generated += sentence
        for s in sentence:
            #print('----- Generating with seed: "' + s + '"')
            fw.write('----- Generating with seed: "' + s + '"')
        #sys.stdout.write(generated)

        for iteration in range(400):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            generated.append(next_char)
            #sentence.append(next_char)

            #sys.stdout.write(next_char+' ')
            fw.write(next_char+' ')
            fw.flush()
fw.close()
