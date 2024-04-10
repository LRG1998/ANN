from Node import Node
import random
from array import *

#Only value you can change
learningRate = 0.001
numberInput = 10
numberOutput = numberInput * 2


#Constructing node network

netwidth, netheight = (4,2)

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
    deltas = [5]*5
    deltas[0] = -difference()
    for i in range(1,5):
        deltas[i] = deltas[0] * secondLayer[i-1].weight
    return deltas

def updateNodes():
    for x in range(len(secondLayer)):
        secondLayer[x].updateWeight(learningRate,output(x),findDelta()[0])

    for x in range(netheight):
        for y in range(netwidth):
            network[x][y].updateWeight(learningRate,numberInput,findDelta()[y+1])

def run():
    while abs(difference()) > 0.05:
        if abs(difference()) >= float('inf'):
            break
        updateNodes()
        print(result())

run()