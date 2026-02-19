import pandas as pd
import pyodbc as db
import  json

class SQL():
    def __init__(self):
        
        driver="ODBC Driver 17 for SQL Server"
        server="DESKTOP-89FLHRU"
        database="BD_AVISOL"
        self.Cadena="Driver={0};server={1};database={2};Trusted_Connection=yes"\
            .format(driver,server,database)
    
    def listarJSON(self,consulta):
        cn= db.connect(self.Cadena)
        df=pd.read_sql_query(consulta,cn)
        data=df.to_json(orient="records")
        return json.loads(data)
    
    def enviarTransaccion(self,consulta):
        try:
            cn=db.connect(self.Cadena)
            cursor=cn.cursor()
            cursor.execute("SET NOCOUNT ON;"+consulta)
            registrosAfectados=cursor.fetchval()
            cursor.commit()
            cn.close()
       
            return registrosAfectados
        except Exception as error:
            registrosAfectados="Error "+str(error)
        return registrosAfectados


