from Entity.DTO import CommanResult

class ListingResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        self.LstDepartMent=[]
        


class AddEditResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        pass

class StockToSalesResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        self.lstResult=[]

class CommonListingResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        self.lstResult=[]


class CommonDeleteResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        
class CommanAddEditResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        
class ItemGetByIDResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        self.lstResult=[]
        self.lstHsnCode=[]