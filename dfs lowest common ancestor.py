#Eulerian Path with Range Minimum Query(RMQ)

t = [
	[1, 2], #0
	[3], #1
	[4, 5], #2
	[], #3
	[6], #4
	[], #5
	[], #6
]

n = len(t)

depth = [0]*(2*n-1)
nodes = [0]*(2*n-1)
last = [0]*n
lastIndex = 0

def visit(node, depthValue):
	global lastIndex
	depth[lastIndex] = depthValue
	nodes[lastIndex] = node
	last[node] = lastIndex
	lastIndex += 1


def dfs(node=0, depthValue=0):
	visit(node, depthValue)
	for i in t[node]:
		dfs(i, depthValue+1)
		visit(node, depthValue)


def lca(a, b):
	dfs()

	a = last[a]
	b = last[b]

	if a > b: a, b = b, a

	minIndex = a
	for i in range(a+1, b+1):
		if depth[i] < depth[minIndex]: 
			minIndex = i

	print(nodes[minIndex])


lca(6, 3)