#!/usr/bin/python3

"""this is a file that contains storage class"""
import json


class FileStorage():
	"""Class for saving data in a json file"""

	__file_path = 'file.json'
	__objects = {}
	
	def all(self):
		"""returns objects"""
		return self.__objects
	
	def new(self, obj):
		"""sets a new object in __objects"""
		self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
	
	def save(self):
		"""serializes __objects to the JSON file"""
		with open(self.__file_path, 'w') as File:		
			json.dump(self.__objects, File, default=str)

	def reload(self):
		"""deserializes the JSON file to __objects"""
		try:
			with open(self.__file_path, 'r') as file:
				self.__objects = json.load(file)
		except Exception:
			pass
	

