from pydantic import BaseModel
class StockSales(BaseModel):
    FromDate:str
    ToDate:str
    TotalRow:str
    strCompanyID:str
    strBranchID:str
    strItemGroupID:str
    strItemID:str
    Unit:str
    PrintGroupBy :str