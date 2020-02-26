import os

def delFilesByID(dirPath):
    for root, dirs, files in os.walk(dirPath):
        for name in files:
            if name.find("sample") == -1:
                os.remove(os.path.join(root, name))
            
if __name__ == '__main__':
    delFilesByID(r"D:\demo") #输入指定路径
    print("Finished!")
