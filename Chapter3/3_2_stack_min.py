

class Min_stack_node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.min_val = float('inf')

	def set_next(self,next):
		self.next = next

	def set_min(self, min_val):
		self.min_val = min_val

	def get_min(self):
		return self.min_val

	def get_data(self):
		return self.data


class Min_stack:
	def __init__(self):
		self.top = None

	def push(self, data):
		node = Min_stack_node(data)

		#case where stack is non empty prior to push
		if self.top:
			new_min_val = min(self.top.get_min(), data)

			node.set_min(new_min_val)


		#case where stack is empty prior to push
		else:
			node.set_min(data)


		#put node on stack
		node.set_next(self.top)
		self.top = node



	def pop(self):
		if not self.top:
			raise Exception('Attempted to pop from empty stack')

		else:
			popped_value = self.top.get_data()

			self.top = self.top.next

			return popped_value


	def get_min(self):

		if not self.top:
			raise Exception('Attempted to get min value from empty stack')

		else:
			return self.top.get_min()


import random

def test_stack():
	s = Min_stack()

	values = [random.randint(1,9) for _ in range(10)]
	print(values)



	for v in values:
		s.push(v)

	for _ in range(len(values)):
		print(s.get_min())
		s.pop()


test_stack()


