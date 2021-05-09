from Animation.Dot.DotAnimation import DotAnimation
import random

class ShakeDotAnimation(DotAnimation):

    def createAnimation(self):
        '''
        随机生成dot，并对所有dot做shake效果
        返回一个嵌套list，表示多个时间上的显示内容
        '''

        coordlists=[]
        coordlist =[]
        for i in range(self.count):
            x = random.randint(1,self.width-1)
            y = random.randint(1,self.height-1)
            coordlist.append([x,y])
        for i in range(0,self.sustain):
            for c in coordlist:
                plusx = random.randint(-1,1)
                plusy = random.randint(-1,1)
                c[0] = c[0] + plusx
                c[1] = c[1] + plusy
            coordlist = self.cutOutRange(coordlist)
            coordlists.append(coordlist)

        return coordlists


