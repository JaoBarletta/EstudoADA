class Pilha:
    def __init__(self,size) -> None:
        self.size = size
        self.data = []

    def push(self,item) -> object:
        self.data.append(item)
        
    def pop(self) -> None:
        print(self.data[-1])
        del self.data[-1]
    
    def data_clear(self):
        self.data.clear()
        return True

    def isFull(self):
        if self.size == len(self.data):
            return True
        else:
            return False