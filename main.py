from queue import PriorityQueue
import math
import random
import time

filename1 = "graph_v2.txt"
filename2 = "vertices_v1.txt"


class Path:
    def __init__(self, start, end, highway, cost):
        self.start = start
        self.end = end
        self.highway = highway
        self.cost = cost

class City:
    def __init__(self, name, lat, long):
        self.name = name
        self.connections = {}
        self.lat = lat
        self.long = long
        self.connections_count = len(self.connections)

    def distance_to(self, other_city):
        if other_city.strip().upper() in self.connections:
            for path in self.connections.values():
                if path.end == other_city.strip().upper():
                    return path.cost
        else:
            raise IndexError(f"Path does not exist between {self.name} and {other_city}.")

def on_start():
    print("Welcome to Oregon Pathfinder!\n")
    while True:
        startcity = input("Enter your starting city: ").upper().strip()
        if startcity not in cities:
            print("City not found in database. Please try again.")
            continue
        destinationcity = input("Enter your destination city: ").upper().strip()
        if destinationcity not in cities:
            print("City not found in database. Please try again.")
            continue

        algorithm = input("Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): ").strip().lower()
        start_time = time.time()
        if algorithm in ['astar', 'a']:
            print(f"Calculating route from {startcity} to {destinationcity} using A* Search algorithm...")
            print(" ")
            astar(startcity, destinationcity)
        elif algorithm in ['dijkstra', 'd']:
            print(f"Calculating route from {startcity} to {destinationcity} using Dijkstra's algorithm...")
            dijkstra(startcity, destinationcity)
            print(" ")
        elif algorithm in ['greedy', 'g']:
            print(f"Calculating route from {startcity} to {destinationcity} using Greedy Best-First Search algorithm...")
            greedy_best_first(startcity, destinationcity)
            print(" ")
        else:
            print("Invalid algorithm choice. Please try again.")
            continue
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds\n")

        again = input("Would you like to try another route? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using Oregon Pathfinder! Safe travels!")
            break

def load_paths(filename1, filename2):
    cities = {}
    paths = []
    with open(filename2, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            city = parts[0].strip().upper()
            lat = float(parts[1])
            long = float(parts[2])
            cities[city] = City(city, lat, long)
    with open(filename1, 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            city = parts[0].strip().upper()
            connection = parts[1].strip().upper()
            highway = parts[2].strip()
            cost = int(parts[3])
            paths.append(Path(city, connection, highway, cost))
            if city in cities:
                cities[city].connections[connection] = Path(city, connection, highway, cost)
    for city in cities.values():
        city.connections_count = len(city.connections)
    return cities, paths

def path_to_string(path):
    result = ""
    citiesexplored = 0
    pathtracker = 1
    totaldistance = 0
    for p in path:
        citiesexplored += 1
        if pathtracker < (len(path) - 1):
            if p in cities:
                totaldistance += cities[p].distance_to(path[pathtracker])
        result += f"{p} -> "
        pathtracker += 1
    return result[:-4] + f"\nCities explored: {citiesexplored}\nTotal distance: {totaldistance} miles"

def astar(start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    came_from = {start: None}
    gvalues = {start: 0}
    while not frontier.empty():
        current = frontier.get()[1]
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            pathstr = path_to_string(path)
            print(f"Path found: {pathstr}")
            print(f"Vertices explored: {len(explored)}")
            return True
        explored.add(current)
        for path in cities[current].connections.values():
            tentative_g = gvalues[current] + path.cost
            if path.end not in gvalues or tentative_g < gvalues[path.end]:
                gvalues[path.end] = tentative_g
                fvalue = gvalues[path.end] + heuristic(cities[path.end], cities[goal])
                frontier.put((fvalue, path.end))
                came_from[path.end] = current


def greedy_best_first(start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic(cities[start], cities[goal]), start))
    explored = set()
    mypath = [start]
    while not frontier.empty():
        current = frontier.get()[1]
        if current == goal:
            pathstr = path_to_string(mypath)
            print(f"Path found: {pathstr}")
            print(f"Vertices explored: {len(explored)}")
            return True
        hvalues = {}
        for path in cities[current].connections.values():
            if path.end not in explored:
                hvalues[path.end] = heuristic(cities[path.end], cities[goal])
                explored.add(path.end)
        minimum = 100000000000000
        for value in hvalues:
            if hvalues[value] < minimum:
                minimum = hvalues[value]
        for key in hvalues:
            if hvalues[key] == minimum:
                next_city = key
            elif hvalues[key] == minimum and random.choice([True, False]):
                next_city = key
        explored.add(current)
        frontier.put((heuristic(cities[next_city], cities[goal]), next_city))
        mypath.append(next_city)
        current = next_city
    return False

def dijkstra(start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    came_from = {start: None}
    gvalues = {start: 0}
    while not frontier.empty():
        current_cost, current = frontier.get()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            pathstr = path_to_string(path)
            print(f"Path found: {pathstr}")
            print(f"Vertices explored: {len(explored)}")
            return True
        explored.add(current)
        for path in cities[current].connections.values():
            tentative_g = gvalues[current] + path.cost
            if path.end not in gvalues or tentative_g < gvalues[path.end]:
                gvalues[path.end] = tentative_g
                frontier.put((gvalues[path.end], path.end))
                came_from[path.end] = current
    print("No path found.")
    return False

def heuristic(city1, city2):
    R = 3958.8 
    lat1 = math.radians(city1.lat)
    lon1 = math.radians(city1.long)
    lat2 = math.radians(city2.lat)
    lon2 = math.radians(city2.long)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

if __name__ == "__main__":
    cities, paths = load_paths(filename1, filename2)
    on_start()

