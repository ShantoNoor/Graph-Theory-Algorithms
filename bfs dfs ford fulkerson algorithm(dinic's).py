# g = [
# 	[0, 3, 0, 3, 0, 0, 0], #0 - source
#     [0, 0, 4, 0, 0, 0, 0], #1
#     [3, 0, 0, 1, 2, 0, 0], #2
#     [0, 0, 0, 0, 2, 6, 0], #3
#     [0, 1, 0, 0, 0, 0, 1], #4
#     [0, 0, 0, 0, 0, 0, 9], #5
#     [0, 0, 0, 0, 0, 0, 0]  #6 - sync
# ] # max_flow = 5
# n = len(g)
# s = 0
# e = n - 1

g = [
	[0, 1, 5, 0, 0, 0], #0
	[0, 0, 7, 10, 0, 0], #1
	[0, 0, 0, 1, 0, 11], #2
	[0, 0, 0, 0, 0, 12], #3
	[6, 14, 0, 0, 0, 0], #4 - source
	[0, 0, 0, 0, 0, 0], #5 - sync
] # max_flow = 20
n = len(g)
s = n - 2
e = n - 1

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

def bfs(g, n, s, e):
	l = 0
	visited = [False]*n
	q = []

	level = [-1]*n

	q.append(s)
	level[s] = l;
	while(len(q)):
		node = q.pop(0)
		visited[node] = True
		for edge in range(n):
			if g[node][edge] > 0 and not visited[edge]:
				if level[edge] == -1:
					level[edge] = level[node]+1
				q.append(edge)

	if(visited[e]): return level
	else: return []


path = []
visited = []
level = []
value = []

def dfs(g, n, s, e):
	visited[s] = True
	if s == e: return

	for edge in range(n):
		if not visited[edge] and level[edge] == level[s]+1 and g[s][edge] > 0:
			path.append([s, edge])
			value.append(g[s][edge])

			dfs(g, n, edge, e)
			if visited[e]: return

			visited[edge] = False
			path.pop()
			value.pop()


def ford_fulkerson(g, n, s, e):
	global path
	global visited
	global level
	global value

	visited = [False]*n
	level = bfs(g, n, s, e)
	path = []
	value = []

	max_flow = 0

	while(len(level)):
		dfs(g, n, s, e)
		while visited[e]:
			min_cut = min(value)
			max_flow += min_cut

			for edge in path:
				g[edge[0]][edge[1]] -= min_cut
				g[edge[1]][edge[0]] += min_cut

			visited = [False]*n
			value = []
			path = []
			dfs(g, n, s, e)

		visited = [False]*n
		level = bfs(g, n, s, e)
		path = []
		value = []

	return max_flow


print(ford_fulkerson(g, n, s, e))