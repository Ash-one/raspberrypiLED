import Animation.AbstractAnimation
import numpy as np
import random
class DotAnimation(AbstractAnimation):
    def __init__(self,yheight,xwidth,x,y,color,count,time=5):
        super.__init__(self,yheight,xwidth,x,y,color)
        self.time = time
        self.timer = 0
        self.count = count


    def createAnimation(self,coordlist):
        #   根据输入的坐标list，将list中所有dot做随机显示效果
        if (self.timer > self.time):
            return None
        coord = []
        for i in range(self.count):
            x = random.randint(coordlist[i][0]-0.5*self.width,  coordlist[i][1]+0.5*self.width)
            y = random.randint(coordlist[i][1]-0.5*self.height, coordlist[i][1]+0.5*self.height)
            coord.append((x,y))
        self.timer += 1
        return coord, self.color






