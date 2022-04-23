#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None, constructor sets it to None 
#Node.data is the data in the Node

#Note I overthought this one, we dont need to update all the nodes and do it in O(n)
#instead I could have done it in constant time by deleting the next node instead of the last node


def delete_middle(node):

	curr_pointer = node
	next_pointer = node.next



	while(True):

		curr_pointer.data = next_pointer.data


		if curr_pointer is None and next_pointer is None:
			break

		curr_pointer = next_pointer
		next_pointer = next_pointer.next



