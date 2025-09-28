# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file contains utility functions for the project.

# File history:
# - 2025-09-27: Created the file and added the initial code.

def show_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
