import numpy as np
from Animation.AbstractAnimation import AbsractAnimation

class PolygonAnimation(AbsractAnimation):
    def __init__(self,sides:int,edge:int,fill=False,height=60,width=90):
        super(PolygonAnimation, self).__init__(height,width)
        if sides >= 3 and sides <= 4:
            self.sides = sides
        else:
            self.sides = 3
        if edge <= min(height,width):
            self.edge = edge
        else:
            self.edge = 10
        self.fill = fill

    def createAnimation(self):
        coordlist = []
        if self.sides == 3:
            coordlist = self.sides3()
        elif self.sides == 4:
            coordlist = self.sides4()

        return coordlist

    def sides3(self):
        coordlist =[]
        if self.edge%2==1:
            self.edge+=1
        if self.fill == False:
            for i in range(0,self.edge):
                for j in range(0,self.edge):
                    if i==j:
                        coordlist.append((i,j))
                    elif j==0:
                        coordlist.append((i,j))
                    elif i==self.edge-1:
                        coordlist.append((i,j))
        else:
            for i in range(0,self.edge):
                for j in range(0,self.edge):
                    if i-j >=0:
                        coordlist.append((i,j))
        return coordlist

    def sides4(self):
        coordlist = []
        if self.fill == False:
            for i in range(0,self.edge):
                for j in range(0,self.edge):
                    if i==0:
                        coordlist.append((i,j))
                    elif j==0:
                        coordlist.append((i,j))
                    elif i==self.edge-1:
                        coordlist.append((i,j))
                    elif j==self.edge-1:
                        coordlist.append((i,j))
        else:
            for i in range(0,self.edge):
                for j in range(0,self.edge):
                    coordlist.append((i,j))
        return coordlist
