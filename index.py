import uvicorn
from fastapi import FastAPI,Body,Depends
from os import path
from Controller import mstDepartmentController,StockToSalesController,MastersController,TransactionController
from Controller.ServiceController import signJWT
from fastapi.middleware.cors import CORSMiddleware
from Entity.DTO.CommanResult import UserLoginSchema,UserSchema
from Controller.servicebearercontroller import jwtBearer
from utility.Logger import logger
from fastapi.staticfiles import StaticFiles
app=FastAPI()
logger.info('Start APi Log')

users=[]
defauluser=UserSchema(fullname='om', email='om@gmail.com', password='12345')
users.append(defauluser)
app.include_router(mstDepartmentController.Department,prefix='/Department')
app.include_router(StockToSalesController.StockToSales,prefix='/StockToSales')
app.include_router(MastersController.Master,prefix='/Master')
app.include_router(TransactionController.Transaction,prefix='/Transaction')
origins=['*']

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

@app.post("/", dependencies=[Depends(jwtBearer())])
def Demo():
    return{"msg":"Welcome to Fast"}

@app.post("/login")
def login(data:UserLoginSchema=Body(default=None)):
    print('req',data)
    print('userarr',users)
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
    print(len(users))
    
    coun=0
    for user in users:
        coun+=1
        print(coun)
        print(user)
        print(data)
        if user.email==data.email and user.password==data.password:
             return True
        elif len(users)==coun:
            return False
       

if __name__ == "__main__":
#     import sys
#     sys.path.append(path.join(path.dirname(__file__),'..'))
     uvicorn.run(app, host="127.0.0.1", port=8000)
