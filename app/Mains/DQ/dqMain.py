from app.PyClass import OracleClass as oracle
from app.PyClass import TimeClass
from app.PyClass import XMLClass as XML
import pandas as pd


def errReport():
    t = TimeClass.Time()

    xml = XML.XMLclass('dqMapper')
    xml2 = XML.XMLclass('property')
    filePath = xml2.getData("OUTPUT")

    workList = [
        {'SQL': xml.getData("selectVldErrDataResult"), 'sheetName': '오류값목록'}

    ]
    file = f'{filePath}/dq_errDataList_report_{t.getStrYMD2()}.xlsx'
    print(file)
    writer = pd.ExcelWriter(file, engine="xlsxwriter")

    ora = oracle.Oracle(connectName='oracle_DQ')
    for work in workList:
        df = ora.getResultToDataFrame(work["SQL"])
        df.to_excel(writer, sheet_name=work["sheetName"], encoding='utf-8', freeze_panes=(1, 0), index=False)

    writer.save()


def mainReport():
    t = TimeClass.Time()

    xml = XML.XMLclass('dqMapper')
    xml2 = XML.XMLclass('property')
    filePath = xml2.getData("OUTPUT")

    workList = [
        {'SQL': xml.getData("selectTabColList"), 'sheetName': '테이블칼럼전체목록'}
        , {'SQL': xml.getData("selectTabColCommentsStat"), 'sheetName': '논리명요약'}
        , {'SQL': xml.getData("selectTargetTable"), 'sheetName': '분석대상테이블'}
        , {'SQL': xml.getData("selectTargetColumn"), 'sheetName': '분석대상칼럼'}
        , {'SQL': xml.getData("selectAnalyzeColumnVldResult"), 'sheetName': '칼럼값검사'}
        , {'SQL': xml.getData("selectAnalyzeTableVldResult"), 'sheetName': '테이블값검사'}
        , {'SQL': xml.getData("selectAnalyzeTotalVldResult"), 'sheetName': '값검사요약'}
    ]
    file = f'{filePath}/dq_report_{t.getStrYMD2()}.xlsx'
    print(file)
    writer = pd.ExcelWriter(file, engine="xlsxwriter")

    ora = oracle.Oracle(connectName='oracle_DQ')
    for work in workList:
        df = ora.getResultToDataFrame(work["SQL"])
        df.to_excel(writer, sheet_name=work["sheetName"], encoding='utf-8', freeze_panes=(1, 0), index=False)

    writer.save()


def vldInfo():
    t = TimeClass.Time()

    xml = XML.XMLclass('dqMapper')
    xml2 = XML.XMLclass('property')
    filePath = xml2.getData("OUTPUT")

    workList = [
        {'SQL': xml.getData("selectColVldList"), 'sheetName': '적용규칙목록'}
        , {'SQL': xml.getData("selectVldList"), 'sheetName': '규칙목록'}

    ]
    file = f'{filePath}/dq_vldList_{t.getStrYMD2()}.xlsx'
    print(file)
    writer = pd.ExcelWriter(file, engine="xlsxwriter")

    ora = oracle.Oracle(connectName='oracle_DQ')
    for work in workList:
        df = ora.getResultToDataFrame(work["SQL"])
        df.to_excel(writer, sheet_name=work["sheetName"], encoding='utf-8', freeze_panes=(1, 0), index=False)

    writer.save()


vldInfo()
errReport()
mainReport()