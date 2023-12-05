import os
import datetime

save_path = '/home/edumac/file_list.txt'
search_path = '/home/edumac'
f = open(save_path, mode='a', encoding='UTF-8')

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                f_size = os.path.getsize(full_filename)
                f_path = full_filename
                f_ctime = datetime.datetime.strftime (datetime.datetime.fromtimestamp(os.path.getctime(full_filename)) ,'%Y-%m-%d %H:%M:%S')


                f.writelines(f_ctime+  '\t' +  str(f_size)  + '\t' + f_path)


    except PermissionError:
        pass

search(search_path)



