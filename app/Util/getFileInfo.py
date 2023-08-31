# -*- coding: utf-8 -*-
import os
import csv
from datetime import datetime

dir_path = "/upload/"
format_string = "%Y-%m-%d %H:%M:%S"
result_file = "/data/fileList.csv"

# dir_path = "G:/1"
# format_string = "%Y-%m-%d %H:%M:%S"
# result_file = "G:/1/fileList.csv"


buffersize = 1000
insertbuffer = []
counter = 0

#f = open(result_file , mode='a', encoding='utf-8',newline="")
f = open(result_file , 'a' )
wr = csv.writer(f,delimiter='\t')


for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file).replace("\t","")
        file_byte = str(os.path.getsize(file_path))
        file_ctime = datetime.fromtimestamp( os.path.getctime(file_path) ).strftime(format_string)
        counter = counter + 1


        result = [counter,file_path,file_byte,file_ctime]
        insertbuffer.append(result)
        print( str(result )   )

        if len(insertbuffer) == buffersize:
            wr.writerows(insertbuffer )
            insertbuffer = []

wr.writerows(insertbuffer)
insertbuffer = []

f.close()