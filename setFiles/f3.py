import os
import os.path

def renameFilesSortedByTime(dirPath):
    mlist = []

    files = os.listdir(dirPath)

    for filename in files:
        createTime = os.path.getmtime(dirPath + filename)

        # 这里将时间与文件名放一起方便后续作截取
        mlist.append(str(int(createTime)) + "-" + filename)

    mlist = sorted(mlist)

    for i in range(len(mlist)):
        oldName = mlist[i][11:]
        if (i + 1) < 10:
            newName = "cr00" + str(i + 1) 
        elif (i + 1) > 9 and (i + 1) < 100:
            newName = "cr0" + str(i + 1)
        else:
            newName = "cr"+str(i + 1)
        newName = newName + '.jpg'
        os.rename(dirPath + oldName, dirPath + newName)

if __name__ == '__main__':
    renameFilesSortedByTime("D:/demo")
    print("Finished!")
