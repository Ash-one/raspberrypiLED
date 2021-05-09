

class AbsractAnimation(object):
    def __init__(self,height,width,sustain):
        self.height = height
        self.width = width
        self.sustain = sustain

    def cutOutRange(self,list:list):
        newlist = []
        for i in list:
            if 0 <= i[0] <= self.width-1 and 0<=i[1]<=self.height-1:
                newlist.append(i)
        return newlist





