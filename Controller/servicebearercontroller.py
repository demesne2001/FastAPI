from typing_extensions import Annotated
from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from .ServiceController import decodeJWT
import time
import jwt
from decouple import config

JWT_KEY=config("secret")
JWT_ALGO=config("algorithm")

class jwtBearer(HTTPBearer):
    def __init__(self,auto_error: bool = True):
        super(jwtBearer,self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) :
        credentails: HTTPAuthorizationCredentials=await super(jwtBearer,self).__call__(request)
        if credentails:
            print('First Condition')
            print(credentails.scheme)
            if not credentails.scheme=="Bearer":                
                raise HTTPException(status_code=403,detail="Invalid or Expired Token ..!")
            if  (jwtBearer.verify_jwt(credentails.credentials)== False):
                raise HTTPException(status_code=403,detail="Invalid or Expired Token ..!")
            return credentails.credentials
        else:
            print('First Condition false')
            raise HTTPException(status_code=403,detail="Invalid or Expired Token ..!")
    
    def verify_jwt(jwtToken:str):
        print(jwtToken)
        isTokenValid:bool=False
        payload=decodeJWT(jwtToken)
        # decode_token=jwt.decode(jwtToken,JWT_KEY,algorithm=JWT_ALGO)
        # print(decode_token)
        # if decode_token['expiry']>=time.time():
        #     payload=decode_token
        # else:
        #     payload="om"
        # print('payload',payload)
        if payload:
            isTokenValid=True
        print(isTokenValid)
        return isTokenValid
