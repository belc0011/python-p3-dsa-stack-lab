class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.full():
            return self.items
        else:
            self.items.append(item)
            return self.items

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        found = False
        for index, element in enumerate(self.items):
            if element == target:
                found = True
                index_number = index
        if found:
            return len(self.items) - index_number - 1
        else:
            return -1
            
