

class ValueArray:

    def __init__(self) -> None:
        self.values:float = []
        self.count = 0
    
    def writeValueArray(self, value):
        self.values.append(value)
        self.count += 1
    
    def freeValueArray(self):
        self.values = []
        self.count = 0