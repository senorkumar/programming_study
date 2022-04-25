
class Tree_Node:
	def __init__(self,	data):
		self.data = data
		self.left = None
		self.right = None


def height(root):
	if not root:
		return 0
	else:
		return 1 + max(height(root.left), height(root.right))


def balanced(root):
	answer = recursive_helper(root)
	print(answer)
	return (answer > -1)


def recursive_helper(root):

	if not root:
		return 0

	left_height = recursive_helper(root.left)
	right_height = recursive_helper(root.right)

	if left_height == -1 or right_height == -1:
		return -1

	elif abs(left_height - right_height) > 1:
		return -1

	else:
		return 1 +  max(left_height, right_height)





root = Tree_Node(1)
root.left = Tree_Node(2)
root.right = Tree_Node(3)

#root.left.left = Tree_Node(4)
root.left.right = Tree_Node(5)
root.right.left = Tree_Node(6)
root.right.right = Tree_Node(7)

#root.left.left.left = Tree_Node(8)
#root.left.left.right = Tree_Node(9)
root.left.right.left = Tree_Node(10)
root.left.right.right = Tree_Node(11)
root.right.left.left = Tree_Node(12)
root.right.left.right = Tree_Node(13)
root.right.right.left = Tree_Node(14)
root.right.right.right = Tree_Node(15)

print(balanced(root))