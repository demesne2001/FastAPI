from Entity import Result,mstDepartmentEntity
from DAL import mstDepartmentSQL
from utility import pythonCommanLibrary

def GetList():
    result=Result.ListingResult()
    result.LstDepartMent=mstDepartmentSQL.Listing()
    print(result)
    return result

def AddEdit(input:mstDepartmentEntity):
    result=Result.AddEditResult()
    # if(pythonCommanLibrary.IsNullOREmpty(input.mstDepartment.DepartmentName)):
    #     result.Message.append("Required Field DepartmentName")
    if(len(result.Message)==0):
        try:
            id=mstDepartmentSQL.AddEdit(input)
            if (id>0):
                result.Message.append("DepartMent Added")
            else:
                result.Message.append("Failed")  
        except:
            result.Message.append("Failed")
            result.HasError=True
    else:
        result.HasError=True
    return result

def Delete(ID):
    result=Result.AddEditResult()
    if(ID<=0):
        result.Message.append("Enter Valid ID")
    if(len(result.Message)==0):
        try:
            id=mstDepartmentSQL.delete(ID)
            if (id>0):
                result.Message.append("DepartMent deleted")
            else:
                result.Message.append("Failed") 
                result.HasError=True
        except:
            result.HasError=True
    else:
        result.HasError=True   
    return result

def GetFilter(mode:int,DepartmentID:int,DepartmentName:str):
    result=Result.ListingResult()
    if(mode<=0):
        result.Message.append("Mode is Required Field")
    elif(mode ==1):
        if(DepartmentID<=0):
            result.Message.append("DepartmentID is Required Field")
    if(len(result.Message)==0):
        try:
            result.LstDepartMent=mstDepartmentSQL.Search(mode,DepartmentID,DepartmentName)
        except :
            result.HasError=True
    else:
        result.HasError=True
    return result
