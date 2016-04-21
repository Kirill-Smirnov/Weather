import sys
sys.path.append('../classes')
from data import Data

def main():
	s = '{"coord":{"lon":138.93,"lat":34.97},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"base":"cmc stations","main":{"temp":288.655,"pressure":1028.6,"humidity":100,"temp_min":288.655,"temp_max":288.655,"sea_level":1038.23,"grnd_level":1028.6},"wind":{"speed":3.12,"deg":222.5},"clouds":{"all":44},"dt":1461155698,"sys":{"message":0.0038,"country":"JP","sunrise":1461096333,"sunset":1461144068},"id":1851632,"name":"Shuzenji","cod":200}'
	d = Data(s)

	d.parse_json()

	print d.get_needed_data()


if __name__ == '__main__':
	main()