# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file contains the implementation of a graph using an adjacency matrix.

# File history:
# - 2025-09-27: Created the file and added the initial code.

class MatrixGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = 0
        self.adjacency_matrix = [[None for i in range(nodes)] for j in range(nodes)]

    def show(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for j in range(self.nodes):
                print(f"Adj[{i:2d},{j:2d}] =", self.adjacency_matrix[i][j], "", end="")
            print("\n")
    
    def show_min(self):
        print(f"\n n: {self.nodes:2d} ", end="")
        print(f"m: {self.edges:2d}\n")
        for i in range(self.nodes):
            for w in range(self.nodes):
                print("", self.adjacency_matrix[i][w], "", end="") 
            print("\n")

    def remove_node(self, node):
        if (node > self.nodes):
            print("Invalid node!")
            return
        
        removed_edges = sum(self.adjacency_matrix[node])
        removed_edges += sum(row[node] for row in self.adjacency_matrix)

        self.adjacency_matrix.pop(node)
        for row in self.adjacency_matrix:
            row.pop(node)

        self.nodes -= 1
        self.edges -= removed_edges
