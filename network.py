from Node import Node
import random
from array import *

''' Spongegar ANN
    Doesn't handle zeroes as of 4/12/2024
    Copyright Jordan Veldkamp'''


#Only value you can change
learningRate = 0.01
numberInput = 1
numberOutput = numberInput * 2
confidence = 0.05
netwidth = 3
epoch = 4000


#Constructing node network

netheight = (2)

network = [[0 for x in range(netwidth)]for y in range(netheight)]
for x in range(netheight):
    for y in range(netwidth):
        network[x][y] = Node()
secondLayer = [0 for x in range(netwidth)]
for x in range(len(secondLayer)):
    secondLayer[x] = Node()

#functionality for network
def output(nodeNum):
    numOut = 0
    numOut = numberInput * network[0][nodeNum-1].weight + 2 * network[1][nodeNum-1].weight
    return numOut

def result():
    result = 0
    for r in range(netwidth):
        result += output(r) * secondLayer[r].weight
    return output(r)

def difference():
    diff = numberOutput-result()
    return diff

def findDelta():
    deltas = [5]*(netwidth + 1)
    deltas[0] = -difference()
    for i in range(1,netwidth + 1):
        deltas[i] = deltas[0] * secondLayer[i-1].weight
    return deltas

def updateNodes():
    for x in range(len(secondLayer)):
        secondLayer[x].updateWeight(learningRate,output(x),findDelta()[0])

    for x in range(netheight):
        for y in range(netwidth):
            network[x][y].updateWeight(learningRate,numberInput,findDelta()[y+1])

def run():
    iteration = 0
    while abs(difference()) > confidence:
        if abs(difference()) >= float('inf'):
            break
        updateNodes()
        print(result())
        iteration += 1
        if iteration > epoch:
            print("Can't find solution.")
            break
    for x in range(netwidth):
        for y in range(netheight):
            print("Node" + str(x) + str(y) + ": " + str(network[y][x].weight))

run()