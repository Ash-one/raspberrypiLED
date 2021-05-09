import numpy as np
from Animation.AbstractAnimation import AbsractAnimation
from math import floor
class FenceAnimation(AbsractAnimation):
    def __init__(self,sustain=40,count=5,square=True,across=True,height=60,width=90):
        # count 表示条状数量
        super(FenceAnimation,self).__init__(height,width,sustain)
        self.count = count
        self.edgewidth = 3
        self.square = square
        self.across = across

    def createAnimation(self):
        '''
        生成一个栅栏,以外接正方形左下角为原点,返回时以灯阵原点为原点
        返回一个坐标list
        '''
        edge = int((2*self.count - 1)*self.edgewidth)
        coordlist = []

        if self.across == False:
            # 竖状栅栏
            for i in range(0,edge):
                if floor(i/self.edgewidth)%2 == 0:
                    for j in range(0,edge):
                        coordlist.append([i,j])
                else:
                    pass
        else:
            # 横状栅栏
            for j in range(0,edge):
                if floor(j/self.edgewidth)%2 == 0:
                    for i in range(0,edge):
                        coordlist.append([i,j])
                else:
                    pass
        newlist=[]
        newlist2 = []
        for c in coordlist:
            c = [c[0]-edge/2,c[1]-edge/2]
            newlist.append(c)
        for i in newlist:
            i = [int(i[0]+self.width/2),int(i[1]+self.height/2)]
            newlist2.append(i)
        newlist2 = self.cutOutRange(newlist2)

        finallist = []
        for i in range(self.sustain):
            finallist.append(newlist2)

        if self.square == True:
            return finallist
        else:
            # 如果为圆形栅栏，则判断每个点是否距离圆心小于半径
            list=[]
            list2 = []
            for coord in newlist:
                if ((coord[0])**2+(coord[1])**2)**0.5 < edge/2:
                    list.append(coord)
            for i in list:
                i = [int(i[0]+self.width/2),int(i[1]+self.height/2)]
                list2.append(i)
            list2 = self.cutOutRange(list2)
            finallist = []
            for i in range(self.sustain):
                finallist.append(list2)
            return finallist















