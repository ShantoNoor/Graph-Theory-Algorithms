class TreeNode:
	def __init__(self, id, parent, child):
		self.id = id
		self.parent = parent
		self.child = child


def rootTree(g, rootId = 0):
	root = TreeNode(rootId, None, [])
	return buildTree(g, root, None)


def buildTree(g, node, parent):
	for childId in g[node.id]:
		if parent != None and childId == parent.id:
			continue

		new_child = TreeNode(childId, node, [])
		node.child.append(new_child)
		buildTree(g, new_child, node)

	return node


def treeCenters(t):
	n = len(t)
	degree = [0]*n
	leafs = []

	for i in range(n):
		degree[i] = len(t[i])

		if degree[i] == 0 or degree[i] == 1:
			leafs.append(i)
			degree[i] = 0

	count = len(leafs)
	while count < n:
		new_leafs = []
		for node in leafs:
			for neighbor in t[node]:
				degree[neighbor] -= 1
				if degree[neighbor] == 1:
					new_leafs.append(neighbor)

			degree[node] = 0

		count += len(new_leafs)
		leafs = new_leafs

	return leafs


def printTree(tree):
	print(tree.id, end=' ')
	for i in tree.child:
		printTree(i)


def encodeTree(node):
	# if node == None:
	# 	return ""

	labels = []
	for child in node.child:
		labels.append(encodeTree(child))

	labels.sort()

	result = ""
	for label in labels:
		result += label

	return "(" + result + ")"


def areTreesIsomorphic(tree1, tree2):
	tree1_centers = treeCenters(tree1)
	tree2_centers = treeCenters(tree2)

	tree1_rooted = rootTree(tree1, tree1_centers[0])
	tree1_encoded = encodeTree(tree1_rooted)

	for center in tree2_centers:
		tree2_rooted = rootTree(tree2, center)
		tree2_encodeed = encodeTree(tree2_rooted)

		if tree1_encoded == tree2_encodeed:
			return True

	return False


tree1 = [
	[1], #0
	[0, 2, 4], #1
	[1], #2
	[4, 5], #3
	[1, 3], #4
	[3], #5
]

tree2 = [
	[1],#0
	[0, 2],#1
	[1, 4],#2
	[4],#3
	[2, 3, 5],#4
	[4],#5
]

print(areTreesIsomorphic(tree1, tree2))