from enum import Enum

class CarModels(Enum):
	CITY = '1'
	COROLLA = '2'
	CRV = '3'
	YARIS = '4'

	@classmethod
	def choices(cls):
		return [(i.value, i.name) for i in cls]

class Manufacturer(Enum):
	HONDA = '1'

	@classmethod
	def choices(cls):
		return [(i.value, i.name) for i in cls]

class Colour(Enum):
	WHITE = '1'
	BLACK = '2'
	BLUE = '3'
	SILVER = '4'

	@classmethod
	def choices(cls):
		return [(i.value, i.name) for i in cls]