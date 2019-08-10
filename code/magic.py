import time

#-----------------先行部分----------
t1=time.time()
print "复原魔方步骤如下："



#-----------------初始化数据---------------
'''
[0,1,2,3,4,5]依次代表颜色红橙蓝绿黄白
a~f : 各个面识别的颜色,依次代表上下左右前后层面
magicList: 包含颜色列表整个魔方体

'''
a=[0,0,0,1,4,5,2,0,4]#上
b=[4,4,5,1,5,0,2,0,3]#下
c=[2,4,1,5,0,2,4,2,3]#左
d=[5,4,3,5,3,3,0,2,2]#前
e=[1,3,5,4,1,1,0,5,1]#右
f=[3,3,4,3,2,1,5,2,1]#后
magicList = [[a],[b],[c],[d],[e],[f]]
temp=[0,0,0,0,0,0,0,0,0] #定义交换参数


#-------------构建魔方转向变动函数---------

#整体左转
def wholeTurnLeft():
    #上层面进行变换
    for i in range(9):
        temp[i] = a[i]
    a[0] = temp[6]
    a[1] = temp[3]
    a[2] = temp[0]
    a[3] = temp[7]
    a[4] = temp[4]
    a[5] = temp[1]
    a[6] = temp[8]
    a[7] = temp[5]
    a[8] = temp[2]
    #下层面进行交换
    for i in range(9):
        temp [i] = b[i]
    b[0] = temp[2]
    b[1] = temp[5]
    b[2] = temp[8]
    b[3] = temp[1]
    b[4] = temp[4]
    b[5] = temp[7]
    b[6] = temp[0]
    b[7] = temp[3]
    b[8] = temp[6]
    #中间层进行交换
    #左前右后层面依次轮换
    for i in range(9):
        temp [i] = c[i]
    for i in range(9):
        c[i] = d[i]
        d[i] = e[i]
        e[i] = f[i]
        f[i] = temp[i]



#整体右转
def wholeTurnRight():
    for i in range(3):
        wholeTurnLeft()

#左层向下转动
def leftTurnDown():
    for i in range(9):
        temp [i] = c[i]
    c[0] = temp[6]
    c[1] = temp[3]
    c[2] = temp[0]
    c[3] = temp[7]
    c[4] = temp[4]
    c[5] = temp[1]
    c[6] = temp[8]
    c[7] = temp[5]
    c[8] = temp[2]
    
    #1，4，7块
    temp[0] = d[0]
    temp[1] = d[3]
    temp[2] = d[6]

    d[0] = a[0]
    d[3] = a[3]
    d[6] = a[6]

    a[0] = f[8]
    a[3] = f[5]
    a[6] = f[2]

    f[2] = b[6]
    f[5] = b[3]
    f[8] = b[0]

    b[0] = temp[0]
    b[3] = temp[1]
    b[6] = temp[2]


#左层向上转动
def leftTurnUp():
    for i in range(3):
        leftTurnDown()

#上层向右转动    
def upTurnRight():
    for i in range(9):
        temp [i] = a[i]
    a[0] = temp[2]
    a[1] = temp[5]
    a[2] = temp[8]
    a[3] = temp[1]
    a[4] = temp[4]
    a[5] = temp[7]
    a[6] = temp[0]
    a[7] = temp[3]
    a[8] = temp[6]

    #1，2，3块
    temp[0] = d[0]
    temp[1] = d[1]
    temp[2] = d[2]

    d[0] = c[0]
    d[1] = c[1]
    d[2] = c[2]
    
    c[0] = f[0]
    c[1] = f[1]
    c[2] = f[2]
    
    f[0] = e[0]
    f[1] = e[1]
    f[2] = e[2]

    e[0] = temp[0]
    e[1] = temp[1]
    e[2] = temp[2]


#上层向左转动
def upTurnLeft():
    for i in range(3):
        upTurnRight()

#前层顺时针
def frontClock():
    wholeTurnLeft()
    leftTurnDown()
    wholeTurnRight()


#前层逆时针
def frontOnClock():
    wholeTurnLeft()
    leftTurnUp()
    wholeTurnRight()


#右层向下
def rightTurnDown():
    for i in range(2):
        wholeTurnLeft()
    leftTurnUp()
    for i in range(2):
        wholeTurnLeft()


#右层向上
def rightTurnUp():
    for i in range(2):
        wholeTurnLeft()
    leftTurnDown()
    for i in range(2):
        wholeTurnLeft()


