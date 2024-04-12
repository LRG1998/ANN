import random
class ttlist:
    def __init__(self):
        self.input1 = []
        self.output = []
        while len(self.input1) < 500:
            self.input1.append(random.uniform(-5.0,5.0))
        for i in range(len(self.input1)):
            self.output.append(self.input1[i] * 2)
    

