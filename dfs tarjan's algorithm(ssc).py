g = [
	[1], #0
	[2], #1
	[0], #2
	[4,7], #3
	[5], #4
	[0,6], #5
	[0,2,4], #6
	[3,5]  #7
]

n = len(g)
Id = 0
sccCount = 0

ids = [-1]*n
low = [0]*n
onStack = [False]*n
s = [] # s -> for stack

def dfs(at):
	global Id, sccCount

	s.append(at)
	onStack[at] = True
	ids[at] = low[at] = Id
	Id += 1

	for to in g[at]:
		if ids[to] == -1: dfs(to)
		if onStack[to]: low[at] = min(low[at], low[to])

	if ids[at] == low[at]:
		node = s.pop()
		while(True):
			onStack[node] = False
			low[node] = low[at]

			if node == ids[at]: break
			node = s.pop()

		sccCount += 1


def findSccs(n):
	for i in range(n):
		if ids[i] == -1:
			dfs(i)


def printSccs(n):
	global sccCount
	findSccs(n)
	if sccCount == 0:
		print('No strongly connected components found!')
	else:
		print(sccCount, 'strongly connected components found!')
		low2 = [0]*n
		for i in range(n): low2[i] = low[i]
		for i in range(sccCount):
			m = min(low2)

			for j in range(n):
				if low2[j] == m:
					print(ids[j], end=' ')
					low2[j] = float('inf')

			print()


printSccs(n)