pInf = float('inf')
nInf = float('-inf')

g = [
	[[1, 5]],#0
	[[2, 20], [5, 30], [6, 60]],#1
	[[3, 10], [4, 75]],#2
	[[2, -15]],#3
	[[9, 100]],#4
	[[4, 25], [6, 5], [8, 50]],#5
	[[7, -50]],#6
	[[8, -10]],#7
	[],#8
	[],#9
]

def bellman_ford(g, s=0):
	n = len(g)
	dist = [pInf]*n
	dist[s] = 0

	# Bellman Ford Algorithm
	for u in range(n-1):
		for v in range(n-1):
			for node in g[v]:
				if dist[node[0]] > dist[v] + node[1]:
					dist[node[0]] = dist[v] + node[1]


	# for detecting negitive waight cycle
	for v in range(n-1):
		for node in g[v]:
			if dist[node[0]] > dist[v] + node[1]:
				dist[node[0]] = nInf


	return dist


print(bellman_ford(g))
