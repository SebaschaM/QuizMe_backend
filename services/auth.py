import uuid
import time

from bcrypt import hashpw, checkpw, gensalt

from config.connDB import *

user_collection = db['user']


def insertUser(user):
    user["password"] = hashpw(
        user["password"].encode("utf-8"), gensalt()
    ).decode("utf-8")
    user["uid"] = str(uuid.uuid4())
    user["isConfirmed"] = False
    user["keyConfirm"] = int(round(time.time() * 1000))
    user["createdAt"] = time.time()
    user_collection.insert_one(user)
    newUser = user_collection.insert_one(user)
    return newUser


def getUserByEmail(email, isLogin):
    user = user_collection.find_one({"email": email})
    if user and isLogin:
        user.pop("password")
    return user
