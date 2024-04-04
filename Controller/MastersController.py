from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import MasterService
from Entity.mstDepartmentEntity import mstDepartment
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
from Entity.DTO.Input import Listinginput
import base64
Master=APIRouter()


@Master.post('/GetAccountListing', dependencies=[Depends(jwtBearer())])
async def GetAccountListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstAccount_GetListing","GetAccountListing")
    return result.__dict__

@Master.post('/AddEditAccount', dependencies=[Depends(jwtBearer())])
async def AddEditAccount():
    result= MasterService.AddEditAccount()
    return result.__dict__

@Master.post('/DeleteAccount', dependencies=[Depends(jwtBearer())])
async def DeleteAccount():
    result= MasterService.DeleteAccount()
    return result.__dict__

@Master.post('/GetBankListing', dependencies=[Depends(jwtBearer())])
async def GetBankListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstAccount_GetListing","GetBankListing")
    return result.__dict__

@Master.post('/AddEditBank', dependencies=[Depends(jwtBearer())])
async def AddEditBank():
    result= MasterService.AddEditBank()
    return result.__dict__

@Master.post('/DeleteBank', dependencies=[Depends(jwtBearer())])
async def DeleteBank():
    result= MasterService.DeleteBank()
    return result.__dict__

@Master.post('/GetBrandListing', dependencies=[Depends(jwtBearer())])
async def GetBrandListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstBrand_GetForlisting","GetBrandListing")
    return result.__dict__

@Master.post('/AddEditBrand', dependencies=[Depends(jwtBearer())])
async def AddEditBrand():
    result= MasterService.AddEditBrand()
    return result.__dict__

@Master.post('/DeleteBrand', dependencies=[Depends(jwtBearer())])
async def DeleteBrand():
    result= MasterService.DeleteBrand()
    return result.__dict__

@Master.post('/GetProductListing', dependencies=[Depends(jwtBearer())])
async def GetProductListing():
    result= MasterService.commanListingService(input,"WE_mstProduct_GetForlisting","GetProductListing")
    return result.__dict__

@Master.post('/AddEditProduct', dependencies=[Depends(jwtBearer())])
async def AddEditProduct():
    result= MasterService.AddEditProduct()
    return result.__dict__

@Master.post('/DeleteProduct', dependencies=[Depends(jwtBearer())])
async def DeleteProduct():
    result= MasterService.DeleteProduct()
    return result.__dict__

@Master.post('/GetStyleListing', dependencies=[Depends(jwtBearer())])
async def GetStyleListing():
    result= MasterService.commanListingService(input,"WE_mstStyle_GetForlisting","GetStyleListing")
    return result.__dict__

@Master.post('/AddEditStyle', dependencies=[Depends(jwtBearer())])
async def AddEditStyle():
    result= MasterService.AddEditStyle()
    return result.__dict__

@Master.post('/DeleteStyle', dependencies=[Depends(jwtBearer())])
async def DeleteStyle():
    result= MasterService.DeleteStyle()
    return result.__dict__

@Master.post('/GetItemGroupListing', dependencies=[Depends(jwtBearer())])
async def GetItemGroupListing():
    result= MasterService.commanListingService(input,"WE_mstItemGroup_GetForlisting","GetItemGroupListing")
    return result.__dict__

@Master.post('/AddEditItemGroup', dependencies=[Depends(jwtBearer())])
async def AddEditItemGroup():
    result= MasterService.AddEditItemGroup()
    return result.__dict__

@Master.post('/DeleteItemGroup', dependencies=[Depends(jwtBearer())])
async def DeleteItemGroup():
    result= MasterService.DeleteItemGroup()
    return result.__dict__

@Master.post('/GetItemListing', dependencies=[Depends(jwtBearer())])
async def GetItemListing():
    result= MasterService.commanListingService(input,"WE_mstItem_GetForlisting","GetItemListing")
    return result.__dict__

@Master.post('/AddEditItem', dependencies=[Depends(jwtBearer())])
async def AddEditItem():
    result= MasterService.AddEditItem()
    return result.__dict__

@Master.post('/DeleteItem', dependencies=[Depends(jwtBearer())])
async def DeleteItem():
    result= MasterService.DeleteItem()
    return result.__dict__

@Master.post('/GetDesignListing', dependencies=[Depends(jwtBearer())])
async def Listing():
    result= MasterService.commanListingService(input,"WE_mstDesign_GetForlisting","GetDesignListing")
    return result.__dict__

@Master.post('/AddEditDesign', dependencies=[Depends(jwtBearer())])
async def AddEditDesign():
    result= MasterService.AddEditDesign()
    return result.__dict__

@Master.post('/DeleteDesign', dependencies=[Depends(jwtBearer())])
async def DeleteDesign():
    result= MasterService.DeleteDesign()
    return result.__dict__

@Master.post('/GetColorListing', dependencies=[Depends(jwtBearer())])
async def GetColorListing():
    result= MasterService.commanListingService(input,"WE_mstColor_GetForlisting","GetColorListing")
    return result.__dict__

@Master.post('/AddEditColor', dependencies=[Depends(jwtBearer())])
async def AddEditColor():
    result= MasterService.AddEditColor()
    return result.__dict__

@Master.post('/DeleteColor', dependencies=[Depends(jwtBearer())])
async def DeleteAccount():
    result= MasterService.DeleteColor()
    return result.__dict__
