from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import MasterService
from Entity.mstDepartmentEntity import mstDepartment
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
from Entity.DTO import Input
from Entity.DTO.Input import Listinginput,DeleteInput,ItemAddEditInput
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
async def DeleteAccount(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstAccount_DeletByID","DeleteAccount")
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
async def DeleteBank(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstAccount_DeletByID","DeleteBank")
    return result.__dict__

@Master.post('/GetBrandListing', dependencies=[Depends(jwtBearer())])
async def GetBrandListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstBrand_GetForlisting","GetBrandListing")
    return result.__dict__

@Master.post('/AddEditBrand', dependencies=[Depends(jwtBearer())])
async def AddEditBrand(input:Input.BrandAddEditInput):
    result= MasterService.AddEditBrand(input)
    return result.__dict__

@Master.post('/DeleteBrand', dependencies=[Depends(jwtBearer())])
async def DeleteBrand(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstBrand_DeleteByID","DeleteBrand")
    return result.__dict__

@Master.post('/GetProductListing', dependencies=[Depends(jwtBearer())])
async def GetProductListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstProduct_GetForlisting","GetProductListing")
    return result.__dict__

@Master.post('/AddEditProduct', dependencies=[Depends(jwtBearer())])
async def AddEditProduct():
    result= MasterService.AddEditProduct()
    return result.__dict__

@Master.post('/DeleteProduct', dependencies=[Depends(jwtBearer())])
async def DeleteProduct(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstProduct_DeleteByID","DeleteProduct")
    return result.__dict__

@Master.post('/GetStyleListing', dependencies=[Depends(jwtBearer())])
async def GetStyleListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstStyle_GetForlisting","GetStyleListing")
    return result.__dict__

@Master.post('/AddEditStyle', dependencies=[Depends(jwtBearer())])
async def AddEditStyle(input:Input.StyleAddEditInput):
    result= MasterService.AddEditStyle(input)
    return result.__dict__

@Master.post('/DeleteStyle', dependencies=[Depends(jwtBearer())])
async def DeleteStyle(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstStyle_DeleteByID","DeleteStyle")
    return result.__dict__

@Master.post('/GetItemGroupListing', dependencies=[Depends(jwtBearer())])
async def GetItemGroupListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstItemGroup_GetForlisting","GetItemGroupListing")
    return result.__dict__

@Master.post('/AddEditItemGroup', dependencies=[Depends(jwtBearer())])
async def AddEditItemGroup(input:Input.ItemGroupAddEditInput):
    result= MasterService.AddEditItemGroup(input)
    return result.__dict__

@Master.post('/DeleteItemGroup', dependencies=[Depends(jwtBearer())])
async def DeleteItemGroup(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstItemGroup_DeleteByID","DeleteItemGroup")
    return result.__dict__

@Master.post('/GetItemListing', dependencies=[Depends(jwtBearer())])
async def GetItemListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstItem_GetForlisting","GetItemListing")
    return result.__dict__

@Master.post('/AddEditItem', dependencies=[Depends(jwtBearer())])
async def AddEditItem(input:Input.ItemAddEditInput):
    result= MasterService.AddEditItem(input)
    return result

@Master.post('/DeleteItem', dependencies=[Depends(jwtBearer())])
async def DeleteItem(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstItem_DeleteByID","DeleteItem")
    return result.__dict__

@Master.post('/GetDesignListing', dependencies=[Depends(jwtBearer())])
async def Listing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstDesign_GetForlisting","GetDesignListing")
    return result.__dict__

@Master.post('/AddEditDesign', dependencies=[Depends(jwtBearer())])
async def AddEditDesign():
    result= MasterService.AddEditDesign()
    return result.__dict__

@Master.post('/DeleteDesign', dependencies=[Depends(jwtBearer())])
async def DeleteDesign(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstDesign_DeleteByID","DeleteDesign")
    return result.__dict__

@Master.post('/GetColorListing', dependencies=[Depends(jwtBearer())])
async def GetColorListing(input:Listinginput):
    result= MasterService.commanListingService(input,"WE_mstColor_GetForlisting","GetColorListing")
    return result.__dict__

@Master.post('/AddEditColor', dependencies=[Depends(jwtBearer())])
async def AddEditColor():
    result= MasterService.AddEditColor()
    return result.__dict__

@Master.post('/DeleteColor', dependencies=[Depends(jwtBearer())])
async def DeleteColor(input:DeleteInput):
    result= MasterService.commanDeleteService(input,"WE_mstColor_DeleteByID","DeleteColor")
    return result.__dict__

@Master.post('/AddEditItemAddEditInput')
async def DeleteColor(input:ItemAddEditInput):
    return input