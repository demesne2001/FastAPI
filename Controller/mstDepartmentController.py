from fastapi import APIRouter,Body,Depends
from Service import mstDepartmentService
from Entity.mstDepartmentEntity import mstDepartment
from Controller.servicebearercontroller import jwtBearer
Department=APIRouter()

@Department.post('/GetDepartmentList', dependencies=[Depends(jwtBearer())])
async def Listing():
    result= mstDepartmentService.GetList()
    return result.__dict__

@Department.post('/GetSearchDepartMent', dependencies=[Depends(jwtBearer())])
async def Listing(mode:int,DepartmentID:int=None,DepartmentName:str=None):
    result= mstDepartmentService.GetFilter(mode,DepartmentID,DepartmentName)
    return result.__dict__

@Department.post('/AddEditDepartMent', dependencies=[Depends(jwtBearer())])
async def Listing(input:mstDepartment):
    result= mstDepartmentService.AddEdit(input)
    return result.__dict__

@Department.post('/DeleteDepartMentByID', dependencies=[Depends(jwtBearer())])
async def Listing(ID:int):
    result= mstDepartmentService.Delete(ID)
    return result.__dict__