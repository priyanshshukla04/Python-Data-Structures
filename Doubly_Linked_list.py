class Node:
    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous


class Doubly_Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            new_node = Node(data, self.head, None)
            self.head = new_node
        else:
            new_node = Node(data, self.head, None)
            self.head.previous = new_node
            self.head = new_node

    def insert_at_end(self, data):
        if self.head == None:
            new_node = Node(data, self.head, None)
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data, None, temp)
            temp.next = new_node

    def insert_new_iterable_list(self, iterable):
        self.head = None
        for i in iterable:
            self.insert_at_end(i)

    def length_doubly_list(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def remove_element_at_index(self, index):
        if index < 0 or index > self.length_doubly_list():
            raise Exception("Invalid Index given")
        elif index == 0:
            self.head = self.head.next
        elif self.head == None:
            print("List is already empty")
        else:
            count = 0
            temp = self.head
            while temp.next:
                count += 1
                if count == index:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def insert_element_at_index(self, index, data):
        if index < 0 or index > self.length_doubly_list():
            raise Exception("Invalid Index given")
        elif index == 0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            temp = self.head
            while temp.next:
                count += 1
                if count == index:
                    new_node = Node(data, temp.next, self.head)
                    temp.next = new_node
                    temp = temp.next
                    temp.next.previous = temp
                    break
                temp = temp.next

    def insert_after_value_given(self, value, data):
        temp = self.head
        count = 0
        while temp:
            if temp.data == value:
                new_node = Node(data, temp.next, temp)
                temp.next = new_node
                temp = temp.next
                temp.next.previous = temp
                break
            if count == self.length_doubly_list():
                print("Value given does not match")
            else:
                temp = temp.next
            count += 1

    def remove_element_by_value(self, value):
        if self.head == None:
            print("List is empty")
        elif self.head == value:
            self.head = self.head.next
        else:
            temp = self.head
            count = 0
            while count < self.length_doubly_list():
                if temp.next.data == value:
                    temp.next = temp.next.next
                    temp.next.previous = temp
                    break
                temp = temp.next
                count += 1

    def print_forward(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        strdll = ''
        while temp:
            strdll += str(temp.data) + ' --> '
            temp = temp.next
        print(strdll)

    def get_last_node(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            # print(temp.data)
            return temp

    def print_backward(self):
        if self.head == None:
            print("List is empty")
            return
        last_node = self.get_last_node()
        temp = last_node
        strdll = ''
        while temp:
            strdll += str(temp.data) + ' --> '
            temp = temp.previous
        print(strdll)


if __name__ == '__main__':
    dl1 = Doubly_Linked_list()
    # dl1.insert_at_beginning(12)
    # dl1.insert_at_beginning(15)
    # dl1.insert_at_beginning(2)
    # dl1.insert_at_beginning(20)
    # dl1.print_forward()

    # dl1.insert_at_end(200)
    # dl1.insert_at_end(300)
    # dl1.insert_at_end(250)
    # dl1.print_forward()

    dl1.insert_new_iterable_list([1,5,16,4,8,10])
    # dl1.print_forward()

    # print(dl1.length_doubly_list())

    # dl1.remove_element_at_index(3)
    # dl1.print_forward()

    dl1.insert_element_at_index(3,90)
    dl1.print_forward()

    dl1.insert_after_value_given(90,56)
    dl1.print_forward()

    dl1.remove_element_by_value(4)
    dl1.print_forward()

    dl1.get_last_node()
    # dl1.print_forward()

    dl1.print_backward()

