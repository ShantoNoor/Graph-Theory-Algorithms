g = {
	'A': [['B', 3], ['C', 6]],
	'B': [['C', 4], ['D', 4], ['E', 11]],
	'C': [['D', 8], ['G', 11]],
	'D': [['E', -4], ['F', 5], ['G', 2]],
	'E': [['H', 9]],
	'F': [['H', 1]],
	'G': [['H', 2]],
	'H': []
}
visited = { v: False for v in g.keys() }
topological_order = []

def dfs(node):
	visited[node] = True
	for n in g[node]:
		if visited[n[0]] == False:
			dfs(n[0])

	topological_order.append(node)

def topological_sort():
	for node in g.keys():
		if visited[node] == False:
			dfs(node)

	topological_order.reverse()


topological_sort()
print(topological_order)


def shortest_path_count(start_node='A'):
	shortest_path = { v: int(100) for v in g.keys() }
	shortest_path[start_node] = 0

	for node in topological_order:
		for nodes in g[node]:
			if shortest_path[nodes[0]] > shortest_path[node]+nodes[1]:
				shortest_path[nodes[0]] = shortest_path[node]+nodes[1]

	return shortest_path


def longest_path_count(start_node='A'):
	longest_path = { v: int(100) for v in g.keys() }
	longest_path[start_node] = 0

	for node in topological_order:
		for nodes in g[node]:
			if longest_path[nodes[0]] > longest_path[node]+(nodes[1]*-1):
				longest_path[nodes[0]] = longest_path[node]+(nodes[1]*-1)

	for n in g.keys(): longest_path[n] *= -1
	return longest_path


print(shortest_path_count())
print(longest_path_count())
