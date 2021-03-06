class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item): # O(1)
        self.items.append(item)

    def pop(self): # O(1)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)


s = Stack()
print(s.isEmpty())
s.push("word")
s.push(7)
s.push(True)
print(s.size())
s.printStack()
print(s.pop())
s.printStack()
