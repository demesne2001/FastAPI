from pydantic import BaseModel

class mstDepartment(BaseModel):
    DepartmentID:int
    DepartmentName:str
    IsActive:bool

