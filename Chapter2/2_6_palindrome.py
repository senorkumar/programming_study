#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None, constructor sets it to None 
#Node.data is the data in the Node

#Notes - I could have used a stack instead of reversing and comparing, but they have the same asymptotic constraints


def palindrome(head):

	if head is None:
		return True


	copy_head = copy(head)
	reverse_head = reverse_ll(head)

	return check_same(head, reverse_head)




#returns a copy of LL given the original
def copy(head):
	new_list_head = Node(None)
	new_list_pointer = new_list_head

	while(head is not None):
		data = head.data

		new_list_pointer.next = Node(data)

		new_list_pointer = new_list_pointer.next

		head = head.next



	return new_list_head.next



#given a LL, reverses it
def reverse_ll(head):
	curr_pointer = head 
	prev_pointer = None

	while curr_pointer is not None:
		next_pointer = curr_pointer.next

		curr_pointer.next = prev_pointer

		prev_pointer = curr_pointer
		curr_pointer = next_pointer

	return prev_pointer


def check_same(head_1, head_2):
	while head_1 and head_2:
		if head_1.data != head_2.data:
			return False
		
		head_1 = head_1.next
		head_2 = head_2.next



	if head_1 is None and head_2 is None:
		return True
	else:
		return False

