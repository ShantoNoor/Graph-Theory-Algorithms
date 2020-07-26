nodes = ['A', 'B', 'C', 'D']
I = float('inf')
g = [
	[0, 9, -4, I],
	[6, 0, I, 2],
	[I, 5, 0, I],
	[I, I, 1, 0]
]

def setup(g):
	n = len(g)
	dp = [[0 for a in range(n)]
	    	for b in range(n)]

	nxt = [['X' for a in range(n)]
	    	for b in range(n)]

	for i in range(n):
		for j in range(n):
			dp[i][j] = g[i][j]
			if dp[i][j] != float('inf'):
				nxt[i][j] = j
				# nxt[i][j] = i

	return dp, nxt


def floyd_warshall(g):
	n = len(g)
	dp, nxt = setup(g)

	# Floyd Warshall All Pair Shortest Path Algorithm
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dp[i][j] > dp[i][k] + dp[k][j]:
					dp[i][j] = dp[i][k] + dp[k][j]
					nxt[i][j] = nxt[i][k]
					# nxt[i][j] = nxt[k][j]


	for k in range(n):
		for i in range(n):
			for j in range(n):
				if dp[i][j] > dp[i][k] + dp[k][j]:
					dp[i][j] = float('-inf')
					nxt[i][j] = -1

	return dp, nxt


def construce_path(nodes, g, s, e):
	dic = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }
	s = dic[s]
	e = dic[e]

	dist, nxt = floyd_warshall(g)
	path = []

	if dist[s][e] == I: return path

	node = s
	while(node != e):
		if node == -1: return []
		path.append(nodes[node])
		node = nxt[node][e]
	if nxt[node][e] == -1: return []
	path.append(nodes[node])
	return path

	# node = e
	# while(node != s):
	# 	if node == -1: return []
	# 	path.append(nodes[node])
	# 	node = nxt[s][node]
	# if nxt[s][node] != s: return []
	# path.append(nodes[node])
	# path.reverse()
	# return path


print(construce_path(nodes, g, 'A', 'B'))
