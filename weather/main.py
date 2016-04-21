def main():
	from classes.request import Request
	from classes.data import Data

	import sys

	name = sys.argv[1]

	req = Request(name=name)

	json = req.get_json_by_name()

	d = Data(json)
	d.parse_json()
	print d.get_needed_data()


if __name__ == '__main__':
	main()