#-------------定义魔方公式--------------

#左手公式
def LHand():
    upTurnRight()
    print "上层右转"
    leftTurnUp()
    print "左层向上转"
    upTurnLeft()
    print "上层向左转"
    leftTurnDown()
    print "左层向下转"

#右手公式
def RHand():
    upTurnLeft()
    print "上层向左转"
    rightTurnUp()
    print "右层向上转"
    upTurnRight()
    print "上层向右转"
    rightTurnDown()
    print "右层向下转"

#一字公式
def One():
    rightTurnUp()
    print "右层向上转"
    upTurnLeft()
    print "上层向左转"
    rightTurnDown()
    print "右层向下转"
    upTurnRight()
    print "上层向右转"
    rightTurnDown()
    print "右层向下转"
    frontClock()
    print "前层顺时针转"
    rightTurnUp()
    print "右层向上转"
    frontOnClock()
    print "前层逆时针转"

#拐角公式
def Round():
    frontClock()
    print "前层顺时针转"
    rightTurnUp()
    print "右层向下转"
    upTurnRight()
    print "上层向右转"
    rightTurnDown()
    print "右层向下转"
    upTurnRight()
    print "上层向右转"
    rightTurnUp()
    print  "右层向上转"
    upTurnLeft()
    print "上层向左转"
    rightTurnDown()
    print "右层向下转"
    frontOnClock()
    print "前层逆时针转"

#左小鱼公式
def Lfish():
    leftTurnUp()
    print "左层向上转"
    upTurnRight()
    print "上层向右转"
    leftTurnDown()
    print "左层向下转"
    upTurnRight()
    print "上层向右转"
    leftTurnUp()
    print "左层向上转"
    upTurnRight()
    print "上层向右转"
    upTurnRight()
    print "上层向右转"
    leftTurnDown()
    print "左层向下转"

#右小鱼公式
def Rfish():
    rightTurnUp()
    print "右层向上转"
    upTurnLeft()
    print "上层向左转"
    rightTurnDown()
    print "右层向下转"
    upTurnLeft()
    print "上层向左转"
    rightTurnUp()
    print"右层向上转"
    upTurnLeft()
    print "上层向左转"
    upTurnLeft()
    print "上层向左转"
    rightTurnDown()
    print "右层向下转"

#----------------------按步骤的魔方复原算法---------------------------

#-------------魔方复原算法第一步:找到小白花
'''
小白花：又称顶层架十字，黄色的中心块做花蕊，四个白色的棱块做花瓣

'''
def findWhiteFlower():
    
    if(a[1]!=5) or (a[7]!=5) or (a[3]!=5) or (a[5]!=5):
        #先从前边面开始到遍历完每个面找白块
        flag = 0 #左转找白块面次数
        while(flag!=4):
            if (d[1]!=5) and (d[7]!=5) and (d[3]!=5) and (d[5]!=5):
                wholeTurnLeft()
                print "整体左转"
                flag += 1
            else:
                flag=0
                if(d[1]==5):
                    frontClock()
                    print "前层顺时针转"
                    rightTurnUp()
                    print "右层向上转"
                if(d[7]==5):
                    frontClock()
                    print "前层顺时针转"
                    leftTurnUp()
                    print "左层向上转"
                if(d[3]==5):
                    while(a[3]==5):
                        upTurnRight()
                        print "上层右转"
                    leftTurnUp()
                    print "左层向上转"
                if(d[5]==5):
                    while(a[5]==5):
                        upTurnRight()
                        print "上层右转"
                    rightTurnUp()
                    print "右层向上转"
    
    while(a[1]!=5) or (a[7]!=5) or (a[3]!=5) or (a[5]!=5):
        if(b[1]==5):
            while(a[7]==5):
                upTurnRight()
                print "上层右转"
            for i in range(2):
                frontClock()
                print "前层顺时针转"
        wholeTurnLeft()
        print "整体左转"

#--------------魔方复原算法第二步:底棱归位
def Step2Position():
    for i in range(4):
        while((d[1]!=d[4]) or a[7]!=5 ):
            upTurnLeft()
            print "上层左转"
        for i in range(2):
            frontClock()
            print "前层顺时针转"
        wholeTurnLeft()
        print "整体左转"

