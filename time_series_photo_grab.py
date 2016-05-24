import time
import threading

from pop_photo_grab import PhotoStream
from global_data import PHOTO_GRAB_INTERVAL, PHOTO_CATEGORIES

class TimeSeriesPhotoGrabber(object):
	def __init__(self):
		pass

	#photo processing is assigned with a new thread, avoid interferring with API requests 
	def _async_photo_processing(self):
		#start downloading photo stream
		for cat in PHOTO_CATEGORIES:
			ps = PhotoStream()
			photo_list = ps.request_pop_photo_stream(cat, 0)
			located_photos = ps.get_located_photos(photo_list, cat)
			if len(located_photos) > 0:
				ps.save_photo_stream_to_db(located_photos, cat)

#core function of the time series photo grabbing
def start_looping():
	pg = TimeSeriesPhotoGrabber()
#	intervals = 0
	while True:
		count = 0
		pg._async_photo_processing()
		time.sleep(PHOTO_GRAB_INTERVAL)
#		intervals += 1

#		if intervals >= 2:
#			break


