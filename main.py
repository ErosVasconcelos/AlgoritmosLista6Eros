import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Função para carregar a base de dados e construir o grafo
def carregar_base_dados(file_path):
    grafo = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("%") or line.strip() == "":
                continue
            else:
                data = list(map(int, line.strip().split()))
                node1 = data[0] - 1
                node2 = data[1] - 1
                grafo.add_edge(node1, node2)
    return grafo

# Função para calcular o menor caminho usando o algoritmo de Dijkstra
def dijkstra(grafo, origem, destino):
    caminho = nx.shortest_path(grafo, source=origem, target=destino)
    distancia = nx.shortest_path_length(grafo, source=origem, target=destino)
    return caminho, distancia

# Função para visualizar o grafo de forma mais legível
def visualizar_grafo():
    fig, ax = plt.subplots(figsize=(10, 8))  # Definindo o tamanho da figura
    sampled_nodes = random.sample(list(grafo.nodes()), min(len(grafo.nodes()), 50))  # Amostra aleatória de até 50 vértices
    subgraph = grafo.subgraph(sampled_nodes)  # Subgrafo com os vértices amostrados
    pos = nx.spring_layout(subgraph, seed=42)  # Layout do subgrafo usando o algoritmo de spring layout
    nx.draw(subgraph, pos, with_labels=True, ax=ax)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, columnspan=2)  # Usar grid em vez de pack

# Função para calcular e exibir o menor caminho
def calcular_menor_caminho():
    origem = int(entry_origem.get())
    destino = int(entry_destino.get())
    caminho, distancia = dijkstra(grafo, origem, destino)
    label_resultado.config(text=f"Menor caminho entre {origem} e {destino}: {caminho}\nDistância mínima: {distancia}")

# Caminho para o arquivo de dados
base_dados = "ia-crime-moreno.edges.txt"  # Substitua pelo caminho correto do seu arquivo de dados

# Carregar a base de dados e construir o grafo
grafo = carregar_base_dados(base_dados)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Menor Caminho")

# Criar os widgets
label_origem = tk.Label(root, text="Vértice de Origem:")
label_destino = tk.Label(root, text="Vértice de Destino:")
entry_origem = tk.Entry(root)
entry_destino = tk.Entry(root)
button_visualizar_grafo = tk.Button(root, text="Visualizar Grafo", command=visualizar_grafo)
button_calcular = tk.Button(root, text="Calcular Menor Caminho", command=calcular_menor_caminho)
label_resultado = tk.Label(root, text="")

# Posicionar os widgets na janela
label_origem.grid(row=0, column=0)
label_destino.grid(row=1, column=0)
entry_origem.grid(row=0, column=1)
entry_destino.grid(row=1, column=1)
button_visualizar_grafo.grid(row=2, columnspan=2)
button_calcular.grid(row=3, columnspan=2)
label_resultado.grid(row=4, columnspan=2)

# Rodar o loop principal
root.mainloop()
