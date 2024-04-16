from pydantic import BaseModel,Field, StrictInt
from datetime import date
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
    
class VoucherNoInput(BaseModel):
    CompanyID:int | None= Field(default=1)
    BranchID:int | None= Field(default=1)
    CompanyUnitID:int | None= Field(default=1)
    FinYearID:int | None= Field(default=7)
    DaybookID:int| None= Field(default=401)
    TranType:str| None= Field(default='A')
    TableName:str| None= Field(default='trnSales')
    VoucherDate:str| None= Field(default=str(date.today()))
    VoucherNo:str| None= Field(default='')
    
class SalesAddEditInput(BaseModel):
    pass

class CustomerSearch(BaseModel):
    Mobile1:str

class DepartmentAddEditInput(BaseModel):
    DepartmentID:int
    DepartmentName:str
    IsActive:bool

class GetByID(BaseModel):
    ID:int

class ItemAddEditInput(BaseModel):
    ItemID:int
    DepartmentID:int
    BrandID:int | None= Field(default=0)
    ProductID:int
    StyleID:int
    ItemGroupID:int | None= Field(default=0)
    ItemName:str
    ShortName:str
    BarcodeType:str
    DefaultQty:float| None= Field(default=0)
    IsActive:bool
    TaxID:int| None= Field(default=0)
    DiscPrc:float| None= Field(default=0)
    SalesmanCommPrc:float| None= Field(default=0)
    MarkUpPrc:float| None= Field(default=0)
    MarkDownPrc:float| None= Field(default=0)
    SalesMarkUpPrc:float| None= Field(default=0)
    SalesMarkDownPrc:float| None= Field(default=0)
    MesrUnitCode:str| None= Field(default='')
    ItemType:str| None= Field(default='')
    BarcodeShortcut:str | None= Field(default='')
    TranType:str| None= Field(default='A')
    HSNCode:str | None= Field(default='')
    LabourRate:float| None= Field(default=0)
    MesrSalesRate:float | None= Field(default=0)
    SubProcessIDs:str | None= Field(default='')
    SalesmanCommType:str | None= Field(default='P')
    SalesmanCommAmount:float| None= Field(default=0)
    MRPROF:int| None= Field(default=0)
    TaxSlabID:int| None= Field(default=0)
    EyesMesrType:str| None= Field(default='')
    DoNotShowInGarmentDealApp:bool
    

class ItemGroupAddEditInput(BaseModel):
    ItemGroupID:int
    ItemGroupName:str
    ShortName:str
    IsActive:bool

class StyleAddEditInput(BaseModel):
    StyleID:int
    StyleName:str
    ShortName:str
    IsActive:bool

class BrandAddEditInput(BaseModel):
    BrandID:int
    BrandName:str
    ShortName:str
    IsActive:bool

class DesignAddEditInput(BaseModel):
    pass

class salesAddEdit(BaseModel):
    pass

class SalesItemAddEdit(BaseModel):
    pass