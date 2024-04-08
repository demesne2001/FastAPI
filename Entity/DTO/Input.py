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
    
class BarcodeHelpInput(BaseModel):
    CompanyID:int | None= Field(default=1)
    ItemID:int | None= Field(default=0)
    DesignID:int | None= Field(default=0)
    ColorID:int | None= Field(default=0)
    BrandID:int | None= Field(default=0)
    BranchID:int | None= Field(default=1)
    CompanyUnitID:int | None= Field(default=1)
    TranType:str| None= Field(default='A')
    CompanyBarcode:str| None= Field(default='')
    Size1:str| None= Field(default='')
    search:str| None= Field(default='')
    ABStock:bool | None= Field(default=True)
    AllStock:bool | None= Field(default=False)
    PageNo:int
    Pagesize:int
    
class SalesManHelpInput(BaseModel):
    strCompanyID:str| None= Field(default='')
    strBranchID:str| None= Field(default='')
    search:str| None= Field(default='')
    PageNo:int
    Pagesize:int