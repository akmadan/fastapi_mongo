from fastapi import APIRouter
from models.user_model import User 
from schemas.user_schema import users_serializer
from bson import ObjectId
from config.db import collection

userRouter = APIRouter()

@userRouter.post('/')
async def create_user(user: User):
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status" : "Ok", "data": user}

@userRouter.get('/')
async def find_all_users():
    users = users_serializer(collection.find())
    return {"status": "Ok", "data": users}

@userRouter.get('/{id}')
async def find_user(id: str):
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}

@userRouter.put("/{id}")
async def update_user(id: str, user: User):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": dict(user)
        }
    )
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}

@userRouter.delete("/{id}")
async def delete_user(id: str): 
    collection.find_one_and_delete({"_id": ObjectId(id)})
    users = users_serializer(collection.find())
    return {"status": "Ok", "data": users}