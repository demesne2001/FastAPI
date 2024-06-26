from utility import DBConfig
from Entity.DTO.Input import Listinginput,DeleteInput
from Entity.DTO import Input
from Entity import Result
import pyodbc
from Entity.Result import CommonListingResult,CommonDeleteResult,CommanAddEditResult

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

def AddEditBrand(input:Input.BrandAddEditInput):
    result=CommanAddEditResult()
    ID=0
    ID=DBConfig.ExecuteAddEdit(input,"WE_mstBrand_AddEdit","AddEditBrand")
    if(ID>0):
        result.Message.append("Brand Added Sucessfully")
    elif(ID ==-1):
       result.Message.append("Brand Name AlReady Exists") 
       result.HasError=True
    elif(ID ==-2):
       result.Message.append("BrandShortName AlReady Exists") 
       result.HasError=True
    return result
    


def AddEditItem(input:Input.ItemAddEditInput):
    result=CommanAddEditResult()   
    if(input.BarcodeType == ""):
        result.Message.append("BarcodeType Req")
    elif(input.ItemName == ""):
        result.Message.append("ItemName Req")    
    elif(input.DepartmentID <= 0):
        result.Message.append("DepartmentID Req")
    if(len(result.Message)==0):        
        ID=0
        ID=DBConfig.ExecuteAddEdit(input,"WE_mstItem_AddEdit","AddEditItem")
        if(ID>0):
            result.Message.append("Item Added Sucessfully")
        elif(ID ==-1):
           result.Message.append("Item Name AlReady Exists") 
           result.HasError=True
        elif(ID ==-2):
           result.Message.append("Item ShortName AlReady Exists") 
           result.HasError=True
        elif(ID ==-3):
           result.Message.append("Item BarcodeShorCut AlReady Exists") 
           result.HasError=True
    else:
        result.HasError=True
    return result

def AddEditStyle(input:Input.StyleAddEditInput):
    result=CommanAddEditResult()
    ID=0
    ID=DBConfig.ExecuteAddEdit(input,"WE_mstStyle_AddEdit","AddEditStyle")
    if(ID>0):
        result.Message.append("Style Added Sucessfully")
    elif(ID ==-1):
       result.Message.append("Style Name AlReady Exists") 
       result.HasError=True
    elif(ID ==-2):
       result.Message.append("StyleShortName AlReady Exists") 
       result.HasError=True
    return result

def AddEditItemGroup(input:Input.ItemGroupAddEditInput):
    result=CommanAddEditResult()
    ID=0
    ID=DBConfig.ExecuteAddEdit(input,"WE_mstItemGroup_AddEdit","AddEditStyle")
    if(ID>0):
        result.Message.append("ItemGroup Added Sucessfully")
    elif(ID ==-1):
       result.Message.append("ItemGroup Name AlReady Exists") 
       result.HasError=True
    elif(ID ==-2):
       result.Message.append("ItemGroup ShortName AlReady Exists") 
       result.HasError=True
    return result

def GetItemByID(input:Input.GetByID):
    result=Result.ItemGetByIDResult()
    if(input.ID<=0):
        result.Message.append("ItemID Required")
    if(len(result.Message)==0):
        
        Connection=pyodbc.connect(DBConfig.connection)
        cursor = Connection.cursor()
        try:
            cursor.execute(f"EXEC WE_mstItem_GetByID @ID={input.ID}")
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall() 
            for row in rows:
                result.lstResult.append(dict(zip(columns, row)))
            while (cursor.nextset()):
                Nexttable=cursor.fetchall()
                count=0      
                columns2 = [column[0] for column in cursor.description]            
                for Item in Nexttable: 
                    result.lstHsnCode.append(dict(zip(columns2, Item)))  
            
        except Exception as e:
            result.Message.append(e)
            result.HasError=True
        finally:
            cursor.close()
            Connection.close()
    else:
        result.HasError=True
    return result

def CommanGetByID(input:Input.GetByID,SPName:str):
    result=Result.CommonListingResult()
    result.lstResult=DBConfig.ExecuteDataReader(F"@ID={input.ID}",SPName,"CommanGetByID")
    return result