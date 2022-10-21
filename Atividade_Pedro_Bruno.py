# Atividade 1
# Nome: Pedro Bruno Fernandes do Nascimento
# Faculdade Única
# CCO6
# Algoritmos de Busca
# Largura e Profundidade

from collections import deque
import os

n = 20
inf = 9999
dist = [inf] * n
visitados = [False] * n
antecessor = [0] * n

VISITED = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
FILA = deque()

G = [
  [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

H = [
  [
    inf, 50, 100, inf, inf, inf, 45, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    50, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    100, inf, inf, 80, 90, inf, inf, 120, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, 80, inf, 45, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, 90, 45, inf, 55, inf, 85, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, 55, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    45, inf, inf, inf, inf, inf, inf, 90, 145, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, 120, inf, 85, inf, 90, inf, 100, inf, 155, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, 145, 100, inf, 55, inf, 73, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, 55, inf, 35, 45, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, 155, inf, 35, inf, 80, 55, inf, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, 73, 45, 80, inf, 65, 110, 120, inf,
    inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 55, 65, inf, 40, inf,
    inf, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 110, 40, inf, 25,
    85, inf, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 120, inf, 25, inf,
    100, 65, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 85, 100,
    inf, 50, inf, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 65,
    50, inf, 60, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, 60, inf, 150, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, 150, inf, inf
  ],
  [
    inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf,
    inf, inf, inf, inf, inf
  ],
]


def zerar_visitados():
  for i in range(n):
    VISITED[i] = 0


def DFS(v):
  VISITED[v] = 1
  print(str(v + 1) + "->", end="")
  for i in range(n):
    if (G[v][i] == 1):
      if (VISITED[i] == 0):
        DFS(i)


def DFSOrigDest(orig, dest):
  VISITED[orig] = 1
  print(str(orig + 1) + "->", end="")
  for i in range(dest):
    if (G[orig][i] == 1):
      if (VISITED[i] == 0):
        DFSOrigDest(i, dest)


def BFSOrigDest(orig, dest):
  VISITED[orig] = 1
  FILA.append(orig)
  print(str(orig + 1) + "->", end="")
  while not (len(FILA) == 0):
    w = FILA.popleft()
    for i in range(dest):
      if (G[w][i] == 1):
        if (VISITED[i] == 0):
          FILA.append(i)
          print(str(i + 1) + "->", end="")
          VISITED[i] = 1


def BFS(v):
  VISITED[v] = 1
  FILA.append(v)
  print(str(v + 1) + "->", end="")
  while not (len(FILA) == 0):
    w = FILA.popleft()
    for i in range(n):
      if (G[w][i] == 1):
        if (VISITED[i] == 0):
          FILA.append(i)
          print(str(i + 1) + "->", end="")
          VISITED[i] = 1


def removerAresta(orig, dest):
  G[orig - 1][dest - 1] = 0
  G[dest - 1][orig - 1] = 0
  print("Aresta [" + str(orig) + "][" + str(dest) + "] removida !")


def pesquisarOrigemDestino():
  os.system("clear")
  print("\n\n******* Menu de opções *******")
  print("Escolha uma opção")
  print("1  - Busca em Largura")
  print("2  - Busca em Profundidade")
  resp = input(" Digite sua opção: ")
  resp = int(resp)
  if (resp == 1 or resp == 2):
    origem = input("Qual o vértice de origem entre 1 e " + str(n) + ": ")
    origem = int(origem)
    origem = origem - 1

    destino = input("Qual o vértice de destino entre 1 e " + str(n) + ": ")
    destino = int(destino)
    destino = destino - 1
    if (origem >= 0 and origem < n and destino >= 0 and destino < n
        and origem != destino):
      if (resp == 1):
        zerar_visitados()
        BFSOrigDest(origem, destino)
      elif (resp == 2):
        zerar_visitados()
        DFSOrigDest(origem, destino)
    else:
      print("Vértice escolhido é inválido")
  else:
    print("Opção inválida!")


def distancia_min(dist, visitados):
  min = inf
  vertice_min = 0
  for v in range(n):
    if dist[v] < min and visitados[v] == False:
      min = dist[v]
      vertice_min = v
  return vertice_min


def imprime(start, dist, ant):
  for node in range(n):
    print(start + 1, "para ", node, " distância min ", dist[node],
          "antecessor: ", ant[node])


def dijkstra(matrix, start):
  dist[start] = 0
  for x in range(n):
    u = distancia_min(dist, visitados)
    visitados[u] = True
    for v in range(n):
      if (matrix[u][v] < inf and visitados[v] == False
          and dist[v] > dist[u] + matrix[u][v]):
        dist[v] = dist[u] + matrix[u][v]
        antecessor[v] = u
  imprime(start, dist, antecessor)


def prim():
  no_edge = 0
  total = 0
  while (no_edge < n - 1):
    minimum = inf
    x = 0
    y = 0
    for i in range(n):
      if VISITED[i]:
        for j in range(n):
          if ((not VISITED[j]) and H[i][j]):
            if minimum > H[i][j]:
              minimum = H[i][j]
              x = i
              y = j
    print(str(x) + "-" + str(y) + ":   " + str(H[x][y]))
    VISITED[y] = True
    if (H[x][y] != inf):  #Para evitar que a soma final levasse o INF
      total = total + H[x][y]
    no_edge += 1

  print("Custo Mínimo:", total)


op = 0
while not (op == 99):
  print("\n\n******* Menu de opções *******")
  print("Escolha uma opção")
  print("1  - Busca em Largura (matriz EX1) ")
  print("2  - Busca em Profundidade (matriz EX1)")
  print("3  - Remover aresta (matriz EX1)")
  print("4 -  Pesquisa por Origem Destino (matriz EX1)")
  print("5 -  Dijkstra (matriz EX2)")
  print("6 -  Árvore de Custo Mínimo(prim matriz EX2))")
  print("99 - Sair")
  op = input(" Digite sua opção: ")
  op = int(op)
  if (op > 0 and op <= 2):
    v = input("Qual o vértice de origem entre 1 e " + str(n) + ": ")
    v = int(v)
    v = v - 1
    if (v >= 0 and v < n):
      if (op == 1):
        zerar_visitados()
        BFS(v)
      elif (op == 2):
        zerar_visitados()
        DFS(v)
    else:
      print("Vértice escolhido é inválido")
  elif (op == 3):
    orig = input("Qual o vértice de origem entre 1 e " + str(n) + ": ")
    orig = int(orig)
    dest = input("Qual o vértice de destino entre 1 e " + str(n) + ": ")
    dest = int(dest)
    removerAresta(orig, dest)
  elif (op == 4):
    pesquisarOrigemDestino()
  elif (op == 5):
    vertice = input("Qual o vértice de origem entre 1 e " + str(n) + ": ")
    vertice = int(vertice)
    vertice = vertice - 1
    if (vertice >= 0 and vertice < n):
      dijkstra(H, vertice)
    else:
      print("Vértice escolhido é inválido")
  elif (op == 6):
    prim()
  elif (op == 99):
    print("Programa encerrado!")
  else:
    print("Opção inválida!")
