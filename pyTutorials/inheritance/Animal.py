class Animal:
	"""Represents an Animal"""
	def __init__(self, birthType, appearance, blooded):
		self.birthType = birthType
		self.appearance = appearance
		self.blooded = blooded

	@property
	def birthType(self):
		return self.__birthType

	@birthType.setter
	def birthType(self, birthType):
		self.__birthType = birthType

	@property
	def appearance(self):
		return self.__appearance

	@appearance.setter
	def appearance(self, appearance):
		self.__appearance = appearance

	@property
	def blooded(self):
		return self.__blooded

	@blooded.setter
	def blooded(self, blooded):
		self.__blooded = blooded
	
	def __str__(self):
		return ("A {} is {} and it is {}.".format(self.birthType, self.appearance, self.blooded))

class Mammal(Animal):
	"""Represents a Mammal, which is a type of an Animal"""
	def __init__(self, birthType, appearance, blooded, nurseYoung):
		Animal.__init__(self, birthType, appearance, blooded)
		self.__nurseYoung = nurseYoung

	@property
	def nurseYoung(self):
		return self.__nurseYoung

	@nurseYoung.setter
	def nurseYoung(self, nurseYoung):
		self.__nurseYoung = nurseYoung

	def __str__ (self):
		return super().__str__() + " and it is {} that they nurse their young.".format(self.nurseYoung)

class Reptile(Animal):
	"""Represents a Reptile, which is a type of Animal """
	def __init__(self, birthType, appearance, blooded, nurseYoung):
		Animal.__init__(self, birthType, appearance, blooded)
		self.nurseYoung = nurseYoung

	@property
	def nurseYoung(self):
		return self.__nurseYoung

	@nurseYoung.setter
	def nurseYoung(self, nurseYoung):
		self.__nurseYoung = nurseYoung

	def __str__(self):
		return super().__str__() + " and it is {} that they nurse their young.".format(self.nurseYoung)

def main():
	animal1 = Animal("Born Alive", "Has hair and fur", "Warm-blooded")
	print(animal1.appearance)
	print(animal1.birthType)
	print(animal1.blooded)
	print(animal1.__str__())
