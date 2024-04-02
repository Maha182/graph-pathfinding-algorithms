import sys
from main import printLine
import time

class Floyd:
    SPT = []
    cost = []
    last = []

    def runAlgorithm(self, graph, V, start, goal):
        start_time = time.time()
        self.SPT = []
        self.cost = [[sys.maxsize for _ in range(V)] for _ in range(V)]
        self.last = [[-1 for _ in range(V)] for _ in range(V)]

        # Initialize the cost and last matrices
        for i in range(V):
            for j in range(V):
                if i == j:
                    self.cost[i][j] = 0
                elif graph[i][j] != 0:
                    self.cost[i][j] = graph[i][j]
                    self.last[i][j] = i  # Store the predecessor

        # Floyd-Warshall algorithm to calculate shortest paths
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if self.cost[i][k] + self.cost[k][j] < self.cost[i][j]:
                        self.cost[i][j] = self.cost[i][k] + self.cost[k][j]
                        self.last[i][j] = self.last[k][j]

        # Reconstruct the shortest path from start to goal
        if self.cost[start][goal] == sys.maxsize:
            print("No path from", start, "to", goal)
            return []
        path = self.reconstructPath(start, goal)

        if path is None:
            print("No path found from node", start, "to node", goal)
        else:
            print("Shortest path from node", start, "to node", goal, "is:", path)
        
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return path

    def reconstructPath(self, start, goal):
        path = []
        at = goal
        # Reconstruct the path backwards from goal to start
        while at != start:
            if at == -1:
                return []  # No path exists
            path.append(at)
            at = self.last[start][at]
        path.append(start)
        path.reverse()

        # Convert the path to the required edge pair format
        edgePairs = [[path[i], path[i + 1]] for i in range(len(path) - 1)]
        return edgePairs


    def printAlgo(self, node):
        printLine()
        print("Cost from Starting Node:")
        for i in range(len(self.cost)):
            print("(", node, "->", i, ") :\t", self.cost[node][i])

    def costSum(self, V, node):
        sum = 0
        for i in range(V):
            sum += self.cost[node][i]
        printLine()
        print("Total Cost: ", sum)

    def printVisitedNodes(self, start, goal):
        # This function prints intermediary nodes for a specific start-goal path.
        path = self.reconstructPath(start, goal)
        if not path:
            print("No path from", start, "to", goal)
            return
        visited = {node for pair in path for node in pair}
        print("Visited nodes (Floyd, from {} to {}):".format(start, goal), sorted(visited))