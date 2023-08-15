# 复制文件夹

import os
import shutil


def get_filepath(folderpath):
    filelist= []
    folderpath = folderpath.replace('\\', '/')
    filesfolders = os.walk(os.path.join(folderpath))
    filesfoldername = os.path.basename(folderpath)
    for filesfolder in filesfolders:
        for file in filesfolder[2]:
            filepath = filesfolder[0].replace('\\','/')+'/'+file
            filepath = filepath.replace(folderpath,'')
            filelist.append(filepath)
            # print(filepath)
    return filesfoldername,filelist


def open_new_file(newfolderpath, filepath):
    file =(newfolderpath + filepath).replace('\\', '/')
    try:
        f = open(file,'wb') 
    except FileNotFoundError:
        os.makedirs(os.path.dirname(file))
        f = open(file,'wb')
    return f

def copy_folder(newfolderpath):
    filesfoldername, filepaths = get_filepath(folderpath)
    for filepath in filepaths:
        with open(folderpath+filepath, 'rb') as fr:
            fw = open_new_file(newfolderpath +'\{}'.format(filesfoldername), filepath)
            for line in fr.readlines():
                fw.write(line)
                # print(line)
            fw.close()
            fr.close()


if __name__ == '__main__':
    folderpath = r'C:\Users\51276\Desktop\软件'
    folderpath = folderpath.replace('\\', '/')
    copy_folder(r'F:\1')
print('完成')
    print(filepath)
