# Code made by:
#  - Marco Antonio de Camargo, RA: 10418309
#  - Natan Moreira Passos, RA: 10417916
#  - Nicolas Henriques de Almeida, RA: 10418357

# This file contains utility functions for fetching and processing game data from the RAWG API.

# File history:
# - 2025-09-27: Created the file and added the initial code.

import os
import requests
from itertools import combinations

API_KEY = os.getenv("RAWG_API_KEY")
BASE_URL = "https://api.rawg.io/api/games"

def fetch_games(total_pages=2):
    games = []
    for page in range(1, total_pages + 1):
        url = f"{BASE_URL}?key={API_KEY}&page={page}"
        response = requests.get(url)
        data = response.json()
        for game in data["results"]:
            games.append({
                "id": game["id"],
                "name": game["name"],
                "tags": [tag["name"] for tag in game.get("tags", [])]
            })
    return games

def generate_edges(games):
    edges = []
    for (index1, game1), (index2, game2) in combinations(enumerate(games), 2):
        common_tags = set(game1["tags"]) & set(game2["tags"])
        if common_tags:
            weight = len(common_tags)
            edges.append((index1, index2, weight))
    return edges

def save_graph_to_file(games, edges, filename="grafo.txt"):
    graph_type = 2
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"{graph_type}\n")
        file.write(f"{len(games)}\n")
        for index, game in enumerate(games):
            file.write(f'{index} "{game["name"]}"\n')
        file.write(f"{len(edges)}\n")
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
    print(f"Graph saved to {filename}")

if __name__ == "__main__":
    games = fetch_games(4)
    edges = generate_edges(games)
    save_graph_to_file(games, edges)
