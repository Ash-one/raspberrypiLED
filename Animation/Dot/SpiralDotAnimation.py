import numpy as np
from Animation.Dot.DotAnimation import DotAnimation

class SpiralDotAnimation(DotAnimation):

    def createAnimation(self):
        '''
        生成阿基米德螺旋线
        返回一个list
        '''
        coord = []
        coordlist = []
        for i in range(1, int(self.count+1)):
            # theta = i * np.pi/7 * np.exp(-i * 0.01)
            theta = i * 0.5
            r = 1 + 2 * theta
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            coord.append([round(x), round(y)])
        for c in range(len(coord)):
            coordlist.append([coord[c][0]+self.width/2,coord[c][1]+self.height/2])
        coordlist = self.cutOutRange(coordlist)
        finallist = []
        for i in range(self.sustain):
            finallist.append(coordlist)
        return finallist