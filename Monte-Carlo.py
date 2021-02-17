import math
import os
import matplotlib.pyplot as plt
import numpy as np
import random as rand




IN=0
OUT=20


ax=plt.subplots()

plt.fill([0,8,0,0],[0,0,8,0],'b')
plt.fill([0,1,1,0],[4,4,5,5],'w')
plt.fill([4,6,6,4],[0,0,2,2],'w')

for i in range(0,OUT):
    xEx=rand.randrange(0,8)
    yEx=rand.randrange(0,8)
    print('x=',xEx,'y=',yEx)

    if xEx+yEx <=8:
        print('Point in range -x+8 ')
        if xEx+yEx >= 1:
            print('Point in range -x+8 without small kvadrat')
            if xEx+yEx >=4:
                print('Point ...tra-ta-ta big kvadrat')
                IN+=1

S=(64*IN)/OUT
print('S=',S)
    # S fig= S kv * IN / H*W


plt.title("Monte-Carlo's method")
plt.grid(True)

plt.show()
