# -*- coding: utf-8 -*-

import os
import os.path                                   


def renameNameSorted(dirPath):

    i=0
    for parent,dirnames,filenames in os.walk(dirPath):     
        for filename in filenames:

            # 这里图片大小定义在1000内
            if i < 10:
                newName = "00" + str(i)
            elif i > 9 and i < 100:
                newName = "0" + str(i)
            else:
                newName = str(i)

            i=i+1    
            newName=newName+'.jpg'
            
            os.rename(os.path.join(parent,filename),os.path.join(parent,newName)) 


if __name__ == '__main__':
    renameNameSorted(r"D:\demo") #输入指定路径
    print("Finished!")
