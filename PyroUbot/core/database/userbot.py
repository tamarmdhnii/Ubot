from PyroUbot import tomi_run
from PyroUbot.core.database import mongodb

ubotdb = mongodb.ubot

async def add_ubot(user_id, api_id, api_hash, session_string):
    encrypted_data = tomi_run.en(
        {
            "api_id": api_id,
            "api_hash": api_hash,
            "session_string": session_string,
        }
    )
    
    return await ubotdb.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "user_id": user_id,
                "encrypted_data": encrypted_data
            }
        },
        upsert=True,
    )

async def remove_ubot(user_id):
    return await ubotdb.delete_one({"user_id": user_id})

async def get_userbots():
    data = []
    async for ubot in ubotdb.find({"user_id": {"$exists": 1}}):
        decrypted_data = tomi_run.de(ubot["encrypted_data"])
        data.append(
            dict(
                name=str(ubot["user_id"]),
                api_id=decrypted_data["api_id"],
                api_hash=decrypted_data["api_hash"],
                session_string=decrypted_data["session_string"],
            )
        )
    return data
