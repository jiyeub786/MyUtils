import mariadb
import sys
from app.database import ConnectionConfig as config
from app.module.logger import logger

conStringDict = config.MYSQL_CONNECTION_STRING

def getMariaDBCon():
    try:
    # Connect to MariaDB Platform
        con = mariadb.connect(
            user=conStringDict["user"],
            password=conStringDict["password"],
            host=conStringDict["host"],
            port=conStringDict["port"],
            database=conStringDict["database"]
        )
        # Disable Auto-Commit
        con.autocommit = False
        return con

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def getMariaDBCursor(con):
    try:
        cur = con.cursor()
    except mariadb.Error as e:
        print(f"getMariaDBCursor Error: {e}")
    return cur

def closeMariaDBCon(cur):
    try:
        cur.close()
    except mariadb.Error as e:
        print(f"closeMariaDBCon Error: {e}")

def getMariaDBqueryResult(cur,query):
    try:
        cur = cur.execute(query)
        return 0

    except mariadb.Error as e:
        #print(f"getMariaDBqueryResult Error: {e}")
        return 1
        #logger.info(f"getMariaDBqueryResult Error: {e}" + query)




