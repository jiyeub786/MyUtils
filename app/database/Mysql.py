import mariadb
import sys
from app.database import ConnectionConfig as config

conStringDict = config.MYSQL_CONNECTION_STRING

class Mysql():
    def __init__(self):
        try:
            # Connect to MariaDB Platform
            self.con = mariadb.connect(
                            user=conStringDict["user"],
                            password=conStringDict["password"],
                            host=conStringDict["host"],
                            port=conStringDict["port"],
                            database=conStringDict["database"]
            )
            # Disable Auto-Commit
            self.con.autocommit = False

        except mariadb.Error as e:
            print(f"Mysql __init__: {e}")
            sys.exit(1)

    def close(self):
        try:
            self.con.close()
        except mariadb.Error as e:
            print(f"Mysql close Error: {e}")

    def select(self,query):
        try:
            cur = self.con.cursor().execute(query)

        except mariadb.Error as e:
            print(f"Mysql select Error: {e}")

        return cur

    def insertmany(self, query,bindval):
        cur = self.con.cursor()
        cur.executemany(query, bindval)

        #
        # try:
        #     cur = self.con.cursor()
        #     cur.executemany(query,bindval)
        #     return 0
        #
        # except mariadb.Error as e:
        #     print(f"Mysql insert Error: {e}")
        #     return 1



    def commit(self):
        try:
            self.con.commit
        except mariadb.Error as e:
            print(f"Mysql commit Error: {e}")
