
# # 에듀빌 운영 DB 커넥션
# EDUORACLE_HOST = "210.107.249.24:3310"
# EDUORACLE_SID = "EDUMACDB"
# EDUORACLE_ID = "EDUORACLE"
# EDUORACLE_PW = "ok0!LtSHaEi2DYtM#ak5x7oB9"
# EDUORACLE_CONNECTION = EDUORACLE_ID+"/"+EDUORACLE_PW+"@"+EDUORACLE_HOST+"/"+EDUORACLE_SID


DBMS_HOST = "localhost:1521"
DBMS_SID = "ORCL"
DBMS_ID = "workout"
DBMS_PW = "workout"
ORACLE_CONNECTION_STRING = DBMS_ID+"/"+DBMS_PW+"@"+DBMS_HOST+"/"+DBMS_SID


MYSQL_CONNECTION_STRING = {"user":"root"
                           ,"password":"kor0920"
                           ,"host":"127.0.0.1"
                           ,"port":3306
                           ,"database":"mysql"}


POSTGRESQL_CONNECTION_STRING = { "host":"127.0.0.1",
                                 "database":"postgres",
                                 "user":"postgres",
                                 "password":"kor0920",
                                 "port": 5433}