#--------------魔方复原算法第三步:底角归位
def Step3Position():
    asFlag=0
    while (asFlag==0):
        #判断底侧面三块同色,底层全为白块
        if (c[6]==c[7]==c[8])and(d[6]==d[7]==d[8])and(e[6]==e[7]==e[8])and(f[6]==f[7]==f[8])and (b[0]==b[1]==b[2]==b[3]==b[4]==b[5]==b[6]==b[7]==b[8]==5):
            asFlag=1
            break
            
        #上层脚块白色判断
        if (a[0]==5) or (a[2]==5) or (a[6]==5) or (a[8]==5):
            while(a[6]!=5):
                upTurnRight()
                print "上层向右转"
            while(c[2]!=d[4] or c[4]!=d[0]):
                upTurnRight()
                print "上层向右转"
                wholeTurnLeft()
                print "整体左转"
            for i in range(3):
                LHand()

        #侧面上层白色判断
        elif (c[0]==5) or (c[2]==5) or (d[0]==5) or (d[2]==5) or (e[0]==5) or (e[2]==5) or (f[0]==5) or (f[2]==5):
            while(d[0]!=5 and d[2]!=5):
                upTurnRight()
                print "上层向右转"
            if (d[0]==5):
                while(a[6]!=d[4]):
                    upTurnRight()
                    print "上层向右转"
                    wholeTurnLeft()
                    print "整体左转"
                LHand()
            

            else:
                while(a[8]!=d[4]):
                    upTurnRight()
                    print "上层向右转"
                    wholeTurnLeft()
                    print "整体左转"
                RHand()


        #白块底层侧面判断
        elif(c[6]==5) or (c[8]==5) or (d[6]==5) or (d[8]==5) or (e[6]==5) or (e[8]==5) or (f[6]==5) or (f[8]==5):
            while(d[6]!=5 and d[8]!=5):
                wholeTurnLeft()
                print "整体左转"
            if(d[6]==5):
                LHand()
            else:
                RHand()
                
        else:
            #白色脚块朝下
            for i in range(4):
                if(d[6]==d[7]):
                    wholeTurnLeft()
                    print "整体左转"
            LHand()

#---------------魔方复原算法第四步：中棱归位

def Step4Position():
    #判断上侧黄色棱块个数
    yb=0 #黄块个数
    while(c[3]!=c[4]) or (d[3]!=d[4]) or (e[3]!=e[4]) or (f[3]!=f[4]):
        yb=0
        if(a[1]==4):
            yb += 1
        if(a[3]==4):
            yb += 1
        if(a[5]==4):
            yb += 1
        if(a[7]==4):
            yb += 1
        if(c[1]==4):
            yb += 1
        if(d[1]==4):
            yb += 1
        if(e[1]==4):
            yb += 1
        if(f[1]==4):
            yb += 1

        if yb<4:
            while(a[7]==4 or d[1]==4):
                upTurnRight()
                print "上层右转"
            while(d[1]!=d[4]):
                upTurnRight()
                print "上层右转"
                wholeTurnLeft()
                print "整体左转"
            if(a[7]==c[4]):
                LHand()
                wholeTurnRight()
                print "整题右转"
                RHand()
            else:
                RHand()
                wholeTurnLeft()
                print "整体左转"
                LHand()
        else:
           while(d[3]==d[4]):
               wholeTurnLeft()
               print "整体左转"
           LHand()
           wholeTurnRight()
           print "整体右转"
           RHand()

#-----------------魔方复原算法第五步：顶棱面位
def TopEdge():
    flag5=1
    while(flag5):
        if(a[1]==4) and (a[3]==4) and (a[5]==4) and (a[7]==4):
            flag5=0
        if(a[3]==4 and a[5]==4) or (a[1]==4 and a[7]==4):
            while(d[1]==4):
                upTurnRight()
                print "上层右转"
            One()
        while(d[1]!=4 or e[1]!=4):
            upTurnRight()
            print "上层右转"
        Round()

#-----------------魔方复原算法第六步：顶角面位
def TopAngel():
    #判定是否为小鱼
    fishFlag=0 #小鱼黄块检测
    while(fishFlag!=4):
        fishFlag=0 
        if a[0]==4:
            fishFlag += 1
        if a[2]==4:
            fishFlag += 1
        if a[6]==4:
            fishFlag += 1
        if a[8]==4:
            fishFlag += 1
        if(fishFlag==1):
            for i in range(4):
                if(a[7]==a[8]==d[0]) or (a[6]==a[7]==d[2]):
                    break
                upTurnRight()
                print "上层向右转"
            if(a[7]==a[8]==d[0]):
                Lfish()
            else:
                Rfish()
            break
        else:
            while(d[0]!=4):
                upTurnRight()
                print "上层向右转"
            Rfish()

