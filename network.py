from Node import Node
from ttlist import ttlist

''' Spongegar ANN
    Doesn't handle zeroes as of 4/12/2024
    Copyright Jordan Veldkamp'''


#Only value you can change
learningRate = 0.00000001
input1 = 1
input2 = 2
confidence = 0.05
netwidth = 1
stopcounter = 6

outputfile = open("output.txt", 'w')
trainset = ttlist()
testset = ttlist()
print(trainset.input1.pop())

#Constructing node network
epoch = stopcounter * 1000
numberOutput = input1 * input2

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
    numOut = input1 * network[0][nodeNum-1].weight + input2 * network[1][nodeNum-1].weight
    return numOut

#outputs the values
def result():
    result = 0
    for r in range(netwidth):
        result += output(r) * secondLayer[r].weight
    return output(r)

#Finds the difference between the intended output and the result
def difference():
    diff = numberOutput-result()
    return diff

#Creates an array for deltas, with a length of the netwidth
def findDelta():
    deltas = [5]*(netwidth + 1)
    deltas[0] = -difference()
    for i in range(1,netwidth + 1):
        deltas[i] = deltas[0] * secondLayer[i-1].weight
    return deltas

#updates the node weights using the learning rate, the output, and the deltas
def updateNodes():
    for x in range(len(secondLayer)):
        secondLayer[x].updateWeight(learningRate,output(x),findDelta()[0])

    for x in range(netheight):
        for y in range(netwidth):
            network[x][y].updateWeight(learningRate,input1,findDelta()[y+1])

#Main functionality of the network
def train():
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
            outputfile.write("Node" + str(x) + str(y) + ": " + str(network[y][x].weight) + " ")
            outputfile.write("\n")

while len(trainset.input1) > 0:
    input1 = trainset.input1.pop()
    train()

outputfile.close()