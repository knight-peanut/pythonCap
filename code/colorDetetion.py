import cv2
import numpy as np


#ÉèÖÃÑÕÉ«'ºì³ÈÀ¶ÂÌ»Æ°×'ÒÀ´ÎÎª[0,1,2,3,4,5]
#ËùÓÃÍ¼Æ¬½ÔÎª560*560ÏñËØ
#-----------------------------------------

#µÃµ½»Ò¶ÈÖµÍ¼Ïñºó×ª»»ÎªhsvÍ¼Ïñ
color = cv2.imread("demo_5.jpg")
hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

#¸ß¶È,¿í¶È
rowA = color.shape[0]
columB = color.shape[1]

#µÃµ½Í¼ÏñÇøÓòµÄÆ½¾ùÏñËØÖµ
def imgCollection(hsv,sizeA,sizeB):
    division = np.sum(np.sum(hsv,axis=1),axis=0)/(sizeA*sizeB)
    return division

#ÅĞ¶ÏÑÕÉ«
def isColor(hsv):
    h=hsv[0]
    s=hsv[1]
    v=hsv[2]
    if(h>=120 and h<=180) or (h>=0 and h<=8) and (s>=50 and s<=200) and (v>=56 and v<=255):
        return 0
    if(h>=11 and h<=20) and (s>=50 and s<=225) and (v>=56 and v<=255):
        return 1
    if(h>=75 and h<=100) and (s>=50 and s<=225) and (v>=56 and v<=225):
        return 2
    if(h>=40 and h<=74) and (s>=50 and s<=225) and (v>=56 and v<=225):
        return 3
    if(h>=21 and h<=38) and (s>=50 and s<=255) and (v>=50 and v<=255):
        return 4
    if(h>=0 and h<=180) and (s>=0 and s<=35) and (v>=180 and v<=255):
        return 5

#²âÊÔÏñËØÓò
def test():
    print imgUp
    print imgCollection(hsv[0:rowA/3,0:columB/3],rowA/3,columB/3)
    print imgCollection(hsv[0:rowA/3,columB/3:columB*2/3],rowA/3,columB/3)
    print imgCollection(hsv[0:rowA/3,columB*2/3:columB],rowA/3,columB/3)
    print imgCollection(hsv[rowA/3:rowA*2/3,0:columB/3],rowA/3,columB/3)
    print imgCollection(hsv[rowA/3:rowA*2/3,columB/3:columB*2/3],rowA/3,columB/3)
    print imgCollection(hsv[rowA/3:rowA*2/3,columB*2/3:columB],rowA/3,columB/3)
    print imgCollection(hsv[rowA*2/3:rowA,0:columB/3],rowA/3,columB/3)
    print imgCollection(hsv[rowA*2/3:rowA,columB/3:columB*2/3],rowA/3,columB/3)
    print imgCollection(hsv[rowA*2/3:rowA,columB*2/3:columB],rowA/3,columB/3)


#Í¼Æ¬µÄ¾Å¸ö¹¬¸ñÒÀ´ÎµÃµ½ËùÊôÑÕÉ«
block1 = isColor(imgCollection(hsv[0:rowA/3,0:columB/3],rowA/3,columB/3))
block2 = isColor(imgCollection(hsv[0:rowA/3,columB/3:columB*2/3],rowA/3,columB/3))
block3 = isColor(imgCollection(hsv[0:rowA/3,columB*2/3:columB],rowA/3,columB/3))
block4 = isColor(imgCollection(hsv[rowA/3:rowA*2/3,0:columB/3],rowA/3,columB/3))
block5 = isColor(imgCollection(hsv[rowA/3:rowA*2/3,columB/3:columB*2/3],rowA/3,columB/3))
block6 = isColor(imgCollection(hsv[rowA/3:rowA*2/3,columB*2/3:columB],rowA/3,columB/3))
block7 = isColor(imgCollection(hsv[rowA*2/3:rowA,0:columB/3],rowA/3,columB/3))
block8 = isColor(imgCollection(hsv[rowA*2/3:rowA,columB/3:columB*2/3],rowA/3,columB/3))
block9 = isColor(imgCollection(hsv[rowA*2/3:rowA,columB*2/3:columB],rowA/3,columB/3))


imgUp=[block1,block2,block3,block4,block5,block6,block7,block8,block9]

test()
