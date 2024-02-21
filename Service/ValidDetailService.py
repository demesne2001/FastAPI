from typing_extensions import Annotated, Doc
from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from .ValidService import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self,auto_error: bool = True):
        super(jwtBearer,self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) :
        credentails: HTTPAuthorizationCredentials=await super(jwtBearer,self).__call__(request)
        if credentails:
            print('First Condition')
            if not credentails.scheme=="Bearer":
                raise HTTPException(status_code=403,detail="Invalid or Expired Token ..!")
            return credentails.credentials
        else:
            print('First Condition false')
            raise HTTPException(status_code=403,detail="Invalid or Expired Token ..!")
    
    def verify_jwt(self,jwtToken:str):
        isTokenValid:bool=False
        payload=decodeJWT(jwtToken)
        if payload:
            isTokenValid=True
        return isTokenValid