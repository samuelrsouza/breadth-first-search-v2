from queue import Queue

GRAFO = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


def bfs(startingNode, destinationNode, path=None):
    # Para acompanhar o nó que já visitamos
    visited = {}
    # Para manter o controle da distância
    distance = {}
    # Para definir o nó pai
    parent = {}

    if path is None:
        path = [startingNode]
    if startingNode == destinationNode:
        yield path

    bfs_traversal = []
    # O BFS é baseado em fila, portanto, foi importado a biblioteca 'Queue'
    queue = Queue()

    # percorrendo todas as cidades no grafo e atribui valor nulo para todos
    for city in GRAFO.keys():
        # uma vez que inicialmente nenhuma cidade é visitada, então não haverá nada na lista visitada
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # definindo a origem
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    # enquanto a fila não estiver vazia, cada nó visitado será o elemento u
    # para que seja verificado se o nó atual já visitou outros nós e os altera nos dicionarios
    # basicamente o u é o priority queue dos nós que foram visitados
    while not queue.empty():
        u = queue.get()    # primeiro elemento da fila
        bfs_traversal.append(u)

        # explorando cidades adjacentes à cidade inserida
        # v = cidade que está sendo visitado
        for v in GRAFO[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)

        # para chegar na cidade destino
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)


# Starting City & Destination City
def main():
    print('Digite a origem :', end=' ')
    startingNode = input().strip()
    print('Digite o destino :', end=' ')
    destinationNode = input().strip()
    if startingNode not in GRAFO or destinationNode not in GRAFO:
        print('Erro: Esta cidade não existe.')
    else:
        print('\nCaminhos possíveis:')
        paths = bfs(startingNode, destinationNode)
        for path in paths:
            print(' -> '.join(city for city in path))

if __name__ == '__main__':
    main()
