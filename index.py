import uvicorn
from fastapi import FastAPI
from Controller.mstDepartmentController import Department
app=FastAPI()

app.include_router(Department,prefix='/Department')

@app.get("/")
def Demo():
    return{"msg":"Welcome to Fast"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
