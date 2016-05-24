from bitarray import bitarray
from global_data import PHOTO_AMOUNT

photo_bit_array = bitarray(PHOTO_AMOUNT)

def photo_seen(photo_id):
	return photo_bit_array[photo_id]

def add_photo(photo_id):
	photo_bit_array[photo_id] = 1

def clear_all():
	photo_bit_array.setall(False)