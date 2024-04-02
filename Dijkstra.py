import sys
from main import printLine
import time



class Dijkstra:
    def __init__(self):
        self.SPT = []
        self.visited = []
        self.cost = []

    def runAlgorithm(self, graph, V, start_node, goal_node):
        start_time = time.time()
        self.SPT = []
        self.visited = []
        self.cost = []
        node = start_node

        for i in range(V):
            self.cost.append([sys.maxsize, -1])

        self.cost[node] = [0, -1]
        while len(self.visited) != V and node != goal_node:
            self.visited.append(node)
            for j in range(V):
                if (graph[node][j] != 0) and (j not in self.visited) and (self.cost[node][0] + graph[node][j] < self.cost[j][0]):
                    self.cost[j][0] = self.cost[node][0] + graph[node][j]
                    self.cost[j][1] = node

            next_min = [0, sys.maxsize]
            for j in range(len(self.cost)):
                if (self.cost[j][0] < next_min[1]) and (j not in self.visited):
                    next_min = [j, self.cost[j][0]]

            node = next_min[0]
        self.visited.append(node)
        path = self.reconstruct_path(start_node, goal_node)
        if path is None:
            print("No path found from node", start_node, "to node", goal_node)
        else:
            print("Shortest path from node", start_node, "to node", goal_node, "is:", path)
                
        

        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return path

    def reconstruct_path(self, start_node, goal_node):
        path = []
        current_node = goal_node
        while current_node != start_node:
            path.append([self.cost[current_node][1], current_node])
            current_node = self.cost[current_node][1]
        path.reverse()
        return path
    
    def print_path(self, path):
        print("Shortest path from start to goal:")
        for node in path:
            print(node, end=' ')
        print()

    def printVisitedNodes(self):
        print("Visited nodes (Dijkstra):", self.visited)

    def printAlgo(self, start_node, goal_node):
    # Print the total cost from start to goal
        total_cost = self.cost[goal_node][0]
        if total_cost == sys.maxsize:
            print("No reachable path from node", start_node, "to node", goal_node)
        else:
            print("Total cost from node", start_node, "to node", goal_node, "is:", total_cost)

    def costSum(self):
        sum = 0
        for i in self.cost:
            sum += i[0]
        printLine()
        print("Total Cost: ", sum)