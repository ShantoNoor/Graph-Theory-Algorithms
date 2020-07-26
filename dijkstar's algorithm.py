class pqueue:
	def __init__(self): self.q = []
	def enq(self, n, v):
		(self.q).append([n, v])
		(self.q).sort(key=lambda x: x[1], reverse=True)
	def deq(self): return (self.q).pop()
	def isEmpty(self): return not bool(len(self.q))


def dijkstra(g, s, e):
	n = len(g)
	visited = [False]*n
	prev = [-1]*n
	dist = [100]*n
	dist[s] = 0

	pq = pqueue()
	pq.enq(s, 0)

	while not pq.isEmpty():
		node = pq.deq()

		visited[node[0]] = True
		if dist[node[0]] < node[1]: continue

		for nodes in g[node[0]]:
			if visited[nodes[0]]: continue

			new_dist = node[1] + nodes[1]
			if dist[nodes[0]] > new_dist:
				prev[nodes[0]] = node[0]
				dist[nodes[0]] = new_dist
				pq.enq(nodes[0], dist[nodes[0]])

		if node[0] == e: return dist[e], prev

	return 100, prev


def findShortestPath(g, s, e):
	if e == s: return [s]

	dist, prev = dijkstra(g, s, e)
	if dist == 100: return []

	path = []
	node = e
	while prev[node] != -1:
		path.append(node)
		node = prev[node]

	if node != s: return []

	path.append(node)
	path.reverse()
	return path


g = [
	[[1, 4], [2, 1]],#0
	[[3, 1]],#1
	[[1, 2], [3, 5]],#2
	[[4, 3]],#3
	[],#4
]

print(findShortestPath(g, 1, 0))