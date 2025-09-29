# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file contains utility functions for the project.

# File history:
# - 2025-09-27: Created the file and added the initial code.

import os

def show_file_content(filename):
    try:
        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, "..", "resources", filename)
        full_path = os.path.abspath(full_path)

        print(f"Reading file from: {full_path}")
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
