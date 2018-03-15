import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model
import random
from tqdm import tqdm
import numpy as np

batch_size =50
epochs = 10
test_size = 8
in_model = 'model_checkpoint_{}_batch_{}_epochs.h5'.format(batch_size, epochs)
out_model = 'model_checkpoint_{}_batch_{}_epochs.h5'.format(batch_size, epochs)
load_prev_model = False

gamesWon = [0, 1, 2, 3, 4, 5, 6]
testAnswer = [0, 0, 0, 0, 0, 0, 0]
if load_prev_model:
    print("Loading model: ", in_model)
    model = load_model(in_model)
else:
    print("starting fresh!")
    model = Sequential()
with open("teamstats2017.csv") as teamsheet:
    teamStatRows = teamsheet.read().split('\n')
    teamStatRows.pop(0)
    answers = []
    Rows = []
    for row in teamStatRows:
        teamRow = row.split(',')
        teamRow.pop(0)
        length = len(teamRow)
        specificAnswer=testAnswer
        specificAnswer[int(teamRow[length - 1])]=1
        answers.append(specificAnswer)
        teamRow.pop(length - 1)
        Rows.append(teamRow)
        print(teamRow)

np.save("Rows.npy", Rows)
np.save("answers.npy", answers)

Rows = np.load("Rows.npy")
answers = np.load("answers.npy")

x_train = Rows[:-test_size]
y_train = answers[:-test_size]

x_test = Rows[-test_size:]
y_test = answers[-test_size:]

print('Building model...')
if not load_prev_model:
    model = Sequential()
    model.add(Dense(256, input_shape=(len(Rows[0]),)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(256, input_shape=(256,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(answers[0])))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_split=0.1)
score = model.evaluate(x_test, y_test,
                       batch_size=batch_size, verbose=1)
model.save(out_model)
print("Model saved to:", out_model)
print('Test score:', score[0])
print('Test accuracy:', score[1])
