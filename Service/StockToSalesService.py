from Entity.DTO.Input import StockSales
from Entity.Result import StockToSalesResult
from DAL.StockToSalesSQL import BIrpt_StockAgainSales_GetRPT


def StockToSales(input:StockSales):
    Result=StockToSalesResult()
    print(len(input.PrintGroupBy))
    if(len(input.PrintGroupBy)==0):
        Result.Message.append("Required Field PrintGroupBy")
    if(len(Result.Message)==0):
        try:
            Result.lstResult=BIrpt_StockAgainSales_GetRPT(input)
        except Exception as e:
            Result.HasError=True
            print(e)
            Result.Message.append(e)
    else:
        Result.HasError=True
    return Result