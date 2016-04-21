# -*- coding: utf-8 -*-

class Temperature:
		def K_to_C(self, num):
			return num - 273

		def K_to_F(self, num):
			return num * 9/5 - 459.67

class Data:

	def __init__(self, json):
		self.json = json

	def parse_json(self):
		import json

		self.data = json.loads(self.json)

		return self.data

	def get_needed_data(self):
		temperature = Temperature()

		name = self.data["name"]

		temp_k = self.data["main"]["temp"]
		temp_c = temperature.K_to_C(temp_k )
		temp_f = temperature.K_to_F(temp_k )

		return "In %s is %s C or %s F" % (name, temp_c, temp_f)
