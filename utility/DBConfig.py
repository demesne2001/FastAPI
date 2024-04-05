import pyodbc

server='192.168.1.241,20017'
database='GRetailExtreme_ANYBODY'
username='Garment'
password='Garment'

serverj='192.168.1.241,2017'
databasej='JsoftWhExtreme_Tableau_ForWebReport'
usernamej='Garment'
passwordj='Garment'

WRserver='110.227.251.94,25672'
WRatabase='JsoftWhExtreme_Tableau_ForWebReport'
WRsername='Garment'
WRassword='AlpNV@123'

server1='192.168.2.252'
database1='GRetail_Extreme'
username1='Garment'
password1='Garment'

connection = (
    f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')

# connection = (
#     f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')

jconnection = (
    f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={serverj};DATABASE={databasej};UID={usernamej};PWD={passwordj};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')

# connection = (
#     f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server1};DATABASE={database1};UID={username1};PWD={password1};')

WRconnection = (
    f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={WRatabase};UID={username};PWD={password};')

def execute_stored_procedure(connection_string,procedure_name,*params):
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    try:
        cursor.execute(f"EXEC {procedure_name} {', '.join('?' for _ in params)}", params)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        key_value_pairs=[]
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        return key_value_pairs
    finally:
        cursor.close()
        connection.close()

def ExecuteDataReader(param,spname,MethodNname):    
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]    
    wconnection=pyodbc.connect(connection)
    try:
        cursor=wconnection.cursor()        
        cursor.execute(f"EXEC {spname} {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()    
        print(rows)    
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        print(key_value_pairs)
        cursor.close()        
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
    finally:
        wconnection.close()
    return key_value_pairs

def ExcuteNonQuery(param,spname,MethodNname,Result):
    result=""
    ExceptionREsult=None
    drivers = [item for item in pyodbc.drivers()]    
    wconnection=pyodbc.connect(connection)
    cursor=wconnection.cursor()   
    try:
        print(f"EXEC {spname} {param}")
        cursor.execute(f"EXEC {spname} {param}")
        cursor.commit()
        result="Transaction Comapleted Successfully"
    except Exception as e:
        ExceptionREsult=e
        # print(MethodNname + 'Error :- ',e)
        # print('SQL Query',f"EXEC {spname} {param}")
        # print('driver',drivers)
           #    Result.Message=ExecuteDataReader()
        result=f"Error ModuleName:{MethodNname},SPName:{spname},Param:{param},Error:{e}"
        print(e)
        Result.HasError=True
        cursor.rollback()        
    finally:
        cursor.close()
        wconnection.close()
    wconnection2=pyodbc.connect(connection)
    cursor2=wconnection2.cursor()
    try:
        constrain=str(ExceptionREsult).split("REFERENCE constraint")
        constrain=constrain[1].split('"')
        table=str(ExceptionREsult).split("table")
        table=table[1].split(",")
        
        
        if(str(ExceptionREsult).find("column")>=0):
            print('condition')
            coloumn=str(ExceptionREsult).split("column")
            coloumn=coloumn[1].split("\'")       
            coloumn=coloumn[1].split("\\") 
        else:
            coloumn=str(spname).split("mst")      
            coloumn=coloumn[1].split("_")
            coloumn=coloumn[0]+"ID"
        print('colou',coloumn)
        ID=str(param).split(",")
        ID=ID[0].split("=")
        if(constrain[1]!=""):
            print(constrain[1],'Constraint')
        else:
            print('check',constrain[0])
        if(table[0]!=''):
            print(table[0],'table')
        if(coloumn[0]!=''):
            print(coloumn[0],'column')
      
        # print('ID',ID[1])
        if(constrain[0]!="" and table[0]!="" and coloumn[0]!=""):           
           key_value_pairs=[]          
           Exparam=F"@FK_Name='{constrain[1]}',@FieldValue={ID[1]},@FieldName='{coloumn[0]}'"
        
           cursor2.execute(f"ExeC util_GetForeignReferenceUsingFK {Exparam}")
           columns = [column[0] for column in cursor2.description]
           rows = cursor2.fetchall()
           while (cursor2.nextset()):
            print('Condition true')
                
            Nexttable=cursor2.fetchall()
            count=0      
            columns2 = [column[0] for column in cursor2.description]            
            for Item in Nexttable:
               count+=1
               if(count<31):
                print(dict(zip(columns2, Item)))
                key_value_pairs.append(dict(zip(columns2, Item)))        
               else:
                break
            Result.Message.append(key_value_pairs)
        #    print(key_value_pairs)           
    except  Exception as e:
          print(F"Delete Dal Eroor:{e}")
    finally:
        cursor2.close()     
        wconnection2.close()  
    return Result