from Entity.DTO import CommanResult

class ListingResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        self.LstDepartMent=[]
        


class AddEditResult(CommanResult.CommanResult):
    def __init__(self):
        super().__init__()
        pass


