# prim's minimum spanning tree algorithm[lazy]

class pqueue:
	def __init__(self): self.q = []
	def enq(self, s, e, c):
		(self.q).append([s, e, c])
		(self.q).sort(key=lambda x: x[2], reverse=True)
	def deq(self): return (self.q).pop()
	def isEmpty(self): return not bool(len(self.q))


g = [
	[[1, 10], [2, 1], [3, 4]], #0
	[[0, 10], [2, 3], [4, 0]], #1
	[[0, 1], [1, 3], [3, 2], [5, 8]], #2
	[[0, 4], [2, 2], [5, 2], [6, 7]], #3
	[[1, 0], [5, 1], [7, 8]], #4
	[[2, 8], [3, 2], [4, 1], [6, 6], [7, 9]], #5
	[[3, 7], [5, 6], [7, 12]], #6
	[[4, 8], [5, 9], [6, 12]], #7
]

n = len(g)
visited = [False]*n
pq = pqueue()

def visit(node):
	visited[node] = True
	for n in g[node]:
		if visited[n[0]]: continue
		pq.enq(node, n[0], n[1])


def lazyPrims(s = 0):
	mstEdges = []
	mstCost = 0
	edgeCount = 0

	visit(s)

	while(not pq.isEmpty() and edgeCount != n - 1):
		edge = pq.deq()

		if visited[edge[1]]: continue

		visit(edge[1])
		mstEdges.append([edge[0], edge[1]])
		edgeCount += 1
		mstCost += edge[2]

	if edgeCount != n-1:
		return 0, []

	return [mstCost, mstEdges]


print(lazyPrims())
