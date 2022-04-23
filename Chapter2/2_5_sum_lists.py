#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None, constructor sets it to None 
#Node.data is the data in the Node


def sum_lists(list_1, list_2):
	carry = 0
	answer_head = Node(None)
	answer_pointer = answer_head
	while list_1 is not None and list_2 is not None:
		data_1 = list_1.data
		data_2 = list_2.data

		total = data_1+data_2+carry
		value = total%10
		carry = total/10

		new_node = Node(value)
		answer_pointer.next = new_node
		answer_pointer = answer_pointer.next

		list_1 = list_1.next
		list_2 = list_2.next


	if list_1 is not None or list_2 is not None:

		if list_1 is not None:

			list_pointer = list_1

		elif list_2 is not None:
			list_pointer = list_2



		while list_pointer is not None:

			data = list_pointer.data

			total = data+carry
			value = total%10
			carry = total/10

			new_node = Node(value)
			answer_pointer.next = new_node
			answer_pointer = answer_pointer.next

			list_pointer = list_pointer.next

	return answer_head.next



def sum_lists_recursive(head_1, head_2):
	answer = Node(None)
	recursive_helper(head_1, head_2, answer, 0)
	return answer.next


def recursive_helper(head_1, head_2, answer_pointer, carry):

	if head_1 is None and head_2 is None:
		if carry > 0:
			answer_pointer.next = Node(value)
			answer_pointer = answer_pointer.next

		return


	else if head_1 is not None and head_2 is not None:
		data_1 = head_1.data
		data_2 = head_2.data

		total = data_1 + data_2 + carry

		value = total%10
		carry = total/10

		answer_pointer.next = Node(value)
		answer_pointer = answer_pointer.next

		head_1 = head_1.next
		head_2 = head_2.next
		return recursive_helper(head_1, head_2, answer_pointer, carry)





















