from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import mstDepartmentService
from Entity.mstDepartmentEntity import mstDepartment
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
import base64
Department=APIRouter()

@Department.post('/GetDepartmentList', dependencies=[Depends(jwtBearer())])
async def Listing():
    result= mstDepartmentService.GetList()
    return result.__dict__
IMAGEDIR="image/"
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

@Department.post('/uploadfile/')
async def Create_upload_file(file:UploadFile=File(...)):
    file.filename=f"ImageNAme.jpg"
    contents=await file.read()
    
    with open(F"{IMAGEDIR}{file.filename}","wb") as f:
        f.write(contents)
    return {'filename':file.filename}

@Department.post('/uploadfileBase64')
async def Create_upload(input:UploadFile):   
    data_split = input.Base64.split('base64,')
    encoded_data = data_split[1]
    path=Path(F"{IMAGEDIR}ImageNAme1{input.Email}.jpg") 
    print("Path",path)   
    data = base64.b64decode(encoded_data)
    with open(F"{IMAGEDIR}ImageNAme1{input.Email}.jpg","wb") as f:
        f.write(data)
    return {'filename':path}