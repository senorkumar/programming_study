#assume there is a Node class
#constructor Node(data)
#Node.next which is either another Node or None, constructor sets it to None 
#Node.data is the data in the Node


#Note: I didnt see that intersecting lists have the same tails, which would have let me end earlier in the case of non intersecting lists
def intersection(head_1, head_2):
	if not head_1 or not head_2:
		return False

	#otherwise both lists exist
	len_1 = length(head_1)
	len_2 = length(head_2)

	diff = len_1-len_2

	#len 1 is larger than len 2
	if diff > 0:
		for _ in range(diff):
			if head_1:
				head_1 = head_1.next
	elif diff < 0:
		for _ in range(-diff):
			if head_2:
				head_2 = head_2.next

	#head 1 and head 2 are the same distance from the tail or one of them is None

	if not (head_1 and head_2):
		return False

	#now we check if they ever run into each other
	while(head_1 or head_2):
		if head_1 == head_2:
			return head_1

		head_1 = head_1.next
		head_2 = head_2.next

	return False







#given a LL head returns how long the LL is
def length(head):
