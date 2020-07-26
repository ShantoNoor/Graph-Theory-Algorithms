n = 13
g = [
		[9],		#0
		[0],		#1 
		[],			#2
		[2, 4, 5],	#3
		[],			#4
		[6], 		#5
		[7], 		#6
		[3, 10], 	#7
		[7],		#8
		[8], 		#9
		[11], 		#10
		[7], 		#11
		[]			#12
]
visited = [bool(False)]*n

def dfs(at):
	if visited[at]: return

	visited[at] = True
	print(at, end=' ') # <--print

	neighbours = g[at]
	for nextNode in neighbours:
		dfs(nextNode)


startNode = 0
dfs(startNode)