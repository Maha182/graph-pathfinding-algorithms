import sys
from main import printLine

class BellmanFord:
    SPT = []
    distance = []
    prev = []

    def runAlgorithm(self, graph, V, start, goal):
        self.SPT = []
        self.distance = [sys.maxsize] * V
        self.prev = [None] * V
        self.distance[start] = 0

        for _ in range(V - 1):
            for i in range(V):
                for j in range(V):
                    if graph[i][j] != 0:
                        tempDistance = self.distance[i] + graph[i][j]
                        if tempDistance < self.distance[j]:
                            self.distance[j] = tempDistance
                            self.prev[j] = i

        # Check for negative weight cycles
        for i in range(V):
            for j in range(V):
                if graph[i][j] != 0 and self.distance[i] + graph[i][j] < self.distance[j]:
                    print("Graph contains a negative weight cycle")
                    return None

        # Reconstruct path from start to goal in the edge pair format
        path = self.reconstructPath(start, goal)
        if path is None:
            print("No path found from node", start, "to node", goal)
        else:
            print("Shortest path from node", start, "to node", goal, "is:", path)
        return path

    def reconstructPath(self, start, goal):
        path = []
        at = goal
        while at != start:
            if at is None:
                return None
            prev_node = self.prev[at]
            if prev_node is not None:
                path.append([prev_node, at])
            at = prev_node
        path.reverse()
        return path


    def printAlgo(self, node):
        printLine()
        print("Cost from Starting Node:")
        for i in range(len(self.distance)):
            print("(", node, "->", i, ") :\t", self.distance[i])

    def costSum(self):
        sum = 0
        for i in self.distance:
            sum += i
        printLine()
        print("Total Cost: ", sum)

    def printVisitedNodes(self):
        visited = set(self.prev) - {None}
        print("Visited nodes (Bellman-Ford):", sorted(visited))