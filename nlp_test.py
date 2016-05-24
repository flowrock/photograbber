from pop_photo_grab import PhotoStream
import json
from db_helper import mydb

ps = PhotoStream()
col = mydb.photos
photo_list = list(col.find().limit(10))
print len(photo_list)
ps.parse_photo_stream(photo_list,8)