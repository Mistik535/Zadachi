graph = {}

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

# node = find_lowest_cost_node(costs)
# while node is not None: #Если обработаны все узлы, цикл while завершен
#  cost = costs[node]
#  neighbors = graph[node]
#  for n in neighbors.keys(): #Перебрать всех соседей текущего узла
#  new_cost = cost + neighbors[n]
#  if costs[n] > new_cost:
#  costs[n] = new_cost #…обновить стоимость для этого узла
#  parents[n] = node #Этот узел становится новым родителем для соседа
#  processed.append(node) #Узел помечается как обработанный
#  node = find_lowest_cost_node(costs)


nodes = {}
nodes["a"] = 6  # begin point
nodes["b"] = 2
nodes["c"] = 20
nodes["fin"] = float("inf")  # end point

def find_lowest_cost_node(nodes):
    nodes_list = {}  # list
    lowest_cost = float("inf")  # point end
    lowest_cost_node = None  # save node

    for node in nodes:
        cost = nodes[node]  # 6
        print("> key:", node, " - data:", nodes[node])  # "a" - 6

        if cost < lowest_cost and node not in nodes_list:
            print("processed", nodes_list)
            lowest_cost = cost
            print("lowest_cost", lowest_cost)
            lowest_cost_node = node

    return lowest_cost_node

find_lowest_cost_node(nodes)
