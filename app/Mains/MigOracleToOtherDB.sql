--drop table mig_tbl_list 
--create table mig_tbl_list as 
/* 테이블 생성 구문 만들기 */ 
SELECT OBJ.OWNER 
       ,TBL.TABLE_NAME 
       ,SUM_DATA_LENGTH_BYTES --65536 BYTES 
       ,num_rows 
       ,'CREATE TABLE '||TBL.TABLE_NAME ||'('||CHR(13)||CREAT_COL_TEXT_ORACLE||')'  CREAT_TABLE_TEXT_ORACLE 
       ,'SELECT COUNT(*) ROWCOUNT FROM EDUORACLE.'||TBL.TABLE_NAME  COUNT_TABLE_TEXT_ORACLE 
       ,'CREATE TABLE TEST.'||TBL.TABLE_NAME ||'('||CHR(13)||CREAT_COL_TEXT_MYSQL||')ENGINE=InnoDB DEFAULT CHARSET=utf8;'  CREAT_TABLE_TEXT_MYSQL 
       ,'CREATE TABLE TEST.'||TBL.TABLE_NAME ||'('||CHR(13)||CREAT_COL_TEXT_POSTGRESQL||');'  CREAT_TABLE_TEXT_POSTGRESQL 
       ,'Y' TARGET_YN 
       ,0 fail 
       ,'INSERT INTO TEST.'||TBL.TABLE_NAME ||' VALUES ('||CREAT_INSERT_TEXT_MYSQL||')' CREAT_BIND_INSERT_TEXT_MYSQL 
        
       ,'INSERT INTO TEST.'||TBL.TABLE_NAME ||' VALUES ('||CREAT_INSERT_TEXT_POSTGRESQL||')' CREAT_BIND_INSERT_TEXT_POSTGRE 
     --  ,COL.* 
        
FROM DBA_OBJECTS OBJ 
INNER JOIN 
     DBA_TABLES TBL 
