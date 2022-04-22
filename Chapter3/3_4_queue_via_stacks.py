#assume there exists a Stack class w the following methods 
#pop
#push
#isEmpty
#len
#peek



#NOTE: in this version I did not take advantage of the fact that we could optimize for multiple pops in a row
def MyQueue:
	def __init__(self):
		self.main_stack = Stack()
		self.off_stack = Stack()
		self.size = 0
		self.top = None


	def add(data):
		self.main_stack.push(data)
		self.size+=1



	def remove():

		if self.isEmpty():
			raise Exception('Attempted to remove from empty queue')


		#move everything over to the off stack except the last value
		for _ in range(self.size-1):
			pop_val = self.main_stack.pop()
			self.off_stack.push(pop_val)

		#save the last value
		popped_value = self.main_stack.pop()

		#update top 
		self.top = self.off_stack.peek()

		self.size-=1

		#push everything back over to main stack
		for _ in range(self.size):
			pop_val = self.off_stack.pop()
			self.main_stack.push(pop_val)

		
		return popped_value


	def peek():
		return self.top


	def isEmpty():
		return self.size == 0



def MyQueue_v2:
	def __init__:

	def add():

	def remove():

	def peek():

	def 

