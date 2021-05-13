import time
import threading
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def if_empty(self):
        return len(self.buffer) == 0

    def front(self):
        return self.buffer[-1]


food_order = Queue()


def place_order(orders):
    for i in orders:
        print("Placing order: ", i)
        food_order.enqueue(i)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        order = food_order.dequeue()
        print("Serving now: ", order)
        time.sleep(2)


def binary_number(n):
    numbers = Queue()
    numbers.enqueue("1")

    for i in range(n):
        front = numbers.front()
        print(" ", front)
        numbers.enqueue(front + "0")
        numbers.enqueue(front + "1")

        numbers.dequeue()


# q = Queue()
# orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
# t1 = threading.Thread(target=place_order, args=(orders,))
# t2 = threading.Thread(target=serve_order)
#
# t1.start()
# t2.start()
# q.enqueue(12)
# q.enqueue(23)
# q.enqueue(1)
# q.enqueue(10)
#
# print(q.dequeue())

# print(q.size())
# print(q.if_empty())
binary_number(10)
