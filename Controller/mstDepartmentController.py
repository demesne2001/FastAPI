from fastapi import APIRouter
from Service import mstDepartmentService
from Entity.mstDepartmentEntity import mstDepartment
Department=APIRouter()

@Department.post('/GetDepartmentList')
async def Listing():
    result= mstDepartmentService.GetList()
    return result.__dict__

@Department.post('/GetSearchDepartMent')
async def Listing(mode:int,DepartmentID:int=None,DepartmentName:str=None):
    result= mstDepartmentService.GetFilter(mode,DepartmentID,DepartmentName)
    return result.__dict__

@Department.post('/AddEditDepartMent')
async def Listing(input:mstDepartment):
    result= mstDepartmentService.AddEdit(input)
    return result.__dict__

@Department.post('/DeleteDepartMentByID')
async def Listing(ID:int):
    result= mstDepartmentService.Delete(ID)
    return result.__dict__