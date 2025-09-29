# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file contains the implementation of a labeled directed graph using an adjacency matrix.
# It extends the MatrixGraph class to include labels on edges.

# File history:
# - 2025-09-27: Created the file and added the initial code.

import os
from src.models.matrix_graph.matrix_graph import MatrixGraph 

class LabeledUndirectedMatrixGraph(MatrixGraph):
    def __init__(self, nodes = 0):
        super().__init__(nodes)
        self.adjacency_matrix = [[float('inf') for i in range(nodes)] for j in range(nodes)]
        self.node_labels = [None for i in range(nodes)]

    def insert_node(self, label):
        self.nodes += 1
        for row in self.adjacency_matrix:
            row.append(float('inf'))
        self.adjacency_matrix.append([float('inf') for i in range(self.nodes)])
        self.node_labels.append(label)

    def remove_node(self, node):
        if (node >= self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = sum(1 for weight in self.adjacency_matrix[node] if weight != float('inf'))
        removed_edges += sum(1 for row in self.adjacency_matrix if row[node] != float('inf'))

        self.adjacency_matrix.pop(node)
        for row in self.adjacency_matrix:
            row.pop(node)

        self.node_labels.pop(node)

        self.nodes -= 1
        self.edges -= removed_edges // 2

    def insert_edge(self, origin_node, destiny_node, label):
        if origin_node >= self.nodes or destiny_node >= self.nodes:
            raise ValueError("Invalid node index")

        if self.adjacency_matrix[origin_node][destiny_node] == float('inf'):
            self.adjacency_matrix[origin_node][destiny_node] = label
            self.adjacency_matrix[destiny_node][origin_node] = label
            self.edges += 1
    
    def remove_edge(self, origin_node, destiny_node):
        if origin_node >= self.nodes or destiny_node >= self.nodes:
            raise ValueError("Invalid node index")

        if self.adjacency_matrix[origin_node][destiny_node] != float('inf'):
            self.adjacency_matrix[origin_node][destiny_node] = float('inf')
            self.adjacency_matrix[destiny_node][origin_node] = float('inf')
            self.edges -= 1

    def graph_from_file(self, filename):
        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, "..", "..", "resources", filename)
        full_path = os.path.abspath(full_path)

        with open(full_path, "r") as file:
            file.readline()
            nodes = int(file.readline())
            if nodes == 0:
                return self
            
            self.__init__(nodes)

            for i in range(nodes):
                label = file.readline().strip().split('"')
                self.node_labels[i] = label[1]

            edges = int(file.readline())
            if edges == 0:
                self.nodes = nodes
                return self
            
            if edges > nodes ** 2:
                print("Invalid edges quantity")
                return None
            
            for _ in range(edges):
                origin, destiny, label = file.readline().strip().split()
                print(f"Read edge: {origin} - {destiny} with label '{label}'")
                origin = int(origin)
                destiny = int(destiny)
                label = str(label)
                self.insert_edge(origin, destiny, label)
        return self
    
    def graph_to_file(self, filename):
        with open(filename, "w") as f:
            f.write("2\n")
            f.write(f"{self.nodes}\n")
            for i in range(self.nodes): 
                f.write(f'{i} "{self.node_labels[i]}"\n')
            f.write(f"{self.edges}\n")
            for row in range(len(self.adjacency_matrix)):
                for column in range(row, len(self.adjacency_matrix[i])):
                    if(self.adjacency_matrix[row][column] != float('inf')):
                        f.write(f"{row} {column} {self.adjacency_matrix[row][column]}\n")
        print("Gerado grafo.txt")



    def show(self):
        print(f"\n Nodes: {self.nodes:2d} ")
        for i in range(self.nodes):
            print(f"Label[{i}] =", self.node_labels[i], "")
        print(f"\nEdges: {self.edges:2d}\n")
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(f"Adj[{i:2d},{j:2d}] =", self.adjacency_matrix[i][j], "", end="")
            print("\n")

    def show_min(self):
        print(f"\n Nodes: {self.nodes:2d} ")
        for i in range(self.nodes):
            print(f"Label[{i}] =", self.node_labels[i], "")
        print(f"\nEdges: {self.edges:2d}\n")
        for i in range(self.nodes):
            for w in range(self.nodes):
                print("", self.adjacency_matrix[i][w], "", end="") 
            print("\n")

    def dijkstra(self, origin_node):
        distances = [float('inf')] * self.nodes
        distances[origin_node] = 0

        routes = [-1] * self.nodes
        
        open_nodes = list(range(self.nodes))
        closed_nodes = []

        selected_node = origin_node

        while(len(open_nodes) != 0):
            open_nodes.remove(selected_node)
            closed_nodes.append(selected_node)

            for i in range(self.nodes):
                if i not in closed_nodes:
                    route = distances[selected_node] + self.adjacency_matrix[selected_node][i]
                    if route < distances[i]:
                        distances[i] = route
                        routes[i] = selected_node

            min_distance = float('inf')
            for node in open_nodes:
                if distances[node] < min_distance:
                    selected_node = node
        
        return distances, routes

    def connectivity(self):
        marked = [False] * self.nodes
        marked[0] = True
        for i in range(len(self.adjacency_matrix)):
            for j in range(i, len(self.adjacency_matrix)):
                if(self.adjacency_matrix[i][j] != float('inf')):
                    if(marked[j] == False):
                        marked[j] = True
        for i in range(len(marked)):
            if(marked[i] == False):
                return False
        return True
