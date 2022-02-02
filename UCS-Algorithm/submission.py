import csv
from queue import PriorityQueue


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


# reads data into an appropriate data structure.
def build_graph(path):
    graph = {}
    with open(data_path, "r", encoding='UTF-8') as file:
        data = csv.reader(file)
        next(data)
        for p in data:
            if p[0] in graph:
                graph[p[0]].append((int(p[2]), p[1]))
            else:
                graph[p[0]] = [(int(p[2]), p[1])]
            if p[1] in graph:
                graph[p[1]].append((int(p[2]), p[0]))
            else:
                graph[p[1]] = [(int(p[2]), p[0])]
    return graph


# performs uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    prio = PriorityQueue()
    prio.put((0, start))
    if prio.empty():
        raise CityNotFoundError(city=start)
    explored = set()

    def check_prio():
        temp1 = PriorityQueue()
        a = []
        while not prio.empty():
            x = prio.get()
            a.append(x[1])
            temp1.put(x)
        while not temp1.empty():
            prio.put(temp1.get())
        return a

    def add_path(current1):
        if len(current1) > 2:
            return current1[2] + " " + current1[1]
        else:
            return current1[1]

    while not prio.empty():
        current = prio.get()
        explored.add(current)
        if current[1] == end:
            return current
        for neighbor in graph[current[1]]:
            if neighbor[1] not in [x[1] for x in explored] + check_prio():
                prio.put((neighbor[0] + current[0], neighbor[1], add_path(current)))
            elif neighbor[1] in check_prio():
                temp = PriorityQueue()
                while not temp.empty():
                    x = prio.get()
                    if x[1] == neighbor[1] and neighbor[0] + current[0] < x[0]:
                        x[0] = neighbor[0] + current[0]
                    explored.add(x)
                while not temp.empty():
                    prio.put(temp.get())
    raise CityNotFoundError(city=end)


# main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    data_path = input("please enter file path: ")
    try:
        graph = build_graph(path=data_path)
        start = input("please enter current city: ")
        end = input("please enter target city: ")
        try:
            result = (uniform_cost_search(graph=graph, start=start, end=end))
            print(f"distance: {result[0]}\npath:{result[2] + ' ' + result[1]}")
        except CityNotFoundError:
            print("City Not Found!")
    except FileNotFoundError:
        print("File Not Found!")
