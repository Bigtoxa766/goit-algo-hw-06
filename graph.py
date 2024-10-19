import networkx as nx
import matplotlib.pyplot as plt

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



