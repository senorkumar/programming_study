class Tree_Node:
	def __init__(self,	data):
		self.data = data
		self.left = None
		self.right = None




def validate(root):
	return recursive_helper(root, float('-inf'), float('inf'))


def recursive_helper(root, lower_bound, upper_bound):
	#base case
	if root is None:
		return True


	#validate root
	elif not (root.data < upper_bound and root.data > lower_bound):
		return False


	#otherwise we recurse
	return recursive_helper(root.left, lower_bound, root.data) and recursive_helper(root.right, root.data, upper_bound)


