from Animation.AbstractAnimation import AbsractAnimation
import random
import numpy as np

class ExplosionAnimation(AbsractAnimation):
    def __init__(self,sustain=40,count=10,style=0,width=90,height=60):
        '''
        count: 爆炸效果的数量
        style: 0表示方形，1表示十字
        width: 默认宽度90
        height:默认高度60
        '''
        super(ExplosionAnimation, self).__init__(height=height,width=width,sustain=sustain)
        if count < 10:
            self.count = 10
        else:
            self.count = int(count)
        if sustain < 10:
            self.sustain =10
        else:
            self.sustain = sustain
        self.style = style
        self.origin = []


    def createAnimation(self):
        finallist = []
        coordlist = []
        randomlist = []
        for c in range(self.count):
            randomlist.append([random.randint(0,90),random.randint(0,self.width-10)])
        # （theta，distance）
        for r in randomlist:
            coordlist.append(([round(abs((r[1])*np.cos(r[0]))),round(abs((r[1])*np.sin(r[0])))]))
        self.origin = self.cutOutRange(coordlist)
        for frame in range(self.sustain-3):
            finallist.append(self.origin)
        if self.style == 0:
            coordlist=[]
            for c in self.origin:
                coordlist+=self.square2(c)
            finallist.append(self.cutOutRange(coordlist))
            coordlist=[]
            for c in self.origin:
                coordlist+=self.square3([c[0]+1,c[1]+1])
            finallist.append(self.cutOutRange(coordlist))
            coordlist=[]
            for c in self.origin:
                coordlist+=self.square4([c[0]+2,c[1]+2])
            finallist.append(self.cutOutRange(coordlist))
        else:
            coordlist=[]
            for c in self.origin:
                coordlist+=self.cross2(c)
            finallist.append(self.cutOutRange(coordlist))
            coordlist=[]
            for c in self.origin:
                coordlist+=self.cross3([c[0]+1,c[1]+1])
            finallist.append(self.cutOutRange(coordlist))
            coordlist=[]
            for c in self.origin:
                coordlist+=self.cross4([c[0]+2,c[1]+2])
            finallist.append(self.cutOutRange(coordlist))

        return finallist

    def square2(self,coord):
        coords = []
        coords.append(coord)
        coords.append([coord[0]+1,coord[1]])
        coords.append([coord[0],coord[1]-1])
        coords.append([coord[0]+1,coord[1]-1])
        return coords
    def square3(self,coord):
        '''
        以coord作为左上角下面的第一个点
        '''
        coords = []
        coords.append(coord)
        coords.append([coord[0]+2,coord[1]])
        coords.append([coord[0],coord[1]+1])
        coords.append([coord[0]+1,coord[1]+1])
        coords.append([coord[0]+2,coord[1]+1])
        coords.append([coord[0],coord[1]-1])
        coords.append([coord[0]+1,coord[1]-1])
        coords.append([coord[0]+2,coord[1]-1])
        return coords
    def square4(self,coord):
        '''
        以coord作为左上角下面的第一个点
        '''
        coords = []
        coords.append(coord)
        coords.append([coord[0],coord[1]+1])
        coords.append([coord[0],coord[1]-1])
        coords.append([coord[0],coord[1]-2])
        coords.append([coord[0]+3,coord[1]+1])
        coords.append([coord[0]+3,coord[1]])
        coords.append([coord[0]+3,coord[1]-1])
        coords.append([coord[0]+3,coord[1]-2])
        coords.append([coord[0]+1,coord[1]+1])
        coords.append([coord[0]+2,coord[1]+1])
        coords.append([coord[0]+1,coord[1]-2])
        coords.append([coord[0]+2,coord[1]-2])
        return coords

    def cross2(self,coord):
        coords=[]
        if (random.randint(0,10))%2==0:
            #横
            coords.append(coord)
            coords.append([coord[0],coord[1]+1])
            coords.append([coord[0],coord[1]-1])
            coords.append([coord[0]+1,coord[1]])
            coords.append([coord[0]-1,coord[1]])
        else:
            # 斜着
            coords.append(coord)
            coords.append([coord[0]+1,coord[1]+1])
            coords.append([coord[0]+1,coord[1]-1])
            coords.append([coord[0]-1,coord[1]+1])
            coords.append([coord[0]-1,coord[1]-1])
        return coords
    def cross3(self,coord):
        coords=[]
        if (random.randint(0,10))%2==0:
            #横
            coords.append(coord)
            coords.append([coord[0],coord[1]+1])
            coords.append([coord[0],coord[1]-1])
            coords.append([coord[0]+1,coord[1]])
            coords.append([coord[0]-1,coord[1]])
            coords.append([coord[0],coord[1]+2])
            coords.append([coord[0],coord[1]-2])
            coords.append([coord[0]+2,coord[1]])
            coords.append([coord[0]-2,coord[1]])
        else:
            # 斜着
            coords.append(coord)
            coords.append([coord[0]+1,coord[1]+1])
            coords.append([coord[0]+1,coord[1]-1])
            coords.append([coord[0]-1,coord[1]+1])
            coords.append([coord[0]-1,coord[1]-1])
            coords.append([coord[0]+2,coord[1]+2])
            coords.append([coord[0]+2,coord[1]-2])
            coords.append([coord[0]-2,coord[1]+2])
            coords.append([coord[0]-2,coord[1]-2])
        return coords
    def cross4(self,coord):
        coords=[]
        if (random.randint(0,10))%2==0:
            #横
            coords.append(coord)
            coords.append([coord[0],coord[1]+1])
            coords.append([coord[0],coord[1]-1])
            coords.append([coord[0]+1,coord[1]])
            coords.append([coord[0]-1,coord[1]])
            coords.append([coord[0],coord[1]+2])
            coords.append([coord[0],coord[1]-2])
            coords.append([coord[0]+2,coord[1]])
            coords.append([coord[0]-2,coord[1]])
            coords.append([coord[0]-1,coord[1]+1])
            coords.append([coord[0]-1,coord[1]-1])
            coords.append([coord[0]+1,coord[1]+1])
            coords.append([coord[0]+1,coord[1]-1])
        else:
            # 斜着
            coords.append(coord)
            coords.append([coord[0]+1,coord[1]+1])
            coords.append([coord[0]+1,coord[1]-1])
            coords.append([coord[0]-1,coord[1]+1])
            coords.append([coord[0]-1,coord[1]-1])
            coords.append([coord[0]+2,coord[1]+2])
            coords.append([coord[0]+2,coord[1]-2])
            coords.append([coord[0]-2,coord[1]+2])
            coords.append([coord[0]-2,coord[1]-2])
            coords.append([coord[0]+1,coord[1]])
            coords.append([coord[0]-1,coord[1]])
            coords.append([coord[0],coord[1]+1])
            coords.append([coord[0],coord[1]-1])
        return coords