import numpy as np

def VotedPerceptron (x, T) :
    v = []
    c = []
    v.append(0)
    c.append(0)
    k = 0
    for epoch in range(T) :
        for i in range(len(x)) :
            y = np.sign(v[k] * x[i][0])
            if x[i][1] == y :
                c[k] = c[k] + 1
            else :
                v.append(v[k] + x[i][1] * x[i][0])
                c.append(1)
                k = k + 1
    return v, c

def Prediction (v, c, x) :
    s = 0
    for i in range(len(v)) :
        s = s + c[i] * np.sign(v[i] * x[0])
    return np.sign(s)

def accuracy(examples, predicted) :
    right = 0
    for i in range(len(examples)) :
        if examples[i][1] == predicted[i] :
            right = right + 1
    return right/len(examples)