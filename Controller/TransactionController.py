from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import TransactionService
# from Entity.mstDepartmentEntity import 
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
from Entity.DTO.Input import SalesListingInput,BarcodeHelpInput
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