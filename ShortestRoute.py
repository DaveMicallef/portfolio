
#Network of seven nodes
graph = {
    'a':{'b':3, 'c':4, 'd':7},
    'b':{'c':1, 'f':5},
    'c':{'d':2,'f':6},
    'd':{'e':3,'g':6},
    'e':{'f':1,'g':3,'h':4},
    'f':{'h':8},
    'g':{'h':2},
    'h':{'g':2}
    }


def shortestPath(graph, start, goal):
    shortest_distance = {}#records the cost to reach a given node. Will be updated as we move along the graph 
    track_predecessor = {}#keep track of nodes that were visited (and therefore the path that was being created)
    unseenNodes = graph #iterate through entire graph 
    infinity = 999999999999 #must be significantly larger than cumulitave cost
    track_path = [] #trace journey back to source node - the optimal route 

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance [node] < shortest_distance[min_distance_node]:
                min_distance_node = node 

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor [child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("path is not reachable")
            break

    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("Shortest distance is: " + str(shortest_distance[goal]))
        print("Optimal path is: " + str(track_path))



shortestPath(graph,'a','h')
