#assume there exists a Queue class with the following methods
#add
#remove
#peek
#isEmpty

#assume there is an isCat and isDog methods


class Shelter:
	def __init__(self):
		self.dogs = Queue()
		self.cats = Queue()
		self.counter = 0

	def addPet(pet):
		if isCat(pet):
			self.cats.add((pet, self.counter))

		elif isDog(pet):
			self.dogs.add((pet, self.counter))

		else:
			raise Exception('attempted to add pet that is neither dog nor cat')

		self.counter+=1

	def dequeueAny():


		#if both are non empty pop the older one
		if not self.dogs.isEmpty() and not self.cats.isEmpty():
			(dog,dog_age) = self.dogs.peek()
			(cat,cat_age) = self.cats.peek()

			if dog_age < cat_age:
				self.dogs.pop()
				return dog
			elif cat_age < dog_age:
				self.cats.pop()
				return cat


		#if cats is non empty pop cat
		elif not self.cats.isEmpty():
			(cat, _) = self.cats.pop()
			return cat

		#if dogs is non empty pop dog
		elif not self.dogs.isEmpty():
			(dog, _) = self.dogs.pop()
			return dog

		raise Exception('no pets in shelter')

		#raise exception no pets in shelter

	def dequeueDog():
		if not self.dogs.isEmpty():
			(dog, _) = self.dogs.pop()
			return dog

		raise Exception('no dog in shelter')


	def dequeueCat():
		if not self.cats.isEmpty():
			(cat, _) = self.cats.pop()
			return cat
		else:
			raise Exception('no cats in shelter')

