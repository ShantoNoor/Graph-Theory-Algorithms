n = 18
g = [
		[4, 8, 13, 14],#0
		[5],#1
		[9, 15],#2
		[9],#3
		[0, 8],#4
		[1, 16, 17],#5
		[7, 11],#6
		[6, 11],#7
		[0, 4, 14],#8
		[2, 3, 15],#9
		[15],#10
		[6, 7],#11
		[],#12
		[0, 14],#13
		[8, 13],#14
		[2, 9, 10],#15
		[5],#16
		[5],#17
]
visited = [bool(False)]*n
components = [int(-1)]*n
color = 0

def dfs(at):
	if visited[at]: return

	visited[at] = True
	components[at] = color

	for nextNode in g[at]:
		dfs(nextNode)


def findComponents():
	global color
	for node in range(n):
		if not visited[node]:
			dfs(node)
			color += 1


findComponents()

for c in range(color):
	print('Color', c, end='')
	print(":", end=' ')
	for node in range(n):
		if components[node] == c:
			print(node, end=' ')

	print()