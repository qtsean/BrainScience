# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:44:40 2019

@author: QITAO SHEN
"""
import numpy as np

def activation(x):
    if x > 0:
        return 1
    else:
        return 0

class perception(object):
    def __init__(self):
        self.weights = np.random.random(3)
        self.bias = 0
        
    def train(self, feature, label, iter, lr):
        for i in range(iter):
#            print('iteration: ', i)
            for i in range(len(feature)):
                output = 0
                output = np.sum(feature[i] * self.weights)
                output += self.bias
#                print(output)
                output = activation(output)
                self.weights = self.weights + lr * (label[i] - output) * np.array(feature[i])
                self.bias = self.bias + lr * (label[i] - output)

    def predict(self, feature):
        output = 0
        for i in range(len(self.weights)):
            output += self.weights[i] * feature[i]
        output += self.bias
#        print(output)
        output = activation(output)
        return output

data_feature = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])

data_label = np.array([
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1
])

classfier = perception()
classfier.train(data_feature, data_label, 1000, 0.001)

test_feature = np.array([0,1,1])
result = classfier.predict(test_feature)

print('Input data: ', test_feature)
print('reslut: ', result)


























