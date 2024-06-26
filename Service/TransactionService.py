from utility import DBConfig
from Entity.DTO.Input import SalesListingInput,DeleteInput,BarcodeHelpInput,SalesManHelpInput,VoucherNoInput
from Entity.DTO import Input
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

def GetBarcodeHelp(input:BarcodeHelpInput):
    Result=CommonListingResult()
    if(input.PageNo<=0):
        Result.Message.append("PageNo")
    elif(input.Pagesize<=0):
        Result.Message.append("Pagesize")
    if(len(Result.Message)==0):
        param="" 
        if(input.CompanyID>0):            
            param +=f" @CompanyID={input.CompanyID},"
        if(input.ItemID>0):            
            param +=f" @ItemID={input.ItemID},"
        if(input.CompanyUnitID>0):            
            param +=f" @CompanyUnitID={input.CompanyUnitID},"
        if(input.DesignID>0):            
            param +=f" @DesignID={input.DesignID},"
        if(input.ColorID>0):            
            param +=f" @ColorID={input.ColorID},"
        if(input.TranType !=""):            
            param +=f" @TranType='{input.TranType}',"
        if(input.Size1 !=""):            
            param +=f" @Size1='{input.Size1}',"
        if(input.search !=""):            
            param +=f" @search='{input.search}',"
        if(input.CompanyBarcode !=""):            
            param +=f" @CompanyBarcode='{input.CompanyBarcode}',"      
        if(input.BrandID >0):            
            param +=f" @BrandID={input.BrandID},"    
        if(input.BranchID >0):            
            param +=f" @BranchID={input.BranchID},"             
        param +=f" @PageSize={input.Pagesize},"
        param +=f" @ABStock={input.ABStock},"
        param +=f" @AllStock={input.AllStock},"
        param +=f" @PageNo={input.PageNo}"
        Result=DBConfig.ExecuteDataReaderWithResult(param,"WE_trnStock_GetBarcodeStockHelp","GetBarcodeHelp",Result)
    else:
        Result.HasError=True
    return Result        


def GetSalesmanHelp(input:SalesManHelpInput): 
    Result=CommonListingResult()
    if(input.PageNo<=0):
        Result.Message.append("PageNo")
    elif(input.Pagesize<=0):
        Result.Message.append("Pagesize")
    if(len(Result.Message)==0):
        param="" 
        if(input.search !=""):            
            param +=f" @search='{input.search}',"
        if(input.strBranchID !=""):            
            param +=f" @strBranchID='{input.strBranchID}',"
        if(input.strCompanyID !=""):            
            param +=f" @strCompanyID='{input.strCompanyID}',"
        param +=f" @PageSize={input.Pagesize},"
        param +=f" @PageNo={input.PageNo}"
        Result=DBConfig.ExecuteDataReaderWithResult(param,"WR_mstSalesman_GetForHelp","GetSalesmanHelp",Result)
    else:
        Result.HasError=True
    return Result  

def GetVoucherNo(input:VoucherNoInput): 
    Result=CommonListingResult()   
    if(len(Result.Message)==0):
        param="" 
        if(input.CompanyID>0):            
            param +=f" @CompanyID={input.CompanyID},"
        if(input.BranchID >0):            
            param +=f" @BranchID={input.BranchID},"  
        if(input.FinYearID>0):            
            param +=f" @FinYearID={input.FinYearID},"   
        if(input.VoucherDate !=""):            
            param +=f" @VoucherDate='{input.VoucherDate}',"
        if(input.VoucherNo !=""):            
            param +=f" @VoucherNo='{input.VoucherNo}',"
        if(input.TranType !=""):            
            param +=f" @TranType='{input.TranType}',"
        if(input.TableName !=""):            
            param +=f" @TableName='{input.TableName}',"
        if(input.DaybookID>0):            
            param +=f" @DaybookID={input.DaybookID},"
        if(input.CompanyUnitID>0):            
            param +=f" @CompanyUnitID={input.CompanyUnitID}"
        Result=DBConfig.ExecuteDataReaderWithResult(param,"WE_trnGetVoucherNoMissing","GetVoucherNo",Result)
    else:
        Result.HasError=True
    return Result  

def GetCustomerDetailByMobileNo(input:Input.CustomerSearch):
    result=CommonListingResult()
    try:
        param=''
        param=DBConfig.spParam(input)
        result=DBConfig.ExecuteDataReaderWithResult(param,"WE_mstAccount_GetForAccountUC","GetCustomerDetailByMobileNo",result)
    except Exception as e:
        result.HasError=True
        result.Message.append(str(e))
    return result