#-*- coding: utf-8 -*-
import os
from app.module import modules as m
from app.PyClass import OracleClass

#소스 경로 저장
base_dir = os.path.dirname( os.path.abspath( __file__ ) )
inputFilePath = base_dir + "/Files/INPUTS/" #읽을 파일 경로
outputFilePath = base_dir + "/Files/OUTPUTS/" #결과값 저장 경로


# sql 텍스트파일 1개 > 텍스트 파일 당 엑셀 산출 > m.getSqlListToExcels
# sql 텍스트파일 n개 > 단일 엑셀 파일 산출 > m.getSqlListToExcel

if __name__ == "__main__":
    # inputFilePath에 있는 sql 텍스트 파일을 읽어서 sql을 저장한 배열을 리턴한다
    sqlList = m.getSqlDictList(inputFilePath )
    #m.getSqlDictListToExcels(sqlList, outputFilePath, dbcon.GetDBConnect(dbconfig.DBMS_CONNECTION))
    con = OracleClass.Oracle()
    m.getSqlDictListToExcel(sqlList, outputFilePath, con)