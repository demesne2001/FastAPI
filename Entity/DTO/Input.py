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
    
class UploadFile(BaseModel):
    Base64:str
    Email:str
    
class Listinginput(BaseModel):
    PageNo:int
    Pagesize:int
    Search:str

class DeleteInput(BaseModel):
    ID:int

class DeleteValidation(BaseModel):
    ID:int

class SalesListingInput(BaseModel):
    CompanyID:int
    FinYearID:int
    TranType:str
    VoucherNo:str
    VoucherFromDate:str
    VoucherToDate:str
    SalesType:str
    EntryFormType:str
    CompanyID:int
    PageNo:int
    Pagesize:int
    AccountID:int
    CompanyUnitID:int
    FromDaybookID:int
    ToDaybookID:int
    CommaSeperate_CounterID:str
    strBranchID:str
    DefaultSalesTypeSR:str