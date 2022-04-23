
#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None
#Node.data is the data in the Node


#Notes:
#I could have used two pointers in parallel instead of in series and stepped at the same time,
#but this solution has the same bigO runtime and memory 

def return_kth_to_last(head,k):
	#1. determine length
	length = get_len(head)

	#2. calc which node we want
	desired = length-k+1

	#3. except if that node DNE
	if desired < 1:
		raise Exception('node DNE')

	#4. find desired node
	return get_kth_node(head, k)



def get_len(head):
	curr_len = 0
	while head not None:
		curr_len+=1
		head = head.next

	return curr_len

def get_kth_node(head,k):
	curr_pos = 1

	while curr_pos != k:
		head = head.next
		curr_pos+=1

	return head
