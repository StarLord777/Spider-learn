


import pymongo

conn = pymongo.MongoClient(host='192.168.1.7')

db = conn['myblog']
db.create_collection('test')
print(db.collection_names())
test = db['test']

test.insert({1:'5445546'})