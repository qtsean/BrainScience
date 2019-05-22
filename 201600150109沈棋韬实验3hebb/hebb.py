# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:20:10 2019

@author: QITAO SHEN
"""

import numpy as np
import random
class Hebb(object):
    def __init__(self):
        self.weights = np.zeros((30, 30))
#        print(self.weights)
    
    def train(self, input_vector, iter_, rate):
        for it in range(iter_):
#            print(input_vector)
            for vec in input_vector:
#                vec = np.array(vec)
#                self.weights = self.weights + rate * np.dot(vec.T, vec)
#                print(vec)
                for i in range(len(vec)):
                    for j in range(len(vec)):
                        self.weights[i][j] += vec[i] * vec[j]
        return self.weights
    def predict(self, input_vector):
        output = np.dot(self.weights, input_vector.T)
        return output
    
def activation(x):
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = 1
        else:
            x[i] = -1
    return x

def addnoise(testsample):
    for x in range(6):
        for y in range(5):
            if random.randint(0, 10) > 9:
                if testsample[x * 5 + y] == 1:
                    testsample[x * 5 + y] = -1
                else:
                    testsample[x * 5 + y] = 1
    return testsample

def draw(data):
    for j in range(6):
        ch = ""
        for i in range(5):
            ch += " " if data[j*5+i] == -1 else "*"
        print(ch)
        

zero = np.array(
        [-1, 1, 1, 1, -1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         -1, 1, 1, 1, -1])

one = np.array(
        [-1, 1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1])
    
two = np.array(
        [1, 1, 1, -1, -1,
         -1, -1, -1, 1, -1,
         -1, -1, -1, 1, -1,
         -1, 1, 1, -1, -1,
         1, -1, -1, -1, -1,
         1, 1, 1, 1, 1])   
    
noise_zero = addnoise(zero.copy())
noise_one = addnoise(one.copy())
noise_two = addnoise(two.copy())




hebb = Hebb()
hebb.train([zero, one, two], 100, 1)

pred_zero = hebb.predict(noise_zero)
pred_one = hebb.predict(noise_one)
pred_two = hebb.predict(noise_two)

pred_zero = activation(pred_zero)
pred_one = activation(pred_one)
pred_two = activation(pred_two)

draw(zero)
draw(noise_zero)
draw(pred_zero)

draw(one)
draw(noise_one)
draw(pred_one)

draw(two)
draw(noise_two)
draw(pred_two)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    