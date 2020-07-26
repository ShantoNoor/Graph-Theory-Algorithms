g = {
	'A': ['D'],
	'B': ['D'],
	'C': ['A', 'B'],
	'D': ['G', 'H'],
	'E': ['A', 'D', 'F'],
	'F': ['J', 'K'],
	'G': ['I'],
	'H': ['I', 'J'],
	'I': ['L'],
	'J': ['L', 'M'],
	'K': ['J'],
	'L': [],
	'M': []
}
visited = { k: False for k in g.keys() }
topological_order = []

def dfs(node):
	visited[node] = True
	for n in g[node]:
		if visited[n] == False:
			dfs(n)

	topological_order.append(node)

def topological_sort():
	for node in g.keys():
		if visited[node] == False:
			dfs(node)

	topological_order.reverse()


topological_sort()
print(topological_order)