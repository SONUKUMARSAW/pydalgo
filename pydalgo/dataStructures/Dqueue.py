


class Dequeue:
	""" doc string """
	def __init__(self,head=None):
		self.head = head
		self.ls = []

	def frontEnqueue(self,key):
		""" doc string """
		if self.head is None:
			self.head = key
		self.ls.append(self.head)

	def frontDequeue(self, key):
		""" doc string """
		if self.head is None:
			return "Queue is empty"
		else:
			return self.ls[0]
			self.ls.pop(0)

	def backEnqueue(self,key):
		"""doc string """
		pass

	def backDequeue(self,key):
		""" doc string """
		pass

	def topFront(self):
		""" doc string """
		return self.head

	def topBack(self):
		""" doc string """
		pass

	def isEmpty(self):
		""" doc string """
		return bool(self.ls)