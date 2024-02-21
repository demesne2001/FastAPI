from pydantic import BaseModel,Field

class CommanResult:
    def __init__(self):
        self.Message = []
        self.HasError = False
        
class UserSchema(BaseModel):
    fullname:str = Field(default=None)
    email:str= Field(default=None)
    password:str= Field(default=None)
    class congif:
        the_demo={
            "Demo":{
                "fullname":"om",
                "email":"patelom109@gmail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    email:str= Field(default=None)
    password:str= Field(default=None)
    class congif:
        the_demo={
            "Demo":{
                "email":"patelom109@gmail.com",
                "password":"123"
            }
        }