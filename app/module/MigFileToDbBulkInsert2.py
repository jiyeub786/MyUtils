

from app.module import File
from app.module import Time
import time
from app.database import Oracle

t = Time.Time()
File01 = File.File( "G:/ff/mart_djy_01.txt")
file01 = File01.readFile()


startTime = t.getNow()


buffer = 1024*1024 * 10
endLine =0
#get file end line
while True:
    lines = file01.readlines(buffer)
    endLine = endLine + str(lines).count("\\n")
    if not lines :
        file01.close()
        break;
    print("\r seek endLine : "+str(endLine) + " Elapsed time:"+ str(t.getTimeSub(startTime,t.getNow()))+"s",end="")


print("")



t = Time.Time()


startTime = t.getNow()

ora = Oracle.Oracle()

counter = 0
buffersize = 20000
insertbuffer = []

File02 = File.File( "G:/ff/mart_djy_01.txt")

file02 = File02.readFile()
while True:
    counter = counter + 1
    data = file02.readline()

    if not data:
        print("\rinserting rows :" + str(counter) + "/" + str(endLine) + "  [" + str(
            round(counter / endLine, 4)) + "%] Elapsed time: " + str(t.getTimeSub(startTime, t.getNow())) + "s", end="")
        ora.insertmany(
            "insert /*+APPEND_VALUES*/ into eduoracle.test_ins values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30)"
            , insertbuffer)
        ora.commit()
        file02.close()
        break

    else :

        dataSplited = data.split('|')
        dataMoif = []

        for v in dataSplited:
            dataMoif.append(v.replace("''", "None"))

        insertbuffer.append(tuple(dataMoif))

        if len(insertbuffer) == buffersize :
            print("\rinserting rows :" + str(counter) + "/" + str(endLine) + "  [" + str(
                round(counter / endLine, 4)) + "%] Elapsed time: " + str(t.getTimeSub(startTime, t.getNow())) + "s",
                  end="")
            ora.insertmany("insert /*+APPEND_VALUES*/into eduoracle.test_ins values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30)"
                , insertbuffer)
            ora.commit()
            insertbuffer = []

print ( t.getTimeSub(startTime,t.getNow()) )