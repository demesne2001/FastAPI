import uvicorn
from fastapi import FastAPI
from os import path
from Controller import mstDepartmentController
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()


app.include_router(mstDepartmentController.Department,prefix='/Department')

origins=['*']

app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

@app.get("/")
def Demo():
    return{"msg":"Welcome to Fast"}

if __name__ == "__main__":
#     import sys
#     sys.path.append(path.join(path.dirname(__file__),'..'))
     uvicorn.run(app, host="127.0.0.1", port=8000)
