n = 13
g = [
		[7, 9, 11],#0
		[8, 10],#1
		[3, 12],#2
		[2, 4, 7],#3
		[3],#4
		[6],#5
		[5, 7],#6
		[0, 3, 6, 11],#7
		[1, 9, 12],#8
		[0, 8, 10],#9
		[1, 9],#10
		[0, 7],#11
		[2, 8]#12
]

visited = [bool(False)]*n
q = []
prev = [int(-1)]*n

def bfs(node):
	q.append(node)
	visited[node] = True

	while(len(q)):
		node = q.pop(0)

		for nextNode in g[node]:
			if not visited[nextNode]:
				q.append(nextNode)
				visited[nextNode] = True
				prev[nextNode] = node


def find_path(s, e):
	path = []
	bfs(s)
	node = e
	while prev[node] != -1:
		path.append(node)
		node = prev[node]

	path.append(node)
	path.reverse()

	if path[0] == s:
		f = False
		for node in path:
			if(f): print('->', end='')
			print(node, end='')
			f = True
	else:
		print('There is no path', end='')

	print()


find_path(5,8)