from utility import DBConfig
from Entity.DTO.Input import Listinginput,DeleteInput
from Entity.Result import CommonListingResult,CommonDeleteResult

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

def commanDeleteService(input:DeleteInput,SpName:str,MethodName:str):
    result=CommonDeleteResult()
    print('input',input)
    if(input.ID<=0):
        result.Message.append("ID Required Field") 
    # if(ValidatationSP !=""):
    #     result.DependentChild=DeleteValidation(input.ID,ValidatationSP)
    #     if(len(result.DependentChild)>0):
    #         result.HasError=True
    if(len(result.Message)==0 and result.HasError == False):
        param=""        
        param +=f" @ID={input.ID},@UserID=1"  
        print(param)   
        result=DBConfig.ExcuteNonQuery(param,SpName,MethodName,result)        
    else :
        result.HasError=True
    return result
    
def DeleteValidation(ID:int,SPName:str):
    lstResult=[]
    param=""
    if(input.ID>0):
        param +=f" @ID={ID}"
    lstResult=DBConfig.ExecuteDataReader(param,SPName,"")
    return lstResult