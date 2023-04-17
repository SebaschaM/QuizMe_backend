import time

from bcrypt import hashpw, checkpw, gensalt
from config.connDB import *
from utils.toDict import object_as_dict


user_collection = db['user']


def insertUser(user):
    user["password"] = hashpw(user["password"].encode(
        "utf-8"), gensalt()).decode("utf-8")
    user["isConfirmed"] = False
    user["keyConfirm"] = int(round(time.time() * 1000))
    user["createdAt"] = time.time()
    user_collection.insert_one(user)


def getUserByEmail(email, isLogin):
    user = user_collection.find_one({"email": email})
    if user:
        user.pop("fullname")
    user = object_as_dict(user)
    return user


def getUser(id):
    user = user_collection.find_one({"id": id})
    if user:
        user.pop("password")
    user = object_as_dict(user)
    return user
