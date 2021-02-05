import VPerceptron
import csv
import math
import pandas
import random
import numpy as np


T = 100
k = 10
test_accuracy = []


#lettura primo dataset
datafile = open('Roman Urdu DataSet.csv', 'r', encoding = "utf-8" )
myreader = csv.reader(datafile)
#codifica esempi e classi
x1 = []
y1 = []
i = 1
for row in myreader :
    x1.append(i)
    i = i + 1
    if row[1] == 'Positive' :
        y1.append(1)
    else :
        y1.append(-1)
#liste di esempi di classe positiva e negativa
x1pos = []
x1neg = []
for i in range(len(y1)) :
    if y1[i] > 0 :
        x1pos.append(x1[i])
    else :
        x1neg.append(x1[i])

for j in range(k) :
    random.shuffle(x1pos)
    random.shuffle(x1neg)
    #creazione training set e data set
    x1train = []
    x1test = []
    for i in range(int(math.modf(len(x1pos) * 0.8)[1])) :
        x1train.append((x1pos[i], 1))
    for i in range(int(math.modf(len(x1pos) * 0.8)[1]), len(x1pos)) :
        x1test.append((x1pos[i], 1))
    for i in range(int(math.modf(len(x1neg) * 0.8)[1])) :
        x1train.append((x1neg[i], -1))
    for i in range(int(math.modf(len(x1neg) * 0.8)[1]), len(x1neg)) :
        x1test.append((x1neg[i], -1))
    #train
    v1, c1 = VPerceptron.VotedPerceptron(x1train, T)
    #test
    y1result = []
    for i in range(len(x1test)) :
        y1result.append(VPerceptron.Prediction(v1, c1, x1test[i]))

    test_accuracy.append(VPerceptron.accuracy(x1test, y1result))


#lettura secondo dataset
data = pandas.read_csv('datatraining.txt')
#codifica esempi e classi
points = []
i = 1
for row in data['date'] :
    points.append(i)
    i = i + 1
data['Points'] = points
y2 = []
for i in data['Occupancy'] :
    if i == 1 :
        y2.append(1)
    else :
        y2.append(-1)

x2 = []
for i in data['Points'] :
    x2.append(i)
#liste di esempi di classe positiva e negativa
x2pos = []
x2neg = []
for i in range(len(y2)) :
    if y2[i] > 0 :
        x2pos.append(x2[i])
    else :
        x2neg.append(x2[i])

for j in range(k) :
    random.shuffle(x2pos)
    random.shuffle(x2neg)
    #creazione training set e test set
    x2train = []
    x2test = []
    for i in range(int(math.modf(len(x2pos) * 0.8)[1])) :
        x2train.append((x2pos[i], 1))
    for i in range(int(math.modf(len(x2pos) * 0.8)[1]), len(x2pos)) :
        x2test.append((x2pos[i], 1))
    for i in range(int(math.modf(len(x2neg) * 0.8)[1])) :
        x2train.append((x2neg[i], -1))
    for i in range(int(math.modf(len(x2neg) * 0.8)[1]), len(x2neg)) :
        x2test.append((x2neg[i], -1))
    #train
    v2, c2 = VPerceptron.VotedPerceptron(x2train, T)
    #test
    y2result = []
    for i in range(len(x2test)) :
        y2result.append(VPerceptron.Prediction(v2, c2, x2test[i]))
    test_accuracy.append(VPerceptron.accuracy(x2test, y2result))


#lettura terzo dataset
datafile = open('winequality-red.csv', 'r')
myreader = csv.reader(datafile, delimiter = ';')
next(myreader)
#codifica esempi e classi
x3 = []
y3 = []
i = 1
for row in myreader :
    x3.append(i)
    i = i + 1
    if int(row[11]) <= 5 :
        y3.append(1)
    else :
        y3.append(-1)
#liste di esempi di classe positiva e negativa
x3pos = []
x3neg = []
for i in range(len(y3)) :
    if y3[i] > 0 :
        x3pos.append(x3[i])
    else :
        x3neg.append(x3[i])

for j in range(k) :
    random.shuffle(x3pos)
    random.shuffle(x3neg)
    #creazione training set e data set
    x3train = []
    x3test = []
    for i in range(int(math.modf(len(x3pos) * 0.8)[1])) :
        x3train.append((x3pos[i], 1))
    for i in range(int(math.modf(len(x3pos) * 0.8)[1]), len(x3pos)) :
        x3test.append((x3pos[i], 1))
    for i in range(int(math.modf(len(x3neg) * 0.8)[1])) :
        x3train.append((x3neg[i], -1))
    for i in range(int(math.modf(len(x3neg) * 0.8)[1]), len(x3neg)) :
        x3test.append((x3neg[i], -1))
    #train
    v3, c3 = VPerceptron.VotedPerceptron(x3train, T)
    #test
    y3result = []
    for i in range(len(x3test)) :
        y3result.append(VPerceptron.Prediction(v3, c3, x3test[i]))

    test_accuracy.append(VPerceptron.accuracy(x3test, y3result))

#lettura quarto dataset
datafile = open('winequality-white.csv', 'r')
myreader = csv.reader(datafile, delimiter = ';')
next(myreader)
#codifica esempi e classi
x4 = []
y4 = []
i = 1
for row in myreader :
    x4.append(i)
    i = i + 1
    if int(row[11]) < 5 :
        y4.append(1)
    else :
        y4.append(-1)
#liste di esempi di classe positiva e negativa
x4pos = []
x4neg = []
for i in range(len(y4)) :
    if y4[i] > 0 :
        x4pos.append(x4[i])
    else :
        x4neg.append(x4[i])

for j in range(k) :
    random.shuffle(x4pos)
    random.shuffle(x4neg)
    #creazione training set e data set
    x4train = []
    x4test = []
    for i in range(int(math.modf(len(x4pos) * 0.8)[1])) :
        x4train.append((x4pos[i], 1))
    for i in range(int(math.modf(len(x4pos) * 0.8)[1]), len(x4pos)) :
        x4test.append((x4pos[i], 1))
    for i in range(int(math.modf(len(x4neg) * 0.8)[1])) :
        x4train.append((x4neg[i], -1))
    for i in range(int(math.modf(len(x4neg) * 0.8)[1]), len(x4neg)) :
        x4test.append((x4neg[i], -1))
    #train
    v4, c4 = VPerceptron.VotedPerceptron(x4train, T)
    #test
    y4result = []
    for i in range(len(x4test)) :
        y4result.append(VPerceptron.Prediction(v4, c4, x4test[i]))

    test_accuracy.append(VPerceptron.accuracy(x4test, y4result))

print(np.nanmean(test_accuracy))
print(np.nanstd(test_accuracy))