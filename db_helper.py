import pymongo

connection = pymongo.MongoClient('localhost', 27017, maxPoolSize=10)
mydb = connection.px
