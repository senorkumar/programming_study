

class Tree_Node:
	def __init__(self,	data):
		self.data = data
		self.left = None
		self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_LL(root, answer):
	if root:
		answer = answer + str(root.data)
		print_LL(root.next, answer)
	else:
		print(answer)



#return a list of heads to LLs
def depths(root):
	heads = []
	depth = -1
	q = []
	q.insert(0,(root, 0))

	curr_head = None
	curr_pointer = None

	while (len(q) > 0):

		print(q)

		(curr_tree_node,curr_depth) = q.pop(-1)

		#we need to start a new LL
		if curr_depth != depth:

			#check if current LL exists and if so add it to heads
			if curr_head:
				heads.append(curr_head.next)

			curr_head = Node(None)
			curr_pointer = curr_head

			depth = curr_depth

		
		curr_pointer.next = Node(curr_tree_node.data)
		curr_pointer = curr_pointer.next

		if curr_tree_node.left:
			q.insert(0, (curr_tree_node.left, depth+1))

		if curr_tree_node.right:
			q.insert(0, (curr_tree_node.right, depth+1))

	return heads




COUNT = [10]
# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :

 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.data)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)




root = Tree_Node(1)
root.left = Tree_Node(2)
root.right = Tree_Node(3)

root.left.left = Tree_Node(4)
root.left.right = Tree_Node(5)
root.right.left = Tree_Node(6)
root.right.right = Tree_Node(7)

root.left.left.left = Tree_Node(8)
root.left.left.right = Tree_Node(9)
root.left.right.left = Tree_Node(10)
root.left.right.right = Tree_Node(11)
root.right.left.left = Tree_Node(12)
root.right.left.right = Tree_Node(13)
root.right.right.left = Tree_Node(14)
root.right.right.right = Tree_Node(15)



print2D(root)

heads = depths(root)


for l in heads:
	print_LL(l, '')










