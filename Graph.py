class Graph:
    def __init__(self, cities):
        self.cities = cities
        # print(self.cities)
        self.cities_dict = {}
        for key, value in cities:
            if key in self.cities_dict:
                self.cities_dict[key].append(value)
            else:
                self.cities_dict[key] = [value]
        # print(self.cities_dict)

    def know_path(self, source_city, destination, path_list=[]):
        path_list = path_list + [source_city]
        if source_city == destination:
            return [path_list]

        if source_city not in self.cities_dict:
            return []

        final_path_list = []
        for node in self.cities_dict[source_city]:
            if node not in path_list:
                possible_path = self.know_path(node, destination, path_list)
                for i in possible_path:
                    final_path_list.append(i)

        return final_path_list

    def shortest_path(self, source_city, destination, path_list=[]):
        path_list = path_list + [source_city]
        if source_city == destination:
            return path_list

        if source_city not in self.cities_dict:
            return None

        shortest = None
        for node in self.cities_dict[source_city]:
            if node not in path_list:
                sp = self.shortest_path(node, destination, path_list)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp

        return shortest


if __name__ == '__main__':
    cities_tuple_list = [
        ("Delhi", "Mumbai"),
        ("Delhi", "Chennai"),
        ("Delhi", "Ahmedabad"),
        ("Mumbai", "Kochi"),
        ("Chennai", "Bangalore"),
        ("Ahmedabad", "Bangalore"),
        ("Kochi", "Bangalore"),
    ]

    graph_node = Graph(cities_tuple_list)
    print("possible paths:\n",graph_node.know_path("Delhi", "Bangalore"))
    print("Shortest path:\n",graph_node.shortest_path("Delhi", "Bangalore"))
