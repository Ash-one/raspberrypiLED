import time
from neopixel import *
import argparse
from Audio.tools import Pixel
import numpy as np


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
    # 根据Pixellist中的Pixel对象中坐标和颜色生成图像
    def showPixelList(self,PixelList):
        for pixel in PixelList:
            self.matrix.setPixel(pixel)
        self.matrix.show()

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

    def setXLineColor(self,x,color):
        for i in range(self.yheight):
            self.matrix.setPixelColor(x,i,color)

    def setYLineColor(self,y,color):
        for i in range(self.xlen):
            self.matrix.setPixelColor(i,y,color)


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
    def setPixel(self,Pixel):
        n = self.getPhysicsPos(Pixel.coord[0],Pixel.coord[1])
        self._led_data[n] = Color(Pixel.rgb[0],Pixel.rgb[1],Pixel.rgb[2])

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





