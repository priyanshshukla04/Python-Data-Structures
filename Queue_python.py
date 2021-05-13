from collections import deque

queue = deque()
queue.appendleft(23)
queue.appendleft(43)
queue.appendleft(30)
queue.appendleft(2)
print(queue)

# queue.clear()
# print(queue)
iterable = [2,4,7,0]
# queue.count()
queue.extendleft(iterable)
print(queue)

print(queue.index(4))
# print(queue.pop())