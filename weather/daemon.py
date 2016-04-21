def main():
	from classes.request import Request
	from classes.data import Data

	import sys
	from datetime import datetime
	import time

	try:
		lat = sys.argv[1]
		lon = sys.argv[2]
	except:
		# Default NYC coordinates.
		lat = 40
		lon = -74

	req = Request(lat=lat, lon=lon)

	print "Uploading coordinates.."

	while True:
		now = datetime.now()
		hour = now.hour
		minute = now.minute

		if not hour % 3 and not minute:
			# If 0, 3, 6, 9, 12 hours and 0 minute

			res = req.get_json_by_coords()

			data = Data(json=res)
			data.parse_json()

			print data.get_needed_data()

		else:
			print "Waiting for next data.."

		time.sleep(60)


if __name__ == '__main__':
	main()