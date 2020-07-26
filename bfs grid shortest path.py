adr = [-1, -1, 1, 1, -1, 1, 0, 0]
adc = [-1, 1, 1, -1, 0, 0, 1, -1]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

m = [
	['S', '.', '.', '#', '.', '.', '.'],
	['.', '#', '.', '.', '.', '#', '.'],
	['.', '#', '.', '.', '.', '.', '.'],
	['.', '.', '#', '#', '.', '.', '.'],
	['#', '.', '#', 'E', '.', '#', '.'],
] # dungeon

R = 5
C = 7
sr = 0
sc = 0
rq = [] #queue for row
cq = []	#queue for col

move_count = 0
nodes_left_in_layer = 0
nodes_in_next_layer = 0

reached_end = False

visited = [[bool(False) for b in range(C)]
			for a in range(R)]

def explore_neighbours(r, c):
	global nodes_in_next_layer
	for i in range(4):
		rr = r + dr[i]
		cc = c + dc[i]

		if rr < 0 or cc < 0: continue
		if rr >= R or cc >= C: continue

		if visited[rr][cc]: continue
		if m[rr][cc] == '#': continue

		rq.append(rr)
		cq.append(cc)

		visited[rr][cc] = True
		nodes_in_next_layer += 1


def bfs():
	rq.append(sr)
	cq.append(sc)
	visited[sr][sc] = True

	global move_count
	global nodes_left_in_layer
	global nodes_in_next_layer
	global reached_end

	nodes_left_in_layer = 1

	while len(rq): #len(cq)
		r = rq.pop(0)
		c = cq.pop(0)

		if m[r][c] == 'E':
			reached_end = True
			break

		explore_neighbours(r, c)

		nodes_left_in_layer -= 1
		if nodes_left_in_layer == 0:
			nodes_left_in_layer = nodes_in_next_layer
			nodes_in_next_layer = 0
			move_count += 1

	if reached_end:
		return move_count

	return -1


print(bfs())