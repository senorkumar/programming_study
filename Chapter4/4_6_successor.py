class Tree_Node:
	def __init__(self,	data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None


def successor(root):

	if root.right:
		return min_val(root.right)
	else:
		return first_right_parent(root.parent, root.data)
	




#returns the minimum value in binary search tree
#which is always the leftmost leaf
#assumes that always called on non empty tree(so at least one node)
def min_val(root):
	if root.left:
		min_val(root.left)
	else:
		return root.data


def first_right_parent(node, value):
	
	#if we reach the root of the tree, so no right parents of original 
	if not root:
		return None 

	#detect if we moved right 
	if node.data > value:
		return node.data

	#otherwise we moved left
	return first_right_parent(node.parent, value)




