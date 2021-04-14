from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def readFile(name):
    
    items = []
    file = open(name)
    print(file.name)
    line = file.readline()
    
    first_line = line.split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])
    
    for i in range(1, item_count + 1):
        line = file.readline()
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))
    
    file.close()    
    return items, capacity

def taken_items (items, taken):
    
    def get_taken_list(taken):
        result = []
        for j in range(0, len(taken)):
            if taken[j]: result.append(j)
        return result

    items.sort(key=lambda x: getattr(x, 'index'), reverse=False)
    return get_taken_list(taken)

def total_weight(items, taken):
    weight = 0
    for item in items:
        if taken[item.index]== 1:
            weight += item.weight
    return weight

def check_solution(capacity, items, taken):
    weight = 0
    value = 0
    for item in items:
        if taken[item.index]== 1:
            weight += item.weight
            value += item.value
    if weight> capacity:
        print("solución incorrecta, se supera la capacidad de la mochila (capacity, weight):", capacity, weight)
        return 0
    return value
            
def help():
    print("usage: practica2.py [-h] [-d [DIRECTORY]] [-f [FILE]] [-b] [-r] [-t] [-dt]" + "\n")
    print("optional arguments: ")
    print("  -h, --help             show this help message and exit" + "\n" +
                           "  -d [DIRECTORY], --directory [DIRECTORY]" + "\n" + 
                           "                        directory (process many files)" + "\n" +
                           "  -f [FILE], --file [FILE] " + "\n" +
                           "                        file (process a single file)" + "\n" +
                           "  -b, --benefit         Display benefit" + "\n" +
                           "  -r, --room            Display room (unused knapsack weigth)" + "\n" +
                           "  -t, --time            Display time" + "\n" +
                           "  -dt, --display_taken  Display identifer of taken items" + "\n" +
                           "  -sg, --greedy         Solve it with Greedy" + "\n" +
                           "  -sm, --memoization    Solve it with Memoization" + "\n" +
                           "  -st, --tabulation     Solve it with Tabulation" + "\n")
    