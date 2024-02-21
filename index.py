import uvicorn
from fastapi import FastAPI,Body,Depends
from os import path
from Controller import mstDepartmentController
from Controller.ServiceController import signJWT
from fastapi.middleware.cors import CORSMiddleware
from Entity.DTO.CommanResult import UserLoginSchema,UserSchema
from Controller.servicebearercontroller import jwtBearer

app=FastAPI()

users=[]
app.include_router(mstDepartmentController.Department,prefix='/Department')

origins=['*']

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

@app.post("/",dependencies=[Depends(jwtBearer())])
def Demo():
    return{"msg":"Welcome to Fast"}

@app.post("/login")
def login(data:UserLoginSchema=Body(default=None)):
    if checkuser(data):
         return signJWT(data.email)
    else:
        return {
                "Error":"Data is not Found"
            }
       

@app.post("/register")
def register(data:UserSchema=Body(default=None)):
    users.append(data)
    return signJWT(data.email)

def checkuser(data:UserLoginSchema):
    print(users)
    for user in users:
        if user.email==data.email and user.password==data.password:
             return True
        else:
            return False

if __name__ == "__main__":
#     import sys
#     sys.path.append(path.join(path.dirname(__file__),'..'))
     uvicorn.run(app, host="127.0.0.1", port=8000)
