import numpy as np
from neupy import algorithms
import random
#
#def draw_bin_image(image_featurerix):
#     for row in image_featurerix.tolist():
#         print('| ' + ' '.join(' *'[val] for val in row))
#        
#
#####################################################
#zero = np.featurerix(
#        [0, 1, 1, 1, 0,
#         1, 0, 0, 0, 1,
#         1, 0, 0, 0, 1,
#         1, 0, 0, 0, 1,
#         1, 0, 0, 0, 1,
#         0, 1, 1, 1, 0])
#half_zero = np.featurerix(
#        [0, 1, 1, 1, 0,
#         1, 0, 0, 0, 1,
#         1, 0, 0, 0, 1,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0])
#    
#one = np.featurerix(
#        [0, 1, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 1, 0, 0])
#half_one = np.featurerix(
#        [0, 1, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0])
#    
#two = np.featurerix(
#        [1, 1, 1, 0, 0,
#         0, 0, 0, 1, 0,
#         0, 0, 0, 1, 0,
#         0, 1, 1, 0, 0,
#         1, 0, 0, 0, 0,
#         1, 1, 1, 1, 1])
#half_two = np.featurerix(
#        [1, 1, 1, 0, 0,
#         0, 0, 0, 1, 0,
#         0, 0, 0, 1, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0])
#  
#three = np.featurerix(
#        [1, 1, 1, 1, 0,
#         0, 0, 0, 0, 1,
#         0, 1, 1, 1, 1,
#         1, 1, 1, 1, 1,
#         0, 0, 0, 0, 1,
#         1, 1, 1, 1, 0,])
#half_three = np.featurerix(
#        [1, 1, 1, 1, 1,
#         0, 0, 0, 0, 1,
#         1, 1, 1, 1, 1,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,])
#
#
#four = np.featurerix(
#        [0, 0, 1, 1, 0,
#         0, 1, 0, 1, 0,
#         1, 0, 0, 1, 0,
#         1, 1, 1, 1, 1,
#         0, 0, 0, 1, 0,
#         0, 0, 0, 1, 0,])
#half_four = np.featurerix(
#        [0, 0, 1, 1, 0,
#         0, 1, 0, 1, 0,
#         1, 0, 0, 1, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,
#         0, 0, 0, 0, 0,])
#    
#five = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 0,
#            1, 1, 1, 1, 0,
#            0, 0, 0, 0, 1,
#            0, 0, 0, 0, 1,
#            1, 1, 1, 1, 1,
#        ])
#half_five = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 0,
#            1, 1, 1, 1, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#        ])
#    
#six = np.featurerix([
#            0, 0, 1, 1, 0,
#            0, 1, 0, 0, 0,
#            1, 1, 1, 1, 0,
#            1, 0, 0, 0, 1,
#            1, 0, 0, 0, 1,
#            0, 1, 1, 1, 0,
#        ])
#half_six = np.featurerix([
#            0, 0, 1, 1, 0,
#            0, 1, 0, 0, 0,
#            1, 1, 1, 1, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#        ])   
#    
#seven = np.featurerix([
#            1, 1, 1, 1, 1,
#            0, 0, 0, 0, 1,
#            0, 0, 0, 1, 0,
#            0, 0, 1, 0, 0,
#            0, 1, 0, 0, 0,
#            1, 0, 0, 0, 0,
#        ])
#half_seven = np.featurerix([
#            1, 1, 1, 1, 1,
#            0, 0, 0, 0, 1,
#            0, 0, 0, 1, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#        ])
#    
#eight = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 1,
#            0, 1, 1, 1, 0,
#            0, 1, 1, 1, 0,
#            1, 0, 0, 0, 1,
#            1, 1, 1, 1, 1,
#        ])
#half_eight = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 1,
#            0, 1, 1, 1, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#        ])
#    
#nine = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 1,
#            1, 0, 0, 0, 1,
#            0, 1, 1, 1, 0,
#            0, 0, 0, 1, 0,
#            1, 1, 1, 0, 0,
#        ])
#half_nine = np.featurerix([
#            1, 1, 1, 1, 1,
#            1, 0, 0, 0, 1,
#            1, 0, 0, 0, 1,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#            0, 0, 0, 0, 0,
#        ])
##########################################################
##训练
#data = np.concatenate([zero, one, two, three, four], axis=0)
#dhnet = algorithms.DiscreteHopfieldNetwork(mode='sync')
#dhnet.train(data)
##########################################################
##测试
#draw_bin_image(zero.reshape((6, 5)))
#print("\n")
#draw_bin_image(half_zero.reshape((6, 5)))
#print("\n")
#result = dhnet.predict(half_zero)
#draw_bin_image(result.reshape((6, 5)))
#print("\n")
#
#
#draw_bin_image(one.reshape((6, 5)))
#print("\n")
#draw_bin_image(half_one.reshape((6, 5)))
#print("\n")
#result = dhnet.predict(half_one)
#draw_bin_image(result.reshape((6, 5)))
#print("\n")
#
#draw_bin_image(two.reshape((6, 5)))
#print("\n")
#draw_bin_image(half_two.reshape((6, 5)))
#print("\n")
#result = dhnet.predict(half_two)
#draw_bin_image(result.reshape((6, 5)))
#print("\n")
#
#draw_bin_image(three.reshape((6, 5)))
#print("\n")
#draw_bin_image(half_three.reshape((6, 5)))
#print("\n")
#result = dhnet.predict(half_three)
#draw_bin_image(result.reshape((6, 5)))
#print("\n")
#
#draw_bin_image(four.reshape((6, 5)))
#print("\n")
#draw_bin_image(half_four.reshape((6, 5)))
#print("\n")
#result = dhnet.predict(half_four)
#draw_bin_image(result.reshape((6, 5)))
#print("\n")





