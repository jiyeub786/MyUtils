from app.PyClass import BrClass as br, TimeClass
from app.PyClass import XMLClass as XML

xml = XML.XMLclass('brMapper')

brMartDjy01 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy01']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy01']") ,'tablename' :  'BR.MART_DJY_01' }
brMartDjy02 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy02']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy02']") ,'tablename' :  'BR.MART_DJY_02' }
brMartDjy03 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy03']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy03']") ,'tablename' :  'BR.MART_DJY_03' }
brMartDjy04 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy04']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy04']") ,'tablename' :  'BR.MART_DJY_04' }
brMartDjy05 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy05']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy05']") ,'tablename' :  'BR.MART_DJY_05' }
brMartDjy09 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartDjy09']") ,'dml' : xml.getText("./insert[@id='insertBrMartDjy09']") ,'tablename' :  'BR.MART_DJY_09' }
brMartShtreg01 = { 'ddl' : xml.getText("./ddl[@id='setTableBrMartShtreg01']") ,'dml' : xml.getText("./insert[@id='insertBrMartShtreg01']") ,'tablename' :  'BR.MART_SHTREG_01' }


t = TimeClass.Time()

mart_djy01 = br.BrFile(path="S:/건축물대장21.02/mart_djy_01.txt",ddl= brMartDjy01['ddl'],dml=brMartDjy01['dml'],tablename=brMartDjy01['tablename']) #기본개요
mart_djy02 = br.BrFile(path="S:/건축물대장21.02/mart_djy_02.txt",ddl= brMartDjy02['ddl'],dml=brMartDjy02['dml'],tablename=brMartDjy02['tablename']) #총괄표제부
mart_djy03 = br.BrFile(path="S:/건축물대장21.02/mart_djy_03.txt",ddl= brMartDjy03['ddl'],dml=brMartDjy03['dml'],tablename=brMartDjy03['tablename']) #표제부
mart_djy04 = br.BrFile(path="S:/건축물대장21.02/mart_djy_04.txt",ddl= brMartDjy04['ddl'],dml=brMartDjy04['dml'],tablename=brMartDjy04['tablename']) #층별개요
mart_djy05 = br.BrFile(path="S:/건축물대장21.02/mart_djy_05.txt",ddl= brMartDjy05['ddl'],dml=brMartDjy05['dml'],tablename=brMartDjy05['tablename']) #부속지번
mart_djy09 = br.BrFile(path="S:/건축물대장21.02/mart_djy_09.txt",ddl= brMartDjy09['ddl'],dml=brMartDjy09['dml'],tablename=brMartDjy09['tablename']) #전유부
mart_shtreg01 = br.BrFile(path="S:/건축물대장21.02/mart_shtreg_01.txt",ddl= brMartShtreg01['ddl'],dml=brMartShtreg01['dml'],tablename=brMartShtreg01['tablename']) #폐쇄말소대장





# mart_djy01.setTableDROP()
# mart_djy01.setTable()
# mart_djy01.readAndInsert(11)

# mart_djy02.setTableDROP()
# mart_djy02.setTable()
# mart_djy02.readAndInsert(11)

# mart_djy03.setTableDROP()
# mart_djy03.setTable()
# mart_djy03.readAndInsert(11)

# mart_djy04.setTableDROP()
# mart_djy04.setTable()
# mart_djy04.readAndInsert(11)

mart_djy05.setTableDROP()
mart_djy05.setTable()
mart_djy05.readAndInsert(11)

# mart_djy09.setTableDROP()
# mart_djy09.setTable()
# mart_djy09.readAndInsert(10)

# mart_shtreg01.setTableDROP()
# mart_shtreg01.setTable()
# mart_shtreg01.readAndInsert(11)