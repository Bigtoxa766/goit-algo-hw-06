import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

# Створення неорієнтованого графа
G = nx.Graph()

# Створення вершин
stops = ['Stop 1', 'Stop 2', 'Stop 3', 'Stop 4', 'Stop 5', 'Stop 6', 'Stop 7']
G.add_nodes_from(stops)

# Додавання ребер
edges = [('Stop 1', 'Stop 2'), ('Stop 1', 'Stop 3'), ('Stop 2', 'Stop 4'), 
         ('Stop 3', 'Stop 4'), ('Stop 4', 'Stop 5'), ('Stop 5', 'Stop 6'), 
         ('Stop 6', 'Stop 7'), ('Stop 3', 'Stop 6')]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='#A0CBE2',
node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
plt.title('Transport Network Graph')
plt.show()

# Аналіз характеристик графа
# Кількість вершин
num_nodes = G.number_of_nodes()
print(f"Кількість вершин: {num_nodes}")

# Кількість ребер
num_edges = G.number_of_edges()
print(f"Кількість ребер: {num_edges}")

# Ступінь вершин
degree_dict = dict(G.degree())
print("Ступінь кожної вершини:")
for stop, degree in degree_dict.items():
    print(f"{stop}: {degree}")

# Алгоритм DFS для пошуку шляху
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited =set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path.copy(), visited.copy())
            if result:
                return result

    return None

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node =path[-1]

        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# Вибираємо початкову та кінцеву точки
start_node = 'Stop 1'
goal_node = 'Stop 7'

# Знаходимо шляхи за допомогою DFS і BFS
dfs_res = dfs_path(G, start_node, goal_node)
bfs_res = bfs_path(G, start_node, goal_node)

print(f"Шлях, знайдений за допомогою DFS: {dfs_res}")
print(f"Шлях, знайдений за допомогою BFS: {bfs_res}")

# Порівняння результатів
if dfs_res != bfs_res:
        print("Шляхи різні для DFS та BFS.")
else:
    print("Шляхи однакові для DFS та BFS.")

edges_with_weights  = [('Stop 1', 'Stop 2', 7), ('Stop 1', 'Stop 3', 9), ('Stop 2', 'Stop 4', 10), 
         ('Stop 3', 'Stop 4', 11), ('Stop 4', 'Stop 5', 6), ('Stop 5', 'Stop 6', 2), 
         ('Stop 6', 'Stop 7', 9), ('Stop 3', 'Stop 6', 14)]

G.add_weighted_edges_from(edges_with_weights )

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]
    shortest_paths = {start: [start]}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor,edge_data in graph[current_node].items():
            weight = edge_data['weight']
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths

start_node_dijkstra = 'Stop 1'
distances, paths = dijkstra(G, start_node_dijkstra)

print(f"Найкоротші відстані від {start_node_dijkstra} (алгоритм Дейкстри):")
for stop, distance in distances.items():
    print(f"До {stop}: {distance} одиниць")

print("\nШляхи до кожної вершини (алгоритм Дейкстри):")
for stop, path in paths.items():
    print(f"Шлях до {stop}: {' -> '.join(path)}")
    
"""
Порівняння результатів:

1.Шляхи для DFS:
DFS може повертати довший шлях, оскільки він спочатку намагається дослідити одну гілку графа повністю, перш ніж повернутись назад і досліджувати інші можливі гілки.

2.Шляхи для BFS:
BFS гарантує знаходження найкоротшого шляху, оскільки він досліджує вершини рівень за рівнем і перевіряє всі сусідні вершини перед тим, як піти глибше.

Пояснення алгоритмів:

1.DFS (Пошук в глибину):
Алгоритм починає з вибраної вершини і досліджує якомога глибше сусідні вершини перед тим, як повернутись назад.
Він може знайти шлях, який не обов’язково є найкоротшим, оскільки він намагається досліджувати глибше перед тим, як розглянути інші можливі шляхи.

2.BFS (Пошук в ширину):
Алгоритм починає з вибраної вершини і досліджує всі сусідні вершини на одному рівні, перш ніж перейти до наступного рівня.
BFS завжди знаходить найкоротший шлях у неорієнтованому графі, якщо всі ребра мають однакову вагу.

BFS завжди знайде найкоротший шлях через те, що досліджує граф рівнями, 
тоді як DFS може знайти інший шлях, який не обов'язково є найкоротшим, але все ще приведе до мети.
"""