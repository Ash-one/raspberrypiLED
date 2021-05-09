import time
from neopixel import *
import argparse

class GLED(object):
    def __init__(self,count,pin,len,height):
        LED_COUNT      = count       # 灯的数目
        LED_PIN        = pin      # 树莓派.管脚口 BCM18引脚PWM BCM12引脚PCM 
        LED_FREQ_HZ    = 800000  
        LED_DMA        = 10      
        LED_BRIGHTNESS = 10        # 全局亮度    （0-255）
        LED_INVERT     = False   
        LED_CHANNEL    = 0  

        self.count = count
        self.xlen = len
        self.yheight  = height   
        
        self.matrix = LEDMatrix(num=LED_COUNT, pin=LED_PIN, len=len, height=height,freq_hz=LED_FREQ_HZ, dma=LED_DMA, invert=LED_INVERT, brightness=LED_BRIGHTNESS, channel=LED_CHANNEL)
        self.matrix.begin()
        print('--灯阵初始化成功--')
    
    def getMatrixSize(self):
        return (self.xlen,self.yheight)
    
    def getBrightness(self):
        return self.matrix.getBrightness()
    
    def setBrightness(self,br):
        self.matrix.setBrightness(br)

    def clearMatrix(self):
        self.setAllColor(Color(0,0,0))
        self.matrix.show()

    def getVitualPos(self,num):
        x = int(num/self.yheight)
        if (x%2==0):
            y = num - x * self.yheight
        else:
            y = self.yheight - num + x*self.yheight - 1 
        return x,y

    def showAllColor(self,color):
        for i in range(self.count):
            xx,yy = self.getVitualPos(i)
            self.matrix.setPixelColor(xx, yy, color)
        self.matrix.show()
    
    # 根据list中的坐标和颜色生成图像
    def showListColor(self,list,color):
	    for (xx,yy) in list:
		    self.matrix.setPixelColor(xx, yy, color)
	    self.matrix.show()
    
    # 设置图像平移
    def showListTranslation(self,list,color,step=1,direction='right',wait_ms=50):
        newlist = []
        for (xx,yy) in list:
            self.matrix.setPixelColor(xx, yy, color)
            if(direction=='right'):
                if(xx+step <= self.xlen):
                    newlist.append((xx+step,yy))
            elif (direction=='left'):
                if(xx-step >=0):
                    newlist.append((xx-step,yy))
            elif (direction=='up'):
                if(yy+step <= self.yheight):
                    newlist.append((xx,yy+step))
            elif (direction=='down'):
                if(yy-step >= 0):
                    newlist.append((xx,yy-step))
        self.matrix.show()
        time.sleep(wait_ms/1000.0)
        # 暂定图像移动出灯阵后停止函数
        if(newlist != NULL):
            self.setListTranslation(newlist,color,step=step,direction=direction,wait_ms=wait_ms)
        else:
            return

    # 设置异步频闪|交叉闪烁
    def showCrossFlash(self,color,wait_ms=50):
        even = []       # 偶数位置
        uneven = []     # 奇数位置
        for i in range(self.xlen):
            for j in range(self.yheight):
                if ((i+j)%2==0):
                    even.append((i,j))
                else:
                    uneven.append((i,j))
        while(True):
            self.setListColor(even,color)
            self.matrix.show()
            time.sleep(wait_ms/1000.0)
            self.setListColor(uneven,color)
            self.matrix.show()
            time.sleep(wait_ms/1000.0)
    
    def wheel(self,x,max):
        x = np.around(255/(max-1-0)*(x-0))  # 将0-59或0-89转换到0-255的rgb区间
        if x < 85:
            return Color(x * 3, 255 - x * 3, 0)
        elif x < 170:
            x -= 85
            return Color(255 - x * 3, 0, x * 3)
        else:
            x -= 170
            return Color(0, x * 3, 255 - x * 3)

    # 彩虹流动 
    def showRainbowCycle(self,direction='x',wait_ms=50,iteration=1):
        if(direction=='x'):
            for i in xlen*iteration:
                for i in range(self.xlen):
                    self.setXLineColor(i,wheel(i+j,xlen))
                self.matrix.show()
                time.sleep(wait_ms/1000.0)
        elif(dirction=='y'):
            for i in yheight*iteration:
                for i in range(self.yheight):
                    self.setYLineColor(i,wheel(i+j,yheight))
                self.matrix.show()
                time.sleep(wait_ms/1000.0)

    def setXLineColor(self,x,color):
        for i in range(self.yheight):
            self.matrix.setPixelColor(x,i,color)

    def setYLineColor(self,y,color):
        for i in range(self.xlen):
            self.matrix.setPixelColor(i,y,color)
    


    #彩虹色整体统一柔和渐变-每个灯颜色同一时间相同
    def rainbow(self, wait_ms=20, iterations=1):
        for j in range(256*iterations):
            for i in range(self.yheight):
                self.matrix.setPixelColor(i, self.wheel((i+j) & 255))
            self.matrix.show()
            time.sleep(wait_ms/1000.0)
    #彩虹色每一个灯各自柔和渐变-每个灯颜色同一时间不同
    def rainbowCycle(self, wait_ms=20, iterations=5):
        for j in range(256*iterations):
            for i in range(self.yheight):
                self.matrix.setPixelColor(i, self.wheel((int(i * 256 / self.yheight) + j) & 255))
            self.matrix.show()
            time.sleep(wait_ms/1000.0)
    #彩虹色统一闪烁流动变色-每个灯颜色同一时间相同
    def theaterChaseRainbow(self,wait_ms=50):
        for j in range(256):
            for q in range(3):
                for i in range(0, self.yheight, 3):
                    self.matrix.setPixelColor(i+q, self.wheel((i+j) % 255))
                self.matrix.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.yheight, 3):
                    self.matrix.setPixelColor(i+q, 0)




    def setCrossColor(self,x1,y1,x2,y2,color):
        if((x2-x1)==(y2-y1)):
            for i in range(x2-x1):
                self.matrix.setPixelColor(x1+i,y1+i,color)
                self.matrix.setPixelColor(x2-i,y1+i,color)
            # self.matrix.show()
        else:
            print('unaviliable input')
  


class LEDMatrix(Adafruit_NeoPixel):
    def __init__(self, num, pin, len, height, freq_hz=800000, dma=10, invert=False,
                    brightness=255, channel=0, strip_type=ws.WS2811_STRIP_RGB):
        Adafruit_NeoPixel.__init__(self, num, pin, freq_hz=800000, dma=10, invert=False,
                    brightness=255, channel=0, strip_type=ws.WS2811_STRIP_RGB)
        self.len = len       # x
        self.height = height # y

    def getPhysicsPos(self,x,y):
        # print('len=',self.len,'height=',self.height)
        if (x < self.len and y < self.height):
            if(x%2==0):
                n = self.height * x + y
            else:
                n = self.height * (x+1) - y - 1
            return n
        else:
            return None

    def setPixelColor(self,x,y,color):
        n = self.getPhysicsPos(x,y)
        # print(x,y,n)
        self._led_data[n] = color

    def setPixelColorRGB(self,x,y,red,green,blue,white = 0):
        self.setPixelColor(x,y,Color(red,green,blue,white))

    def getPixelColor(self,x,y):
        n = self.getPhysicsPos(x,y)
        return self._led_data[n]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    myled = GLED(count=5400,pin=12,len=90,height=60) # count=len*height

    try:
        while True:
            myled.showAllColor(Color(255,0,0))

    except KeyboardInterrupt:
        if args.clear:
            myled.clearMatrix()


    