#---------------魔方复原算法第七步：顶角归位        
            
def AngerlPosition():
    #判断一对眼睛
    fisheyes = []
    eyes = 0
    for i in range(4):
        if(c[2]==c[5]==c[8]) and (d[0]==d[3]==d[6]):
            eyes += 1
        if(d[2]==d[5]==d[8]) and (e[0]==e[3]==e[6]):
            eyes += 1
        if(e[2]==e[5]==e[8]) and (f[0]==f[3]==f[6]):
            eyes += 1
        if(f[2]==f[5]==f[8]) and (c[0]==c[3]==c[6]):
            eyes += 1
        upTurnRight()
        print "上层向右转"
        fisheyes.append(eyes)
    eyes=max(fisheyes[0],fisheyes[1],fisheyes[2],fisheyes[3])
    if(eyes==0):
        while((c[0]==d[0]==d[2])==1):
            upTurnRight()
            print "上层向右转"
        Round()
        One()
    if(eyes==1):
        while((((c[2]==c[5]==c[8]) and (d[0]==d[3]==d[6])) or ((d[2]==d[5]==d[8]) and (e[0]==e[3]==e[6])) or ((e[2]==e[5]==e[8]) and (f[0]==f[3]==f[6])) or ((f[2]==f[5]==f[8]) and (c[0]==c[3]==c[6])))==1):
            upTurnRight()
            print "上层向右转"
        while(d[2]!=d[5] or e[0]!=e[3]):
            wholeTurnLeft()
            print "整体向左转"
        One()
        Round()
    else:
        #两只眼睛有两种i情况：相邻，相对
        if(c[0]==c[2] or d[0]==d[2] or e[0]==e[2] or f[0]==f[2]):
            while(d[0]!=d[2]):
                upTurnRight()
                print "上层向右转"
            while(d[0]==d[3]):
                upTurnRight()
                print "上层向右转"
                wholeTurnLeft()
                print "整体向左转"
            wholeTurnLeft()
            print "整体向左转"
            One()
            Round()
        else:
            while(((d[2]==d[5] and e[0]==e[3]) or (f[2]==f[5] and c[0]==c[3]))==1):
                upTurnLeft()
                print "上层向左转"
            while((c[2]==c[5] and d[0]==d[3])==1):
                wholeTurnRight()
                print "整体向左转"
            Round()
            One()
                
            
        

#---------------魔方复原算法第八步;顶棱归位
def PoPosition():
    #先判断棱块是否归位
    while((c[0]==c[1] and d[0]==d[1] and e[0]==e[1] and f[0]==f[1])!=1):
        #分两种情况：一面同色，无一面同色
        if(c[0]==c[1] or d[0]==d[1] or e[0]==e[1] or f[0]==f[1]):
            while(f[0]!=f[1]):
                wholeTurnLeft()
                print "整体左转"
            if(d[4]==c[1]):
                Lfish()
                upTurnRight()
                print "上层右转"
                Rfish()
            else:
                Rfish()
                upTurnLeft()
                print "上层左转"
                Lfish()
        else:
            Lfish()
            while((a[6]==a[7]==d[2])==0):
                wholeTurnLeft()
                print "整体左转"
            Rfish()
    while(d[0]!=d[3]):
        upTurnLeft()
        print "上层左转"
      

#--------------函数测试模块------------
def test():
    #One()
    #Round()
    #Lfish()
    #Rfish()
    findWhiteFlower()
    print magicList
    print "---------------------步骤一分隔符----------------------"
    Step2Position()
    print magicList
    print "---------------------步骤二分隔符----------------------"
    Step3Position()
    print magicList
    print "---------------------步骤三分隔符----------------------"
    Step4Position()
    print magicList
    print "---------------------步骤四分隔符----------------------"
    TopEdge()
    print magicList
    print "---------------------步骤五分隔符----------------------"
    TopAngel()
    print magicList
    print "---------------------步骤六分隔符----------------------"
    AngerlPosition()
    print magicList
    print "---------------------步骤七分隔符----------------------"
    PoPosition()
    print magicList
    print "---------------------步骤八分隔符----------------------"

    
#运行
test()
t2=time.time()
print "run step:(times)"
print 257
print "run time:(second)"
print (t2-t1)

          



























