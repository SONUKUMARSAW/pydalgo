# Implementation of arrays in python

class Array:

	def __init__(self,values):		
		"""Array takes a list or a tuple as parameter and creates a Array"""
		
		self.ls = []
		self.ls.extend(values)

	def append(self,element):
		"""Append element(s) to Array"""
		
		self.ls.extend(element)

	def insert(self,index,element):
		"""Insert element to the specified index"""
		
		tmp = self.ls[index:]
		self.ls=self.ls[:index]+[element]+tmp

	def pop(self,index=-1):
		"""Pop the element from the specified index/last element from the Array"""
		
		if index >= len(self.ls):
			raise Exception("Index out of bound")
		elif len(self.ls)==0:
			raise Exception("Array is empty")
		elif index!=-1 and index<len(self.ls)-2:
			tmp = self.ls[index]
			self.ls = self.ls[:index]+self.ls[index+1:]
			return tmp
		else:
			tmp = self.ls[-1]
			self.ls.pop()
			return tmp
			

	def remove(self,value):
		"""Remove the element if present in Array"""
		try:
			self.ls.remove(value)
		except ValueError:
			raise Exception("Element not found in Array")

	def index(self,value):
		"""Return the first occurence of element"""
		try:
			idx = self.ls.index(value)
			if idx:
				return idx
		except ValueError:
			raise Exception("Element not fount in Array")

	def reverse(self):
		"""Reverse the string"""
		self.ls.reverse()

	def __len__(self):
		return len(self.ls)

	def __repr__(self):
		pass

	def __str__(self):
		return '['+', '.join([str(x) for x in self.ls])+']'
