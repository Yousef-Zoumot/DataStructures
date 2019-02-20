
# This implementation assumes the rear position is at 0
# which allows us to use the insert function on lists to
# add new elements, and the pop function to remove the
# front element (which is at the end of the list)
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item): # O(n)
        self.items.insert(0, item)

    def dequeue(self): # O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)



# Test code
q = Queue()
q.isEmpty()
q.enqueue("word")
q.enqueue(7)
q.enqueue(True)
q.size()
q.printQueue()
q.dequeue()
q.printQueue()
q.size()
q.isEmpty()