ON ( OBJ.OWNER = TBL.OWNER AND OBJECT_NAME = TBL.TABLE_NAME )  
INNER JOIN 
     (SELECT OWNER  
           ,TABLE_NAME 
           ,SUM(DATA_LENGTH_BYTES) SUM_DATA_LENGTH_BYTES 
           ,XMLAGG(XMLELEMENT( A,  CASE WHEN NOT COLUMN_ID = 1 THEN ',' ELSE ' ' END || RPAD(COLUMN_NAME,30,' ') || RPAD(DATA_TYPE_ORACLE,15,' ') || LPAD(DATA_CONSTRAINT_NULLABLE,10,' '),CHR(13) )    ORDER BY COLUMN_ID).EXTRACT('//text()').GETCLOBVAL() CREAT_COL_TEXT_ORACLE 
           ,XMLAGG(XMLELEMENT( A,  CASE WHEN NOT COLUMN_ID = 1 THEN ',' ELSE ' ' END || RPAD(COLUMN_NAME,30,' ') || RPAD(DATA_TYPE_MYSQL,15,' ') || LPAD(DATA_CONSTRAINT_NULLABLE,10,' '),CHR(13) )    ORDER BY COLUMN_ID).EXTRACT('//text()').GETCLOBVAL() CREAT_COL_TEXT_MYSQL 
           ,XMLAGG(XMLELEMENT( A,  CASE WHEN NOT COLUMN_ID = 1 THEN ',' ELSE ' ' END || RPAD(COLUMN_NAME,30,' ') || RPAD(DATA_TYPE_POSTGRESQL,15,' ') || LPAD(DATA_CONSTRAINT_NULLABLE,10,' '),CHR(13) )    ORDER BY COLUMN_ID).EXTRACT('//text()').GETCLOBVAL() CREAT_COL_TEXT_POSTGRESQL 
           ,LISTAGG( '?' ,',' ) WITHIN GROUP(ORDER BY COLUMN_ID )    CREAT_INSERT_TEXT_MYSQL 
           ,LISTAGG( '%s' ,',' ) WITHIN GROUP(ORDER BY COLUMN_ID )    CREAT_INSERT_TEXT_POSTGRESQL 
           --,LISTAGG(  COLUMN_NAME||' ' || DATA_TYPE_ORACLE ||' ' || DATA_CONSTRAINT_NULLABLE ) ,','||CHR(13) ) WITHIN GROUP(ORDER BY COLUMN_ID ) TEXT_CREAT_COL_ORACLE 
                 
     FROM (SELECT COL.OWNER 
                  ,COL.TABLE_NAME 
                  ,COLUMN_NAME 
                  ,DATA_TYPE 
                  ,DATA_LENGTH 
                   
                  ,CASE WHEN DATA_TYPE IN ('VARCHAR2','CHAR','') THEN DATA_LENGTH *3  
                        WHEN DATA_TYPE IN ('NUMBER','','') THEN DATA_LENGTH  
                        WHEN DATA_TYPE IN ('DATE','','') THEN DATA_LENGTH 
                        WHEN DATA_TYPE IN ('CLOB','','') THEN 0 
                        ELSE NULL  
                   END DATA_LENGTH_BYTES 
                   
                  ,DATA_PRECISION 
                  ,DATA_SCALE 
                  ,NULLABLE 
                  ,COLUMN_ID 
                  ,DATA_DEFAULT 
                  ,DECODE(NULLABLE,'Y','NULL','N','NOT NULL') DATA_CONSTRAINT_NULLABLE 
                  ,CASE WHEN DATA_TYPE IN ('VARCHAR2','CHAR','') THEN DATA_TYPE||'('||TO_CHAR(DATA_LENGTH)||')'  
                        WHEN DATA_TYPE IN ('NUMBER','','') THEN DATA_TYPE||'('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||NVL2(DATA_SCALE,','||DATA_SCALE,NULL) ||')' 
                        WHEN DATA_TYPE IN ('DATE','','') THEN DATA_TYPE 
                        WHEN DATA_TYPE IN ('CLOB','','') THEN 'CLOB' 
                        ELSE NULL  
                   END DATA_TYPE_ORACLE 
                    
                  ,CASE WHEN DATA_TYPE IN ('VARCHAR2','CHAR','') THEN DECODE(DATA_TYPE,'VARCHAR2','VARCHAR','CHAR','CHAR')||'('||TO_CHAR(DATA_LENGTH)||')'  
                        --WHEN DATA_TYPE IN ('NUMBER','','') AND NVL(DATA_SCALE,0) =  0 THEN 'DECIMAL('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||')' 
                         
                        WHEN DATA_TYPE IN ('NUMBER','','') AND DATA_SCALE IS NULL     THEN 'DOUBLE' -- NUMBER의 DATA_SACEL이 NULL이면 DOUBLE로 사용하여 아닐경우 DECIMAL로 명시 
                        WHEN DATA_TYPE IN ('NUMBER','','') AND DATA_SCALE IS NOT NULL THEN 'DECIMAL('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||','||DATA_SCALE||')' 
                        WHEN DATA_TYPE IN ('DATE','','') THEN 'DATETIME' 
                        WHEN DATA_TYPE IN ('CLOB','','') THEN 'LONGBLOB' 
                        ELSE NULL  
                   END DATA_TYPE_MYSQL  
                    
                  ,CASE WHEN DATA_TYPE IN ('VARCHAR2','CHAR','') THEN DECODE(DATA_TYPE,'VARCHAR2','VARCHAR','CHAR','CHAR')||'('||TO_CHAR(DATA_LENGTH)||')'  
                        --WHEN DATA_TYPE IN ('NUMBER','','') AND NVL(DATA_SCALE,0) =  0 THEN 'DECIMAL('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||')' 
                         
                        WHEN DATA_TYPE IN ('NUMBER','','') AND DATA_SCALE IS NULL     THEN 'DECIMAL('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||','||'0'||')' 
                        WHEN DATA_TYPE IN ('NUMBER','','') AND DATA_SCALE IS NOT NULL THEN 'DECIMAL('||TO_CHAR(NVL( DATA_PRECISION,DATA_LENGTH))||','||DATA_SCALE||')' 
                        WHEN DATA_TYPE IN ('DATE','','') THEN 'TIMESTAMP' 
                        WHEN DATA_TYPE IN ('CLOB','','') THEN 'TEXT' 
                        ELSE NULL  
                   END DATA_TYPE_POSTGRESQL                    
                    
           FROM DBA_TAB_COLUMNS COL 
           INNER JOIN 
                (SELECT OWNER , TABLE_NAME  
                 FROM DBA_TABLES )TBL  
           ON ( COL.OWNER = TBL.OWNER AND COL.TABLE_NAME = TBL.TABLE_NAME ) )  
     GROUP BY OWNER , TABLE_NAME ) COL 
ON ( TBL.OWNER = COL.OWNER AND TBL.TABLE_NAME = COL.TABLE_NAME ) 
WHERE OBJ.OWNER ='EDUORACLE'  
 AND NOT ( OBJ.OBJECT_NAME LIKE '%$%' OR OBJ.OBJECT_NAME LIKE '%#%' ) --MYSQL SYNTAX    
 and SUM_DATA_LENGTH_BYTES < 65535 
 
 
SELECT * FROM DBA_TAB_COLUMNS 
WHERE DATA_TYPE='NUMBER' 
 
create table eduoracle.mig_tbl_failed 
( 
table_name varchar2(50) 
,failed_desc clob 
,exception_desc clob 
,creat_dt date default sysdate  
) 
