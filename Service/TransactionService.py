from utility import DBConfig
from Entity.DTO.Input import SalesListingInput,DeleteInput
from Entity.Result import CommonListingResult,CommonDeleteResult

def trnSaleslisting(input:SalesListingInput):
    Result=CommonListingResult()
    if(input.PageNo<=0):
        Result.Message.append("PageNo")
    elif(input.Pagesize<=0):
        Result.Message.append("Pagesize")