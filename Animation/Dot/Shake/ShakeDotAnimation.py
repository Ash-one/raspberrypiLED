import Animation.Dot.DotAnimation
import random


class ShakeDotAnimation(DotAnimation):
    def __init__(self,yheight,xwidth,x,y,color,count,time=5):
        super.__init__(self,yheight,xwidth,x,y,color,count,time)
        self.time = time
        self.timer = 0
        self.count = count

    def createAnimation(self, coordlist):
        #   根据输入的坐标list，将list中所有dot做shake效果
        #
        #

        if (self.timer > self.time):
            return None
        coord = []
        for i in range(0, self.count):
            plusx = random.randint(-1,1)
            plusy = random.randint(-1,1)
            x = coordlist[i][0] + plusx
            y = coordlist[i][1] + plusy

            coord.append((int(x), int(y)))
        self.timer += 1
        return coord, self.color