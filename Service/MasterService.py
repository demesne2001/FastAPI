from utility import DBConfig
from Entity.DTO.Input import Listinginput
from Entity.Result import CommonListingResult

def commanListingService(input:Listinginput,SpName:str,MethodName:str):
    result=CommonListingResult()
    if(input.PageNo<=0):
        result.Message.append("PageNo Required Field")
    elif(input.Pagesize<=0):
        result.Message.append("Pagesize Required Field")
    if(result.Message.count()<=0):
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        param +=f" @Search='{input.Search}'"     
        result.lstResult=DBConfig.ExecuteDataReader(param,SpName,MethodName)
    else :
        result.HasError=True
    return result
    