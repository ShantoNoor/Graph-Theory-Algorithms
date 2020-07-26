g = [
	[0, 3, 0, 3, 0, 0, 0], #0 - source
    [0, 0, 4, 0, 0, 0, 0], #1
    [3, 0, 0, 1, 2, 0, 0], #2
    [0, 0, 0, 0, 2, 6, 0], #3
    [0, 1, 0, 0, 0, 0, 1], #4
    [0, 0, 0, 0, 0, 0, 9], #5
    [0, 0, 0, 0, 0, 0, 0]  #6 - sync
] # max_flow = 5
n = len(g)
s = 0
e = n - 1

# g = [
# 	[0, 1, 5, 0, 0, 0], #0
# 	[0, 0, 7, 10, 0, 0], #1
# 	[0, 0, 0, 1, 0, 11], #2
# 	[0, 0, 0, 0, 0, 12], #3
# 	[6, 14, 0, 0, 0, 0], #4 - source
# 	[0, 0, 0, 0, 0, 0], #5 - sync
# ] # max_flow = 20
# n = len(g)
# s = n - 2
# e = n - 1

# g = [
# 	[0, 16, 13, 0, 0, 0], # - source
# 	[0, 0, 10, 12, 0, 0],
# 	[0, 4, 0, 0, 14, 0],
# 	[0, 0, 9, 0, 0, 20],
# 	[0, 0, 0, 7, 0, 4],
# 	[0, 0, 0, 0, 0, 0] # - sync
# ] # max_flow = 23
# n = len(g)
# s = 0
# e = n - 1

def bfs(s, e):
	visited = [False]*n
	parent = [-1]*n

	q = []
	q.append(s)

	while(len(q)):
		node = q.pop(0)
		visited[node] = True

		if visited[e]: break

		for edge in range(n):
			if(g[node][edge] > 0 and not visited[edge]):
				parent[edge] = node
				q.append(edge)

	path = []
	value = []

	if(not visited[e]): return path, value

	while(parent[e] != -1):
		value.append(g[parent[e]][e])
		path.append([parent[e], e])
		e = parent[e]

	path.reverse()
	return path, value


def ford_fulkerson(s, e):
	max_flow = 0

	path, value = bfs(s, e)
	while(len(path)):
		min_cut = min(value)
		max_flow += min_cut
		for edge in path:
			g[edge[0]][edge[1]] -= min_cut
			g[edge[1]][edge[0]] += min_cut

		path, value = bfs(s, e)

	return max_flow


print(ford_fulkerson(s, e))