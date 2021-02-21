from app.PyClass import MysqlClass as mysql, OracleClass as oracle, TimeClass as t
from app.PyClass.LoggerClass import logger

logger.info("aaaa")



time = t.Time()  # 프로그램 시작 시간
startTime = time.getNow()


targetTableListQuery = "select 'select * from eduoracle.'||table_name, 'test.'||lower(table_name)  ,COUNT_TABLE_TEXT_ORACLE TABLE_COUNT ,NUM_ROWS , TABLE_NAME ,CREAT_BIND_INSERT_TEXT_MYSQL from eduoracle.mig_tbl_list   where TARGET_YN='Y' order by NUM_ROWS"
dateTypeTextOacle = '<cx_Oracle.DbType DB_TYPE_DATE>'

# init oracle for target list
oracle01 = oracle.Oracle()
targetListCur = oracle01.select( targetTableListQuery)
targetInfoList = list(targetListCur)
oracle01.close()

migrationTargetInfoList = []
for rowTp in targetInfoList:
    resultDict = {"selectORACLE": list(rowTp)[0]
        , "selectMYSQL": list(rowTp)[1]
        , "selectRowCountORACLE": list(rowTp)[2]
        , "selectTablenameORACLE": list(rowTp)[4]
        , "insertBindStringMysql": list(rowTp)[5]
              }
    migrationTargetInfoList.append(resultDict)
# 1) 오라클에서 대상 테이블 , 관련 SQL을 추출함
for targetTableIndex, targetTableText in enumerate(migrationTargetInfoList):
    oracle02 = oracle.Oracle()  # init oracle02 for target table fetch each rows
    oracle03 = oracle.Oracle()  # init oracle03 for insert / update logging
    rowCountCur = oracle02.select( targetTableText["selectRowCountORACLE"]) # 1-1) 테이블의 행 수를 조회 하여 행수를 저장함
    rowCount = str(list(rowCountCur)[0]).strip('()').replace(',', '')

    startTimePerWork = time.getNow()  # 시작 시간 저장
    totlDurationSecond = time.getTimeSub(startTime ,time.getNow() ) # 개별작업 소요시간

    logger.info("---------------------------------------------------------------------------------------------------------------------")
    logger.info(" [ start time" + " => " + str(totlDurationSecond) +
           " |     " + "target" +" => " + targetTableText["selectTablenameORACLE"].ljust(29,' ') +
           " | " + "target rowCount" +" => " + str(rowCount) +
           " ] "
                )

    fetchCur = oracle02.select(targetTableText["selectORACLE"])  # 1-2) 작업할 테이블을 조회하여 커서를 얻음
    fetchList = fetchCur.fetchmany(1)

    insertPerRow = 50000#bulk insert할 버퍼의 크기
    insertBuffer = []
    counter = 1
    sleepTerm = 0
    failCount = 0

    # init mysql for bulk insert
    mysql01 = mysql.Mysql()
    while fetchList: # 2) 오라클에서 추출한 테이블별로 1행씩 FECTH하여 MYSQL에 INSERT함
        rowValues = list(fetchList[0])# 2-1) FETCH한 행별로 MYSQL에 입력하기 위한 포멧으로 변환
        rowValuesModf = []
        for value in rowValues:
          #  print( str(type(value))  + str(value))
            if str(type(value)) == str(type(int)) or type(value) == str(type(float)) or str(type(value)) == str(type(str) or type(value)) == str(type(None)) :
                value = value # int float str은 처리없음 null = NONE
            elif str(type(value)) == "<PyClass 'datetime.datetime'>":
                value = str(value) #datetime 타입처리
            elif str(type(value)) == "<PyClass 'cx_Oracle.LOB'>":
                value = str(value) #lob 타입처리
            rowValuesModf.append(value)

        insertBuffer.append(tuple(rowValuesModf))
        # 2-2) 정해진 버퍼크기가 도달하면 MYSQL에 입력한다
        if int(insertPerRow) == int(len(insertBuffer)) or int(counter) == int(rowCount):
            # print(sys.getsizeof(insertBuffer))
             try : # 2-3) 만들어진 스트링을 mysql에 입력한다
                 mysql01.insertmany(targetTableText["insertBindStringMysql"], insertBuffer)
                 mysql01.commit()

             except Exception as e : # 2-4) 스트링 입력시 db에서 오류가 발생하는것을 오라클에 저장한다
                 failCount = 1
                 insertRow = ( targetTableText["selectTablenameORACLE"],str(insertBuffer), str(e))
                 oracle03.insert("insert into eduoracle.mig_tbl_failed(table_name,failed_desc,exception_desc) values(:1,:2,:3)",insertRow)
                 oracle03.commit()
                 break

             insertBuffer = []


        counter = counter + 1
        fetchList = fetchCur.fetchmany(1)

    if  failCount == 0 : # oracle03 save target result
        oracle03.update("update eduoracle.mig_tbl_list set target_yn = :1 ,fail = :2 where table_name = :3",['N', failCount, targetTableText["selectTablenameORACLE"]])
    else :
        oracle03.update("update eduoracle.mig_tbl_list set target_yn = :1 ,fail = :2 where table_name = :3",['Y', failCount, targetTableText["selectTablenameORACLE"]])

    oracle03.commit()
    oracle03.close()
    oracle02.close()
    mysql01.close()

    totlDurationSecond = time.getTimeSub(time.getNow() , startTime)
    workPerDurationSecond = time.getTimeSub(time.getNow() , startTimePerWork)
    logger.info(" [ end time" + " => " + str(totlDurationSecond) +
           " | " + "work" + " => " + str(targetTableIndex + 1) + "/" + str(len(migrationTargetInfoList)) +
           " | " + "fail_count" +" => " + str(failCount) +
           " | " + "time per work" + " => " + str(workPerDurationSecond) +
           " ]")

print("work end")