
def IsNullOREmpty(string:str):
    if(string==''):
        return True
    elif(len(string)==0):
        return True
    elif(string == 'Null'):
        return True
    else:
        return False