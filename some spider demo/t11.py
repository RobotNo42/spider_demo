import pymongo

# 获取连接mongo数据库连接
client = pymongo.MongoClient('122.51.194.106', port=27017)
# 获取数据库，没有数据库也没关系。会自己创建
db = client.messi
# 获取数据库中的集合也就是mysql的表
collection = db.test1
# 插入一条，使用insert_one方法，插入很多条，使用insert_many
# collection.insert_one({'count':12})
# 查找集合所有数据,使用find方法
# collection_find = collection.find()
# for c in collection_find:
#     print(c)
# 查找集合第一条数据,使用find_one方法，()里可以加过滤条件
# collection_find = collection.find_one()
# collection_find = collection.find_one({'count':12})
# 更新集合中的数据,使用update_one和updata_many方法
collection_find = collection.update_many({'age': '25'}, {'$set': {'job': 'jjjjj'}})
# print(collection_find)