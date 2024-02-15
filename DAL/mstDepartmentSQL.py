from utility import DBConfig
# import pyodbc
from Entity.mstDepartmentEntity import mstDepartment
from datetime import datetime

def Listing():
    connection=pyodbc.connect(DBConfig.connection)
    cursor=connection.cursor()
    cursor.execute("EXEC ws_mstDesign_Demo")
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    print(rows)
    key_value_pairs=[]
    for row in rows:
        key_value_pairs.append(dict(zip(columns, row)))
    cursor.close()
    connection.close()

    print('========>',key_value_pairs)
    return key_value_pairs
    
def AddEdit(input:mstDepartment):
    connection=pyodbc.connect(DBConfig.connection)
    DatTime: datetime
    DatTime='2024-02-13'
    print(DatTime)
    cursor=connection.cursor()
    cursor.execute(f"exec mstDepartment_AddEdit '{input.DepartmentID}','{input.DepartmentName}','{input.IsActive}','{DatTime}',1,'{DatTime}',1")
    cursor.commit()
    connection.close()
    return 1
    
def delete(ID):
    connection=pyodbc.connect(DBConfig.connection)
    cursor=connection.cursor()
    cursor.execute(f"exec mstDepartment_Delete '{ID}',1")
    cursor.commit()
    connection.close()
    return 1

def Search(mode:int,DepartmentID:int,DepartmentName:str):
    connection=pyodbc.connect(DBConfig.connection)
    cursor=connection.cursor()
    
    if(DepartmentID == None):
        str(DepartmentID)
        DepartmentID=''
    elif(DepartmentID>0):
        pass

    if(DepartmentName ==  None):
        DepartmentName=''
    print('statement',f"EXEC mstDepartment_Search '{mode}','{DepartmentID}','{DepartmentName}'")
    cursor.execute(f"EXEC mstDepartment_Search '{mode}','{DepartmentID}','{DepartmentName}'")
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    print(rows)
    key_value_pairs=[]
    for row in rows:
        key_value_pairs.append(dict(zip(columns, row)))
    cursor.close()
    connection.close()
    print('========>',key_value_pairs)
    return key_value_pairs