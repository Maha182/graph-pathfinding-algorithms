import sys
from main import printLine


class Dijkstra:
    def __init__(self):
        self.SPT = []
        self.visited = []
        self.cost = []

    def runAlgorithm(self, graph, V, start_node, goal_node):
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
        return self.reconstruct_path(start_node, goal_node)

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