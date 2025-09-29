# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file is the main file of the project. It is responsible for running the program.

# File history:
# - 2025-09-27: Created the file and added the initial code.

from src.utils import utils
from src.models.matrix_graph.labeled_undirected_matrix_graph import LabeledUndirectedMatrixGraph


graph = LabeledUndirectedMatrixGraph()

def print_menu():
        print("============== MENU ==============")
        print("1. Read data from grafo.txt")
        print("2. Write data to grafo.txt")
        print("3. Insert vertex")
        print("4. Insert edge")
        print("5. Remove vertex")
        print("6. Remove edge")
        print("7. Show file content")
        print("8. Show graph")
        print("9. Show graph connectivity")
        print("10. Exit")
        print("==================================")

def handle_menu_option(option):
    global graph

    try: 
        if option == 1: # 1. Read data from grafo.txt
            graph = graph.graph_from_file("grafo.txt")
            print("Graph loaded from grafo.txt")

        elif option == 2: # 2. Write data to grafo.txt
            graph.graph_to_file("grafo.txt")
            print("Generated grafo.txt")

        elif option == 3: # 3. Insert vertex
            label = input("Enter the label for the new vertex: ")
            graph.insert_node(label)
            print(f"Vertex '{label}' inserted.")

        elif option == 4: # 4. Insert edge
            origin = int(input("Enter the origin vertex index: "))
            destiny = int(input("Enter the destiny vertex index: "))
            label = input("Enter the label for the new edge: ")
            graph.insert_edge(origin, destiny, label)
            print(f"Edge from vertex {origin} to vertex {destiny} with label '{label}' inserted.")

        elif option == 5: # 5. Remove vertex
            node = int(input("Enter the vertex index to remove: "))
            graph.remove_node(node)
            print(f"Vertex {node} removed.")

        elif option == 6: # 6. Remove edge
            origin = int(input("Enter the origin vertex index: "))
            destiny = int(input("Enter the destiny vertex index: "))
            graph.remove_edge(origin, destiny)
            print(f"Edge from vertex {origin} to vertex {destiny} removed.")

        elif option == 7: # 7. Show file content
            utils.show_file_content("grafo.txt")

        elif option == 8: # 8. Show graph
            graph.show()

        elif option == 9: # 9. Show graph connectivity
            connectivity = graph.connectivity()
            print("Connected") if connectivity else print("Not Connected")

        elif option == 10: # 10. Exit
            print("Exiting the program.")

        else:
            print("Invalid option. Please try again.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu_option = 0
    while(menu_option != 10):
        print_menu()
        menu_option = int(input("Option: "))
        handle_menu_option(menu_option)

    