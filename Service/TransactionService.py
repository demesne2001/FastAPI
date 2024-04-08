from utility import DBConfig
from Entity.DTO.Input import SalesListingInput,DeleteInput
from Entity.Result import CommonListingResult,CommonDeleteResult

def trnSaleslisting(input:SalesListingInput):
    Result=CommonListingResult()
    if(input.PageNo<=0):
        Result.Message.append("PageNo")
    elif(input.Pagesize<=0):
        Result.Message.append("Pagesize")
    if(len(Result.Message)==0):
        param="" 
        if(input.CompanyID>0):            
            param +=f" @CompanyID={input.CompanyID},"
        if(input.FinYearID>0):            
            param +=f" @FinYearID={input.FinYearID},"
        if(input.CompanyUnitID>0):            
            param +=f" @CompanyUnitID={input.CompanyUnitID},"
        if(input.FromDaybookID>0):            
            param +=f" @FromDaybookID={input.FromDaybookID},"
        if(input.ToDaybookID>0):            
            param +=f" @ToDaybookID={input.ToDaybookID},"
        if(input.TranType !=""):            
            param +=f" @TranType='{input.TranType}',"
        if(input.VoucherNo !=""):            
            param +=f" @VoucherNo='{input.VoucherNo}',"
        if(input.VoucherFromDate !=""):            
            param +=f" @VoucherFromDate='{input.VoucherFromDate}',"
        if(input.VoucherToDate !=""):            
            param +=f" @VoucherToDate='{input.VoucherToDate}',"
        if(input.SalesType !=""):            
            param +=f" @SalesType='{input.SalesType}',"
        if(input.EntryFormType !=""):            
            param +=f" @EntryFormType='{input.EntryFormType}',"
        if(input.CommaSeperate_CounterID !=""):            
            param +=f" @CommaSeperate_CounterID='{input.CommaSeperate_CounterID}',"
        if(input.strBranchID !=""):            
            param +=f" @strBranchID='{input.strBranchID}',"
        if(input.DefaultSalesTypeSR !=""):            
            param +=f" @DefaultSalesTypeSR='{input.DefaultSalesTypeSR}',"         
        param +=f" @PageSize={input.Pagesize},"
        param +=f" @PageNo={input.PageNo}"
        Result=DBConfig.ExecuteDataReaderWithResult(param,"WE_trnSales_GetListing","trnSaleslisting",Result)
    else:
        Result.HasError=True
    return Result        