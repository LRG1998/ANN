import random
class Node:

    def __init__(self):
        self.weight = random.uniform(-1.0,1.0)
        
    def report(self):
        print(self.weight)

    def updateWeight(self, rate, numinput, delta):
        self.weight += rate * numinput * delta
        return self.weight

