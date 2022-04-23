#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None, constructor sets it to None 
#Node.data is the data in the Node

def partition(head, pivot):
	#point to the heads of these LLs
	lower = Node(None)
	higher = Node(None)

	#point to the last node in these LLs
	lower_pointer = lower

	higher_pointer = higher

	while head is not None:
		data = head.data
		if data < pivot:
			lower_pointer.next = Node(data)
			lower_pointer = lower_pointer.next

		elif data >= pivot:
			higher_pointer.next = Node(data)
			higher_pointer = higher_pointer.next

		head = head.next


	lower = lower.next
	higher = higher.next

	#if both lists exist merge them
	if lower and higher:
		lower_pointer.next = higher
		return lower

	elif lower and not higher:
		return lower

	elif higher and not lower:
		return higher

	else:
		return None


