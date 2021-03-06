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

g = [
	[0, 16, 13, 0, 0, 0], # - source
	[0, 0, 10, 12, 0, 0],
	[0, 4, 0, 0, 14, 0],
	[0, 0, 9, 0, 0, 20],
	[0, 0, 0, 7, 0, 4],
	[0, 0, 0, 0, 0, 0] # - sync
] # max_flow = 23
n = len(g)
s = 0
e = n - 1

visited = [False]*n
path = []
value = []

def dfs(s, e, delta):
	visited[s] = True
	if s == e: return

	for i in range(n):
		if g[s][i] >= delta and visited[i] == False:
			path.append([s, i])
			value.append(g[s][i])

			dfs(i, e, delta)
			if visited[e]: return

			visited[i] = False
			path.pop()
			value.pop()


def find_large_capacity():
	big_capacity = -1
	for i in range(n):
		for j in range(n):
			if big_capacity < g[i][j]:
				big_capacity = g[i][j]

	delta = 1
	while(delta*2 < big_capacity): delta *= 2

	return delta


def ford_fulkerson(s, e):
	max_flow = 0
	delta  = find_large_capacity()

	while(delta > 0):
		dfs(s, e, delta)
		while(visited[e]):
			cut_value = min(value)
			max_flow += cut_value
			for edge in path:
				g[edge[0]][edge[1]] -= cut_value
				g[edge[1]][edge[0]] += cut_value

			while value != []: value.pop()
			while path != []: path.pop()
			for i in range(n): visited[i] = False
			dfs(s, e, delta)

		delta //= 2

	return max_flow


print(ford_fulkerson(s, e))
