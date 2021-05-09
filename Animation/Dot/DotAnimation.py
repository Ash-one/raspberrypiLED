from Animation.AbstractAnimation import  AbsractAnimation
import numpy as np
import random

class DotAnimation(AbsractAnimation):
    def __init__(self,sustain=40,count=10,height=60,width=90):
        super(DotAnimation,self).__init__(height,width,sustain)
        self.count = int(count)


    def createAnimation(self):
        '''
        随机生成dot并显示
        返回一个dot的list
        '''
        coordlist = []
        for i in range(self.count):
            x = random.randint(0,self.width)
            y = random.randint(0,self.height)
            coordlist.append((x,y))

        return coordlist






