import cx_Oracle
import os
from app.database import ConnectionConfig as config

import platform
#os.environ["NLS_LANG"] = ".AL32UTF8"
#os.putenv('NLS_LANG','KOREAN_KOREA.KO16MSWIN949')
os.putenv('NLS_LANG','AMERICAN_AMERICA.AL32UTF8')

conString = config.ORACLE_CONNECTION_STRING

def getOracleDBCon():
    print(platform.architecture())


    try:
        con = cx_Oracle.connect(conString)
        return con
    except cx_Oracle.Error as e:
        print(f"getOracleDBCon Error: {e}")

def closeOracleDBcon(con):
    try:
        con.close()
    except cx_Oracle.Error as e:
        print(f"closeOracleDBcon Error: {e}")

