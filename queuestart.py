"""queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
print("initial queue")
print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)"""
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        return self.items.pop(0)
q=Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        q.enqueue(int(do[1]))
    elif operation == 'dequeue':
        if q.is_empty():
            print('Queue is empty.')
        else:
            print('Dequeued value: ', q.dequeue())
    elif operation == 'quit':
        break
          
