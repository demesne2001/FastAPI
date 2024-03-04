from fastapi import APIRouter,Body,Depends
from Service import StockToSalesService
from Entity.DTO.Input import StockSales
from Controller.servicebearercontroller import jwtBearer
StockToSales=APIRouter()

@StockToSales.post('/GetStockToSales', dependencies=[Depends(jwtBearer())])
async def Listing(input:StockSales):
    result= StockToSalesService.StockToSales(input)
    return result.__dict__