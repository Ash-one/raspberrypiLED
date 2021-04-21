import numpy as np
import Animation.Dot.DotAnimation

class SpiralDotAnimation(DotAnimation):
    def __init__(self,yheight,xwidth,x,y,color,count,time=5):
        super.__init__(self,yheight,xwidth,x,y,color,count,time=5)
        self.time = time
        self.timer = 0
        self.count = count


    def createAnimation(self):
        if (self.timer > self.time):
            return None
        coord = []
        for i in range(1, self.count+1):
            theta = i * np.pi / 7.0 * np.exp(-i * 0.001)
            r = 0.03 + 0.07 * theta
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            coord.append((int(x), int(y)))
        self.timer += 1
        return coord, self.color