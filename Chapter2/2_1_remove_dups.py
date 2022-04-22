

#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None
#Node.data is the data in the Node


def remove_dups(head):
	s = set()

	prev_pointer = None
	curr_pointer = head

	while curr_pointer is not None:
		if curr_pointer.data in s:
			curr_pointer = curr_pointer.next
			remove_node(prev_pointer)

		else:
			s.add(curr_pointer.data)
			prev_pointer = curr_pointer
			curr_pointer = curr_pointer.next


#assumes that the node you would like to delete exists
def remove_node(prev):
	to_delete = prev.next

	#check if we are deleting the last node in the LL
	if to_delete.next is None:
		prev.next = None
		return

	else:
		after = to_delete.next
		prev.next = after
		return