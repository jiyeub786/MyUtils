import cx_Oracle
import os
from app.module import logger
from app.database import ConnectionConfig as config

#os.environ["NLS_LANG"] = ".AL32UTF8"
#os.putenv('NLS_LANG','KOREAN_KOREA.KO16MSWIN949')
os.putenv('NLS_LANG','AMERICAN_AMERICA.AL32UTF8')


conString = config.ORACLE_CONNECTION_STRING
class Oracle():
    def __init__(self):
        try:
            self.con = cx_Oracle.connect(conString)
           # print("Oracle version:", self.con.version)
        except cx_Oracle.Error as e:
            print(f"oracle __init__ Error: {e}")

    def close(self):
        try:
            self.con.close()
        except cx_Oracle.Error as e:
            print(f"oracle close Error: {e}")

    def select(self, query):
        try:
            cur = self.con.cursor()
            cur.execute(query)
        except cx_Oracle.Error as e:
            print(f"oracle getCursor Error: {e}")
        return cur

    def insert(self,query,bindval):
        try:
            cur = self.con.cursor()
            cur.execute(query,bindval)
        except cx_Oracle.Error as e:
            print(f"oracle insert Error: {e}")
        return cur


    def insertmany(self,query,bindval):
        cur = self.con.cursor()
        cur.executemany(query,bindval)

    def update(self,query,bindval):
        try:
            cur = self.con.cursor()
            cur.execute(query,bindval)
        except cx_Oracle.Error as e:
            print(f"oracle update Error: {e}")
        return cur

    def commit(self):
        try:
            self.con.commit()
        except cx_Oracle.Error as e:
            print(f"commit Error: {e}")
