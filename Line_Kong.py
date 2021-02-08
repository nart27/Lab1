import math

def rand():
    global x
    x=(1664525*x+1013904223)% math.pow(2,32)
    return int(x)

x=1
for i in range(0,10):
    print(rand())
    
# Xn+1=(a*Xn+c)*mod m 
