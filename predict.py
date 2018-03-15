import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model
import random
from tqdm import tqdm
import numpy as np

in_model = 'model_checkpoint_{}_batch_{}_epochs.h5'.format(50, 10)

print("Loading model: ", in_model)
model = load_model(in_model)
with open("teamstats2018.csv") as teamsheet:
    teamStatRows = teamsheet.read().split('\n')
    teamStatRows.pop(0)
    Rows = []
    Names = []
    for row in teamStatRows:
        teamRow = row.split(',')
        Names.append(teamRow[0])
        teamRow.pop(0)

        Rows.append(teamRow)
        print(teamRow)

answers = model.predict(Rows)
i = 0
for answer in answers:
    print(answer)
    wins = np.argmax(answer)
    print(wins)
    #print(Names[i] + " will win " + wins + " games.")
    i += 1
