import heapq
def dijkstra(grafo, origen):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0
    pq = [(0, origen)]

    while pq:
        distancia_actual, nodo = heapq.heappop(pq)
        if distancia_actual > dist[nodo]:
            continue
        for vecino, peso in grafo[nodo]:
            nueva_dist = distancia_actual + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(pq, (nueva_dist, vecino))
    return dist

grafo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1), ('D', 3)],
    'C': [('D', 2)],
    'D': []
}
print("Dijkstra desde A:")
print(dijkstra(grafo, 'A'))
