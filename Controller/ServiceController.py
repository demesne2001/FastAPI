import time
import jwt
from decouple import config



JWT_KEY=config("secret")
JWT_ALGO=config("algorithm")

def token_response(token:str):
    return{
        "acsess token":token
    }

def signJWT(userID:str):
    payload={
        "userID":userID,
        "expiry":time.time()+600
    }
    token=jwt.encode(payload,JWT_KEY,algorithm=JWT_ALGO)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decode_token=jwt.decode(token,JWT_KEY,algorithm=JWT_ALGO)
        return decode_token if decode_token['expires']>=time.time() else None
    except:
        return{}