I = float('inf')
m = [
	[I, 10, 15, 20],
	[5, I, 9, 10],
	[6, 13, I, 12],
	[8, 8, 9, I]
];

def combinations(r, n):
	subsets = []
	combination(0, 0, r, n, subsets)
	return subsets


def combination(st, at, r, n, subsets):
	if r == 0: subsets.append(st)
	else:
		for i in range(at, n):
			st = st | (1 << i)
			combination(st, i+1, r-1, n, subsets)
			st = st & ~(1 << i)


def setup(m, memo, s, n):
	for i in range(n):
		if i == s: continue
		memo[i][1 << s | 1 << i] = m[s][i]


def notIn(i, subset):
	return ((1 << i) & subset) == 0


def solve(m, memo, s, n):
	for r in range(3, n+1):
		for subset in combinations(r, n):
			if notIn(s, subset): continue

			for nxt in range(n):
				if nxt == s or notIn(nxt, subset):
					continue

				state = subset ^ (1 << nxt)
				minDist = I

				for e in range(n):
					if e == s or e == nxt or notIn(e, subset):
						continue

					newDistance = memo[e][state] + m[e][nxt]

					if newDistance < minDist: minDist = newDistance

				memo[nxt][subset] = minDist


def findMinCost(m, memo, s, n):
	end_state = (1 << n) - 1

	minTourCost = I

	for i in range(n):
		if i == s: continue
		tourCost = memo[i][end_state] + m[i][s]
		if tourCost < minTourCost:
			minTourCost = tourCost

	return minTourCost


def findOptimalTour(m, memo, s, n):
	lastIndex = s
	state = (1 << n) - 1 #end state
	tour = [-1]*(n+1)

	for i in range(n-1, 0, -1):
		index = -1
		for j in range(n):
			if j == s and notIn(j, state): continue
			if index == -1: index = j
			prevDist = memo[index][state] + m[index][lastIndex]
			newDist = memo[j][state] + m[j][lastIndex]
			if newDist < prevDist: index = j

		tour[i] = index
		state = state^(1 << index)
		lastIndex = index

	tour[0] = tour[n] = s
	return tour


def TSP(m, s):
	n = len(m)
	memo = [[I for a in range(1 << n)]
				for b in range(n)]
	setup(m, memo, s, n)
	solve(m, memo, s, n)
	minTourCost = findMinCost(m, memo, s, n)
	minTourPath = findOptimalTour(m, memo, s, n)

	return (minTourCost, minTourPath)


print(TSP(m, 0))