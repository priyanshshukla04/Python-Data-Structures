from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def size(self):
        return len(self.container)

    def push(self, data):
        self.container.append(data)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    # def print(self):
    #     for i in self.container:
    #         print(i, end=" ")
    #     print()


def reverse_string(string):
    stack = Stack()
    for i in string:
        stack.push(i)
    temp = ''
    while stack.size() != 0:
        temp += stack.pop()
    return temp


if __name__ == '__main__':
    # s1 = Stack()
    # s1.push(1)
    # s1.push("Shukla")
    # s1.push("Priyansh")
    # s1.push(23)
    # s1.print()
    print(reverse_string("Hello Priyansh Shukla"))
