
#assume there exists a Stack class w the following methods 
#pop
#push
#isEmpty
#len




class stack_stack:
	def __init__(self, max_size):
		self.max_size = max_size
		self.stack_list = []
		self.top_pointer = -1



	def push(self,data):

		if self.top_pointer == -1:
			self.stack_list.append(Stack())
			self.top_pointer+=1

		if len(self.stack_list[self.top_pointer]) == self.max_size:
			self.stack_list.append(Stack())
			self.top_pointer+=1


		self.stack_list[self.top_pointer].push(data)



	def pop(self):

		if self.top_pointer == -1:
			raise Exception('Attempted to pop from empty stack stack')

		popped_value = self.stack_list[self.top_pointer].pop()

		if self.stack_list[self.top_pointer].isEmpty():
			self.top_pointer-=1
			self.stack_list = self.stack_list[:-1]

		return popped_value


		



