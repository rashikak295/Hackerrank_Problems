class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if self.first == []:
            while self.second != []:
                self.first.append(self.second.pop())
        return self.first[-1]
    
    def pop(self):
        if self.first == []:
            while self.second != []:
                self.first.append(self.second.pop())
        if self.first != []:
            self.first.pop()
                
    def put(self, value):
        self.second.append(value)