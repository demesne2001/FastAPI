from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import MasterService
from Entity.mstDepartmentEntity import mstDepartment
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
import base64
Master=APIRouter()


@Master.post('/GetAccountListing', dependencies=[Depends(jwtBearer())])
async def GetAccountListing():
    result= MasterService.commanListingService(input,"WE_mstAccount_GetListing","GetAccountListing")
    return result.__dict__

@Master.post('/AddEditAccount', dependencies=[Depends(jwtBearer())])
async def AddEditAccount():
    result= mstDepartmentService.AddEditAccount()
    return result.__dict__

@Master.post('/DeleteAccount', dependencies=[Depends(jwtBearer())])
async def DeleteAccount():
    result= mstDepartmentService.DeleteAccount()
    return result.__dict__

@Master.post('/GetBankListing', dependencies=[Depends(jwtBearer())])
async def GetBankListing():
    result= MasterService.commanListingService(input,"WE_mstAccount_GetListing","GetBankListing")
    return result.__dict__

@Master.post('/AddEditBank', dependencies=[Depends(jwtBearer())])
async def AddEditBank():
    result= mstDepartmentService.AddEditBank()
    return result.__dict__

@Master.post('/DeleteBank', dependencies=[Depends(jwtBearer())])
async def DeleteBank():
    result= mstDepartmentService.DeleteBank()
    return result.__dict__

@Master.post('/GetBrandListing', dependencies=[Depends(jwtBearer())])
async def GetBrandListing():
    result= mstDepartmentService.commanListingService(input,"","GetBrandListing")
    return result.__dict__

@Master.post('/AddEditBrand', dependencies=[Depends(jwtBearer())])
async def AddEditBrand():
    result= mstDepartmentService.AddEditBrand()
    return result.__dict__

@Master.post('/DeleteBrand', dependencies=[Depends(jwtBearer())])
async def DeleteBrand():
    result= mstDepartmentService.DeleteBrand()
    return result.__dict__

@Master.post('/GetProductListing', dependencies=[Depends(jwtBearer())])
async def GetProductListing():
    result= mstDepartmentService.commanListingService(input,"","GetProductListing")
    return result.__dict__

@Master.post('/AddEditProduct', dependencies=[Depends(jwtBearer())])
async def AddEditProduct():
    result= mstDepartmentService.AddEditProduct()
    return result.__dict__

@Master.post('/DeleteProduct', dependencies=[Depends(jwtBearer())])
async def DeleteProduct():
    result= mstDepartmentService.DeleteProduct()
    return result.__dict__

@Master.post('/GetStyleListing', dependencies=[Depends(jwtBearer())])
async def GetStyleListing():
    result= mstDepartmentService.commanListingService(input,"","GetStyleListing")
    return result.__dict__

@Master.post('/AddEditStyle', dependencies=[Depends(jwtBearer())])
async def AddEditStyle():
    result= mstDepartmentService.AddEditStyle()
    return result.__dict__

@Master.post('/DeleteStyle', dependencies=[Depends(jwtBearer())])
async def DeleteStyle():
    result= mstDepartmentService.DeleteStyle()
    return result.__dict__

@Master.post('/GetItemGroupListing', dependencies=[Depends(jwtBearer())])
async def GetItemGroupListing():
    result= mstDepartmentService.commanListingService(input,"","GetItemGroupListing")
    return result.__dict__

@Master.post('/AddEditItemGroup', dependencies=[Depends(jwtBearer())])
async def AddEditItemGroup():
    result= mstDepartmentService.AddEditItemGroup()
    return result.__dict__

@Master.post('/DeleteItemGroup', dependencies=[Depends(jwtBearer())])
async def DeleteItemGroup():
    result= mstDepartmentService.DeleteItemGroup()
    return result.__dict__

@Master.post('/GetItemListing', dependencies=[Depends(jwtBearer())])
async def GetItemListing():
    result= mstDepartmentService.commanListingService(input,"","GetItemListing")
    return result.__dict__

@Master.post('/AddEditItem', dependencies=[Depends(jwtBearer())])
async def AddEditItem():
    result= mstDepartmentService.AddEditItem()
    return result.__dict__

@Master.post('/DeleteItem', dependencies=[Depends(jwtBearer())])
async def DeleteItem():
    result= mstDepartmentService.DeleteItem()
    return result.__dict__

@Master.post('/GetDesignListing', dependencies=[Depends(jwtBearer())])
async def Listing():
    result= mstDepartmentService.commanListingService(input,"","GetDesignListing")
    return result.__dict__

@Master.post('/AddEditDesign', dependencies=[Depends(jwtBearer())])
async def AddEditDesign():
    result= mstDepartmentService.AddEditDesign()
    return result.__dict__

@Master.post('/DeleteDesign', dependencies=[Depends(jwtBearer())])
async def DeleteDesign():
    result= mstDepartmentService.DeleteDesign()
    return result.__dict__

@Master.post('/GetColorListing', dependencies=[Depends(jwtBearer())])
async def GetColorListing():
    result= mstDepartmentService.commanListingService(input,"","GetColorListing")
    return result.__dict__

@Master.post('/AddEditColor', dependencies=[Depends(jwtBearer())])
async def AddEditColor():
    result= mstDepartmentService.AddEditColor()
    return result.__dict__

@Master.post('/DeleteColor', dependencies=[Depends(jwtBearer())])
async def DeleteAccount():
    result= mstDepartmentService.DeleteColor()
    return result.__dict__
