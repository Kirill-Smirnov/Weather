APP_ID = '385c1dffb95d309758f0956f7e61c1d6'
URL = "http://api.openweathermap.org/data/2.5/weather"


import requests

class Request:
	def __init__(self, lat=None, lon=None, name=None):
		self.latitude = lat
		self.longitude = lon
		self.name = name

	def get_json_by_coords(self):
		params = {
			'lat': self.latitude,
			'lon': self.longitude,
			'appid': APP_ID
		}

		res = requests.get(url=URL, params=params)

		self.res = res.text.encode('ascii')

		return self.res

	def get_json_by_name(self):
		params = {
			'q': self.name,
			'appid': APP_ID
		}

		return requests.get(url=URL, params=params).text.encode('ascii')