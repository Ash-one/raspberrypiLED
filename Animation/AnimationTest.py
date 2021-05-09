from Animation.Fence.FenceAnimation import FenceAnimation
from Animation.Dot.DotAnimation import DotAnimation
from Animation.Dot.ShakeDotAnimation import ShakeDotAnimation
from Animation.Dot.SpiralDotAnimation import SpiralDotAnimation
from Animation.Circle.CircleAnimation import CircleAnimation
from Animation.Polygon.PolygonAnimation import PolygonAnimation
from Animation.Explosion.ExplosionAnimation import ExplosionAnimation
import matplotlib.pyplot as plt
import numpy as np

ani = FenceAnimation(sustain=40,count=8,square=True )
ani2 = ExplosionAnimation(sustain=40)

l = ani.createAnimation()[39]
l2 = ani2.createAnimation()[39]

newlist = l+l2

# print(l,len(l),len(l[0]),len(l[0][0]))
print(newlist)
m = np.array(newlist)
x = m[:,0]
y = m[:,1]

plt.scatter(x,y)#画散点图
plt.show()

