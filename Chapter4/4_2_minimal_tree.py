
class Node:
	def __init__(self,	data):
		self.data = data
		self.left = None
		self.right = None




def minimal_tree(values):
	if not len(values):
		return None
	else:
		return recursive_helper(values)


def recursive_helper(values):
	if len(values) == 0:
		return None
	if len(values) == 1:
		return Node(values[0])
	else:
		if len(values)%2 ==0:
			middle_index = len(values)//2 -1
		else:
			middle_index = len(values)//2

		middle_value = values[middle_index]
		root = Node(middle_value)

		
		
		left_arr = values[:middle_index]
		right_arr = values[middle_index+1:]

		root.left = recursive_helper(left_arr)
		root.right = recursive_helper(right_arr)

		return root





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

res = minimal_tree([1,2,3,4,5,6,7,8,9])

print2D(res)

