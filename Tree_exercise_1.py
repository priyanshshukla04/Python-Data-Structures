class Global_Tree:
    def __init__(self, country):
        self.country = country
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

    # def print_tree(self):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + "----->"
    #     print(prefix+self.country)
    #     if self.children:
    #         for i in self.children:
    #             i.print_tree()

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "----->"
        print(prefix+self.country)
        if self.children:
            for i in self.children:
                i.print_tree(level)


def build_tree():
    # 1
    Global = Global_Tree("Global")

    # 2
    India = Global_Tree("India")

    Gujarat = Global_Tree("Gujarat")
    Gujarat.add_child(Global_Tree("Ahmedabad"))
    Gujarat.add_child(Global_Tree("Baroda"))

    Karnataka = Global_Tree("Karnataka")
    Karnataka.add_child(Global_Tree("Bengaluru"))
    Karnataka.add_child(Global_Tree("Mysore"))

    India.add_child(Gujarat)
    India.add_child(Karnataka)

    # 3
    USA = Global_Tree("USA")

    New_Jersey = Global_Tree("New_Jersey")
    New_Jersey.add_child(Global_Tree("Princeton"))
    New_Jersey.add_child(Global_Tree("Trenton"))

    California = Global_Tree("California")
    California.add_child(Global_Tree("San Fransisco"))
    California.add_child(Global_Tree("Mountain View"))
    California.add_child(Global_Tree("Palo Alto"))

    USA.add_child(New_Jersey)
    USA.add_child(California)

    # 4
    Global.add_child(India)
    Global.add_child(USA)

    # Global.print_tree(1)
    # Global.print_tree(2)
    Global.print_tree(3)


if __name__ == '__main__':
    build_tree()