def train(X):
    N = len(X[0])
    print("N: ", N)
    P = len(X)
    print("P: ", P)
    feature = [0]*N
    returnfeature = []
    for i in range(N):
        m = feature[:]
        returnfeature.append(m)
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            totalweight = 0
            for u in range(P):
                totalweight += X[u][i] * X[u][j]
            returnfeature[i][j] = totalweight/float(N)
    return returnfeature


    
def predict(infeature , weighfeature):
    returnfeature = infeature
    choose = []
    for i in range(len(infeature)):
        choose.append(random.randint(0,len(infeature)-1))
    for i in choose:
        totalweight = 0
        for j in range(len(infeature)):
            totalweight += weighfeature[i][j] * infeature[j]
        if totalweight >= 0:
            returnfeature[i] = 1
        else: returnfeature[i] = -1
    return returnfeature

sample = [
        [-1, 1, 1, 1, -1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         1, -1, -1, -1, 1,
         -1, 1, 1, 1, -1],
        [-1, 1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1,
         -1, -1, 1, -1, -1],
        [1, 1, 1, -1, -1,
         -1, -1, -1, 1, -1,
         -1, -1, -1, 1, -1,
         -1, 1, 1, -1, -1,
         1, -1, -1, -1, -1,
         1, 1, 1, 1, 1],
        [1, 1, 1, 1, -1,
         -1, -1, -1, -1, 1,
         -1, 1, 1, 1, 1,
         -1, -1,-1, -1, 1,
         -1, -1, -1, -1, 1,
         1, 1, 1, 1, -1,],
        [-1, -1, 1, 1, -1,
         -1, 1, -1, 1, -1,
         1, -1, -1, 1, -1,
         1, 1, 1, 1, 1,
         -1, -1, -1, 1, -1,
         -1, -1, -1, 1, -1,]
        ]
    
def addnoise(testsample):
#    print(len(testsample))
    for x in range(6):
        for y in range(5):
            if random.randint(0, 10) > 7:
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

weightfeature =  train(sample)
draw(sample[4])
print("\n")
test = addnoise(sample[4])
draw(test)
print("\n")
for i in range(1000):
    test = predict(test,weightfeature)
draw(test)
print("\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    