# import pyodbc


server='192.168.2.252'
database='GRetail_Extreme'
username='Garment'
password='Garment'


connection = (
    f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;')

# print("DB Connected")



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