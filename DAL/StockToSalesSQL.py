from utility import DBConfig
import pyodbc 
from Entity.DTO.Input import StockSales


def BIrpt_StockAgainSales_GetRPT(input:StockSales):
    key_value_pairs=[]
    param=''
    print('connectionstring',DBConfig.WRconnection)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        if(len(input.FromDate) > 0):
            param +=f" @FromDate='{input.FromDate}',"
        if(len(input.ToDate)> 0):
            param +=f" @ToDate='{input.ToDate}',"
        if(len(input.strBranchID) > 0):
            param +=f" @strBranchID='{input.strBranchID}',"
        if(len(input.strCompanyID) > 0):
            param +=f" @strCompanyID='{input.strCompanyID}',"
        if(len(input.strItemGroupID) > 0):
            param +=f" @strItemGroupID='{input.strItemGroupID}',"
        if(len(input.strItemID) > 0):
            param +=f" @strItemID='{input.strItemID}',"
        if(len(input.Unit) > 0):
            param +=f" @Unit='{input.Unit}',"
        if(len(input.TotalRow)> 0):
            param +=f" @TotalRow='{input.TotalRow}',"
        param +=f"@PrintGroupBy ='{input.PrintGroupBy}'"
        print(len(input.ToDate))
        cursor=connection.cursor()
        print('SQL Statement',f"EXEC WR_BIrpt_StockAgainSales_StockToSales {param}")
        cursor.execute(f"EXEC WR_BIrpt_StockAgainSales_StockToSales {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
        connection.close()
        print(e)
        
    print(key_value_pairs)
    return key_value_pairs

   