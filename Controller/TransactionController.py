from fastapi import APIRouter,Body,Depends,File,UploadFile
from Service import TransactionService
# from Entity.mstDepartmentEntity import 
from Entity.DTO.Input import UploadFile
from Controller.servicebearercontroller import jwtBearer
from pathlib import Path
from Entity.DTO.Input import SalesListingInput
import base64
Transaction=APIRouter()


@Transaction.post('/GetSalesListing', dependencies=[Depends(jwtBearer())])
async def GetAccountListing(input:SalesListingInput):
    result= TransactionService.trnSaleslisting(input)
    return result.__dict__