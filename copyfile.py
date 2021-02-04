import os 
import shutil
 
srcpath=r'D:\archive18273\zc2214'
targetpath=r'D:\archive18273\output'
#累加，用于命名
i=1
#返回指定路径下的文件和目录信息
pathDir =  os.listdir(srcpath)
#遍历
for allDir in pathDir:
 
 
    for j in os.listdir(os.path.join(srcpath, allDir)):
        if j == "output.log":
            #路径拼接
            imgPath = os.path.join(srcpath,allDir,j)
 
            newtargetpath=targetpath+str(i).zfill(6)+'.log'#zfill()向右对齐，用0补齐
            #复制文件
            shutil.copyfile(imgPath,newtargetpath)
            #打印被复制的文件
            print(imgPath)
            i+=1
