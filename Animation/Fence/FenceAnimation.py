import numpy as np
import Animation.AbstractAnimation

class FenceAnimation(AbstractAnimation):
    def __init__(self,yheight,xwidth,x,y,color,count,time=5):
        # count 表示条状数量
        super.__init__(self,yheight,xwidth,x,y,color)
        self.time = time
        self.timer = 0
        self.count = count

    def createAnimation(self):



