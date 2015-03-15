import qPython
from pymongo import MongoClient

q = qconnection.QConnection(host = 'localhost', port = 5000, username = 'tu', password = 'secr3t', timeout = 3.0)
client = MongoClient(‘localhost’, 27017)
db = client['djnNews']

try:
    q.open()
    # ...
finally:
    q.close()

record = db.collection.find_one()
#record = db.collection.find({"date":"20140501",$text:{$search:"Google"}})

