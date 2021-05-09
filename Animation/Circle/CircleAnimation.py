from Animation.AbstractAnimation import AbsractAnimation


class CircleAnimation(AbsractAnimation):
    def __init__(self,r:int,width=90,height=60):
        super(CircleAnimation, self).__init__(height=height,width=width)
        self.r = r



    def createAnimation(self):
        '''
        生成一个实心圆,以外接正方形左下角为原点
        返回一个坐标list
        '''
        coordlist = []

        for i in range(0,2* self.r):
            for j in range(0,2* self.r):
                if ((i-self.r)**2+(j-self.r)**2)**0.5 <= self.r:
                    coordlist.append((i,j))

        return coordlist

