from Entity import Result,mstDepartmentEntity
from DAL import mstDepartmentSQL


def GetList():
    result=Result.ListingResult()
    result.LstDepartMent=mstDepartmentSQL.Listing()
    print(result)
    return result

def AddEdit(input:mstDepartmentEntity):
    result=Result.AddEditResult()
    id=mstDepartmentSQL.AddEdit(input)
    if (id>0):
        result.Message.append("DepartMent Added")
    else:
        result.Message.append("Failed")    
    return result

def Delete(ID):
    result=Result.AddEditResult()
    id=mstDepartmentSQL.delete(ID)
    if (id>0):
        result.Message.append("DepartMent deleted")
    else:
        result.Message.append("Failed")    
    return result

def GetFilter(mode:int,DepartmentID:int,DepartmentName:str):
    result=Result.ListingResult()
    result.LstDepartMent=mstDepartmentSQL.Search(mode,DepartmentID,DepartmentName)
    return result