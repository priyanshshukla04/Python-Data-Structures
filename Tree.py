class Normal_Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        count = 0
        current_level = self.parent
        while current_level:
            count += 1
            current_level = current_level.parent
        return count

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "->"
        print(prefix + self.data)
        if self.children:
            for i in self.children:
                i.print_tree()


def operations():
    root_node = Normal_Tree("Animals")

    carnivores = Normal_Tree("Carnivores")
    carnivores.add_child(Normal_Tree("Lion"))
    carnivores.add_child(Normal_Tree("Tiger"))
    carnivores.add_child(Normal_Tree("Crocodile"))

    omnivores = Normal_Tree("Omnivores")
    omnivores.add_child(Normal_Tree("Dog"))
    omnivores.add_child(Normal_Tree("cat"))

    herbivores = Normal_Tree("Herbivores")
    herbivores.add_child(Normal_Tree("Cow"))
    herbivores.add_child(Normal_Tree("Horse"))
    herbivores.add_child(Normal_Tree("Goat"))

    root_node.add_child(carnivores)
    root_node.add_child(omnivores)
    root_node.add_child(herbivores)

    root_node.print_tree()
    # herbivores.print_tree()


if __name__ == '__main__':
    operations()
