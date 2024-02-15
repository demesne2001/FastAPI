import uvicorn
from fastapi import FastAPI
from os import path
from Controller import mstDepartmentController
app=FastAPI()

app.include_router(mstDepartmentController.Department,prefix='/Department')

@app.get("/")
def Demo():
    return{"msg":"Welcome to Fast"}

if __name__ == "__main__":
#     import sys
#     sys.path.append(path.join(path.dirname(__file__),'..'))
    

     uvicorn.run(app, host="127.0.0.1", port=8000)
