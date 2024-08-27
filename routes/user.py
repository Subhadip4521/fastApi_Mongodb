from fastapi import APIRouter  # type: ignore
from bson import ObjectId # type: ignore

from models.user import User
from config.db import collection
from schemas.user import serializeDict, serializeList

user = APIRouter()

@user.get("/")
async def find_all_users():
    return serializeList(collection.find())


@user.get("/{id}")
async def find_one_users(id):
    return serializeDict(collection.find_one({"_id": ObjectId(id)}))


@user.post("/")
async def create_users(user: User):
    collection.insert_one(dict(user))
    return serializeList(collection.find())


@user.put("/{id}")
async def update_users(id, user: User):
    collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return serializeDict(collection.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
async def delete_users(id):
    return serializeDict(
        collection.find_one_and_delete({"_id": ObjectId(id)})
    )
