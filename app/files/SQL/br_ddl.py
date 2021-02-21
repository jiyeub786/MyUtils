import app.PyClass.TimeClass as t

tt = t.Time()
ymd = tt.getStrYMD2();


DDL01 = " CREATE TABLE BR.MART_DJY_01_"+ymd+"\
    (\
        mgmBldrgstPk VARCHAR2(33),\
        mgmUpBldrgstPk VARCHAR2(33),\
        regstrGbCd VARCHAR2(1),\
        regstrGbCdNm VARCHAR2(100),\
        regstrKindCd VARCHAR2(1),\
        regstrKindCdNm VARCHAR2(100),\
        platPlc VARCHAR2(200),\
        newPlatPlc VARCHAR2(200),\
        bldNm VARCHAR2(100),\
        sigunguCd VARCHAR2(5),\
        bjdongCd VARCHAR2(5),\
        platGbCd CHAR(1),\
        bun VARCHAR2(4),\
        ji VARCHAR2(4),\
        splotNm VARCHAR2(200),\
        block VARCHAR2(20),\
        lot VARCHAR2(20),\
        bylotCnt NUMBER(5),\
        naRoadCd VARCHAR2(12),\
        naBjdongCd VARCHAR2(5),\
        naUgrndCd VARCHAR2(1),\
        naMainBun NUMBER(5),\
        naSubBun NUMBER(5),\
        jiyukCd VARCHAR2(6),\
        jiguCd VARCHAR2(6),\
        guyukCd VARCHAR2(6),\
        jiyukCdNm VARCHAR2(100),\
        jiguCdNm VARCHAR2(100),\
        guyukCdNm VARCHAR2(100),\
        crtnDay VARCHAR2(8)\
    );"


DDL02 = " CREATE TABLE BR.MART_DJY_02_"+ymd+"\
    (\
        mgmBldrgstPk VARCHAR2(33),\
        regstrGbCd VARCHAR2(1),\
        regstrGbCdNm VARCHAR2(100),\
        regstrKindCd VARCHAR2(1),\
        regstrKindCdNm VARCHAR2(100),\
        newOldRegstrGbCd CHAR(1),\
        newOldRegstrGbCdNm VARCHAR2(100),\
        platPlc VARCHAR2(200),\
        newPlatPlc VARCHAR2(200),\
        bldNm VARCHAR2(100),\
        sigunguCd VARCHAR2(5),\
        bjdongCd VARCHAR2(5),\
        platGbCd CHAR(1),\
        bun VARCHAR2(4),\
        ji VARCHAR2(4),\
        splotNm VARCHAR2(200),\
        block VARCHAR2(20),\
        lot VARCHAR2(20),\
        bylotCnt NUMBER(5),\
        naRoadCd VARCHAR2(12),\
        naBjdongCd VARCHAR2(5),\
        naUgrndCd VARCHAR2(1),\
        naMainBun NUMBER(5),\
        naSubBun NUMBER(5),\
        platArea NUMBER(19,9),\
        archArea NUMBER(19,9),\
        bcRat NUMBER(19,9),\
        totArea NUMBER(19,9),\
        vlRatEstmTotArea NUMBER(19,9),\
        vlRat NUMBER(19,9),\
        mainPurpsCd VARCHAR2(5),\
        mainPurpsCdNm VARCHAR2(100),\
        etcPurps VARCHAR2(500),\
        hhldCnt NUMBER(5),\
        fmlyCnt NUMBER(5),\
        mainBldCnt NUMBER(5),\
        atchBldCnt NUMBER(5),\
        atchBldArea NUMBER(19,9),\
        totPkngCnt NUMBER(7),\
        indrMechUtcnt NUMBER(6),\
        indrMechArea NUMBER(19,9),\
        oudrMechUtcnt NUMBER(6),\
        oudrMechArea NUMBER(19,9),\
        indrAutoUtcnt NUMBER(6),\
        indrAutoArea NUMBER(19,9),\
        oudrAutoUtcnt NUMBER(6),\
        oudrAutoArea NUMBER(19,9),\
        pmsDay VARCHAR2(8),\
        stcnsDay VARCHAR2(8),\
        useAprDay VARCHAR2(8),\
        pmsnoYear VARCHAR2(4),\
        pmsnoKikCd CHAR(7),\
        pmsnoKikCdNm VARCHAR2(100),\
        pmsnoGbCd VARCHAR2(4),\
        pmsnoGbCdNm VARCHAR2(100),\
        hoCnt NUMBER(5),\
        engrGrade VARCHAR2(4),\
        engrRat NUMBER(19,9),\
        engrEpi NUMBER(5),\
        gnBldGrade CHAR(1),\
        gnBldCert NUMBER(5),\
        itgBldGrade CHAR(1),\
        itgBldCert NUMBER(5),\
        crtnDay VARCHAR2(8)\
    );"


