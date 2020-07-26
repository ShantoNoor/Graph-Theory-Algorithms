class TreeNode:
	def __init__(self, id, parent, child):
		self.id = id
		self.parent = parent
		self.child = child


g = [
	[1, 2, 5], #0
	[0], #1
	[0, 3], #2
	[2], #3
	[5], #4
	[0, 4, 6], #5
	[5]  #6
]

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


def printTree(tree):
	print(tree.id, end=' ')
	for i in tree.child:
		printTree(i)


printTree(rootTree(g, 5))