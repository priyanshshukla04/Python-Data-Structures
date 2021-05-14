class Management_Tree:
    def __init__(self, name, position):
        self.name = name
        self.position = position
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

    def print_tree(self, var):
        if var == "name":
            value = self.name
        elif var == "position":
            value = self.position
        else:
            value = self.name + " (" + self.position + ")"

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "->"
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(var)


def operations():
    name1, position1 = input("Enter the name and his position: ").split(" ")
    ceo = Management_Tree(name1, position1)

    name2, position2 = input("Enter the name and his position: ").split(" ")
    cto = Management_Tree(name2, position2)
    Vishwa = Management_Tree("Vishwa", "Infrastructure")
    Aamir = Management_Tree("Aamir", "Application head")
    Vishwa.add_child(Management_Tree("Dhaval", "Cloud Management"))
    Vishwa.add_child(Management_Tree("Abhijit", "App Management"))
    cto.add_child(Vishwa)
    cto.add_child(Aamir)

    name3, position3 = input("Enter the name and his position: ").split(" ")
    hr_head = Management_Tree(name3, position3)
    hr_head.add_child(Management_Tree("Peter", "Recruitment manager"))
    hr_head.add_child(Management_Tree("Waqas", "Policy manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    ceo.print_tree("name")
    # ceo.print_tree("position")
    # ceo.print_tree("both")


if __name__ == '__main__':
    operations()