DDL03 = " CREATE TABLE BR.MART_DJY_03_"+ymd+"\
    (\
        mgmBldrgstPk VARCHAR2(33),\
        regstrGbCd VARCHAR2(1),\
        regstrGbCdNm VARCHAR2(100),\
        regstrKindCd VARCHAR2(1),\
        regstrKindCdNm VARCHAR2(100),\
        platPlc VARCHAR2(200),\
        newPlatPlc VARCHAR2(200),\
        bldNm VARCHAR2(100),\
        sigunguCd VARCHAR2(5),\
        bjdongCd VARCHAR2(5),\
        platGbCd CHAR(1),\
        bun VARCHAR2(4),\
        ji VARCHAR2(4),\
        splotNm VARCHAR2(200),\
        block VARCHAR2(20),\
        lot VARCHAR2(20),\
        bylotCnt NUMBER(5),\
        naRoadCd VARCHAR2(12),\
        naBjdongCd VARCHAR2(5),\
        naUgrndCd VARCHAR2(1),\
        naMainBun NUMBER(5),\
        naSubBun NUMBER(5),\
        dongNm VARCHAR2(100),\
        mainAtchGbCd CHAR(1),\
        mainAtchGbCdNm VARCHAR2(100),\
        platArea NUMBER(19,9),\
        archArea NUMBER(19,9),\
        bcRat NUMBER(19,9),\
        totArea NUMBER(19,9),\
        vlRatEstmTotArea NUMBER(19,9),\
        vlRat NUMBER(19,9),\
        strctCd CHAR(1),\
        strctCdNm VARCHAR2(100),\
        etcStrct VARCHAR2(500),\
        mainPurpsCd VARCHAR2(5),\
        mainPurpsCdNm VARCHAR2(100),\
        etcPurps VARCHAR2(500),\
        roofCd VARCHAR2(2),\
        roofCdNm VARCHAR2(100),\
        etcRoof VARCHAR2(500),\
        hhldCnt NUMBER(5),\
        fmlyCnt NUMBER(5),\
        heit NUMBER(19,9),\
        grndFlrCnt NUMBER(5),\
        ugrndFlrCnt NUMBER(5),\
        rideUseElvtCnt NUMBER(5),\
        emgenUseElvtCnt NUMBER(5),\
        atchBldCnt NUMBER(5),\
        atchBldArea NUMBER(19,9),\
        totDongTotArea NUMBER(19,9),\
        indrMechUtcnt NUMBER(6),\
        indrMechArea NUMBER(19,9),\
        oudrMechUtcnt NUMBER(6),\
        oudrMechArea NUMBER(19,9),\
        indrAutoUtcnt NUMBER(6),\
        indrAutoArea NUMBER(19,9),\
        oudrAutoUtcnt NUMBER(6),\
        oudrAutoArea NUMBER(19,9),\
        pmsDay VARCHAR2(8),\
        stcnsDay VARCHAR2(8),\
        useAprDay VARCHAR2(8),\
        pmsnoYear VARCHAR2(4),\
        pmsnoKikCd CHAR(7),\
        pmsnoKikCdNm VARCHAR2(100),\
        pmsnoGbCd VARCHAR2(4),\
        pmsnoGbCdNm VARCHAR2(100),\
        hoCnt NUMBER(5),\
        engrGrade VARCHAR2(4),\
        engrRat NUMBER(19,9),\
        engrEpi NUMBER(5),\
        gnBldGrade CHAR(1),\
        gnBldCert NUMBER(5),\
        itgBldGrade CHAR(1),\
        itgBldCert NUMBER(5),\
        crtnDay VARCHAR2(8),\
        rserthqkapplc VARCHAR2(4000),\
        rserthqkablty VARCHAR2(4000)\
    );"


DDL04 = " CREATE TABLE BR.MART_DJY_04_"+ymd+"\
    (\
        mgmBldrgstPk VARCHAR2(33),\
        platPlc VARCHAR2(200),\
        newPlatPlc VARCHAR2(200),\
        bldNm VARCHAR2(100),\
        sigunguCd VARCHAR2(5),\
        bjdongCd VARCHAR2(5),\
        platGbCd CHAR(1),\
        bun VARCHAR2(4),\
        ji VARCHAR2(4),\
        splotNm VARCHAR2(200),\
        block VARCHAR2(20),\
        lot VARCHAR2(20),\
        naRoadCd VARCHAR2(12),\
        naBjdongCd VARCHAR2(5),\
        naUgrndCd VARCHAR2(1),\
        naMainBun NUMBER(5),\
        naSubBun NUMBER(5),\
        dongNm VARCHAR2(100),\
        flrGbCd VARCHAR2(2),\
        flrGbCdNm VARCHAR2(100),\
        flrNo NUMBER(4),\
        flrNoNm VARCHAR2(100),\
        strctCd CHAR(1),\
        strctCdNm VARCHAR2(100),\
        etcStrct VARCHAR2(500),\
        mainPurpsCd VARCHAR2(5),\
        mainPurpsCdNm VARCHAR2(100),\
        etcPurps VARCHAR2(500),\
        mainAtchGbCd CHAR(1),\
        mainAtchGbCdNm VARCHAR2(100),\
        area NUMBER(19,9),\
        areaExctYn VARCHAR2(1),\
        crtnDay VARCHAR2(8)\
    );"