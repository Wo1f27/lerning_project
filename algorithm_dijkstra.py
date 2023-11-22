import heapq

def dijkstra(graph, start_vertex):
    distanses = {vertex: float('infinity') for vertex in graph}
    distanses[start_vertex] = 0
    pq = [(0, start_vertex)]

    while len(pq) > 0:
        current_dist, current_vertex = heapq.heappop(pq)
        if current_dist > distanses[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            dist = current_dist + weight
            if dist < distanses[neighbor]:
                distanses[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distanses


graph = {
    'A': {'B': 4, 'C': 9},
    'B': {'D': 2},
    'C': {'D': 7},
    'D': {}
}
print(dijkstra(graph, 'A'))
