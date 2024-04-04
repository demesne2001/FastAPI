from utility import DBConfig
from Entity.DTO.Input import Listinginput
from Entity.Result import CommonListingResult

def commanListingService(input:Listinginput,SpName:str,MethodName:str):
    result=CommonListingResult()
    print('input',input)
    if(input.PageNo<=0):
        result.Message.append("PageNo Required Field")
    elif(input.Pagesize<=0):
        result.Message.append("Pagesize Required Field")
    print(len(result.Message))
    if(len(result.Message)==0):
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.Pagesize>0):
            param +=f" @PageSize={input.Pagesize},"
        param +=f" @Search='{input.Search}'"  
        print(param)   
        result.lstResult=DBConfig.ExecuteDataReader(param,SpName,MethodName)
    else :
        result.HasError=True
    return result

def commanDeleteService(input:Listinginput,SpName:str,MethodName:str):
    result=CommonListingResult()
    print('input',input)
    if(input.PageNo<=0):
        result.Message.append("PageNo Required Field")
    elif(input.Pagesize<=0):
        result.Message.append("Pagesize Required Field")
    print(len(result.Message))
    if(len(result.Message)==0):
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.Pagesize>0):
            param +=f" @PageSize={input.Pagesize},"
        param +=f" @Search='{input.Search}'"  
        print(param)   
        result.lstResult=DBConfig.ExecuteDataReader(param,SpName,MethodName)
    else :
        result.HasError=True
    return result
    