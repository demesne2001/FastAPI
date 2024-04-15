from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import TransactionService
# from Entity.mstDepartmentEntity import 
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
from Entity.DTO.Input import SalesListingInput,BarcodeHelpInput,SalesManHelpInput,VoucherNoInput
from Entity.DTO import Input
import base64
Transaction=APIRouter()


@Transaction.post('/GetSalesListing', dependencies=[Depends(jwtBearer())])
async def GetSalesListing(input:SalesListingInput):
    result= TransactionService.trnSaleslisting(input)
    return result.__dict__

@Transaction.post('/GetBarcodeHelp', dependencies=[Depends(jwtBearer())])
async def GetBarcodeHelp(input:BarcodeHelpInput):
    result= TransactionService.GetBarcodeHelp(input)
    return result.__dict__

@Transaction.post('/GetSalesmanHelp', dependencies=[Depends(jwtBearer())])
async def GetSalesmanHelp(input:SalesManHelpInput):
    result= TransactionService.GetSalesmanHelp(input)
    return result.__dict__

@Transaction.post('/GetVoucherNo', dependencies=[Depends(jwtBearer())])
async def GetVoucherNo(input:VoucherNoInput):
    result= TransactionService.GetVoucherNo(input)
    return result.__dict__

@Transaction.post('/GetCustomerDetailByMobileNo', dependencies=[Depends(jwtBearer())])
async def GetCustomerDetailByMobileNo(input:Input.CustomerSearch):
    result= TransactionService.GetCustomerDetailByMobileNo(input)
    return result.__dict__