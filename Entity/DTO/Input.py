from pydantic import BaseModel,Field
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
    CompanyID:int | None= Field(default=1)
    FinYearID:int | None= Field(default=7)
    TranType:str| None= Field(default='A')
    VoucherNo:str| None= Field(default="")
    VoucherFromDate:str | None= Field(default="2024-04-01")
    VoucherToDate:str | None= Field(default="")
    SalesType:str | None= Field(default="SALE")
    EntryFormType:str | None= Field(default="SALE")    
    PageNo:int
    Pagesize:int
    AccountID:int | None= Field(default=0)
    CompanyUnitID:int | None= Field(default=1)
    FromDaybookID:int| None= Field(default=401)
    ToDaybookID:int| None= Field(default=420)
    CommaSeperate_CounterID:str | None= Field(default="")
    strBranchID:str | None= Field(default="1")
    DefaultSalesTypeSR:str | None= Field(default="S")