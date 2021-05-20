class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_child(self, child):
        if self.data == child:
            return
        elif self.data > child:
            if self.left_child:
                self.left_child.add_child(child)
            else:
                self.left_child = BinaryTree(child)
        else:
            if self.right_child:
                self.right_child.add_child(child)
            else:
                self.right_child = BinaryTree(child)

    def search_element(self, element):
        if self.data == element:
            return True
        elif element < self.data:
            if self.left_child:
                return self.left_child.search_element(element)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.search_element(element)
            else:
                return False

    def in_order_traversal(self):
        element = []
        if self.left_child:
            element += self.left_child.in_order_traversal()

        element.append(self.data)

        if self.right_child:
            element += self.right_child.in_order_traversal()

        return element

    def min_element(self):
        if self.left_child is None:
            return self.data
        return self.left_child.min_element()

    def max_element(self):
        if self.right_child is None:
            return self.data
        return self.right_child.max_element()

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left_child:
            elements += self.left_child.pre_order_traversal()
        if self.right_child:
            elements += self.right_child.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left_child:
            elements += self.left_child.post_order_traversal()
        if self.right_child:
            elements += self.right_child.post_order_traversal()
        elements.append(self.data)

        return elements

    def sum_elements(self):
        left_sum = self.left_child.sum_elements() if self.left_child else 0
        right_sum = self.right_child.sum_elements() if self.right_child else 0
        return self.data + left_sum + right_sum

    def delete_element(self, element):
        if element < self.data:
            if self.left_child:
                self.left_child = self.left_child.delete_element(element)
        elif element > self.data:
            if self.right_child:
                self.right_child = self.right_child.delete_element(element)
        else:
            if self.left_child is None and self.right_child is None:
                return None
            elif self.left_child == None:
                return self.right_child
            elif self.right_child == None:
                return self.left_child

            min_val = self.right_child.min_element()
            self.data = min_val
            self.right_child = self.right_child.delete_element(min_val)

        return self


def build_tree(elements1):
    root_node = BinaryTree(elements1[0])

    for i in range(1, len(elements1)):
        root_node.add_child(elements1[i])

    return root_node


if __name__ == '__main__':
    elements = [1, 3, 5, 2, 8, 13, 5, 66, 90, 100]
    main = build_tree(elements)

    print(main.search_element(13))
    # print(main.search_element(130))
    print(main.in_order_traversal())
    # print(main.min_element())
    # print(main.max_element())
    print(main.pre_order_traversal())
    print(main.post_order_traversal())
    print(main.sum_elements())
    main.delete_element(13)
    print("After deleting 13 ", main.in_order_traversal())
