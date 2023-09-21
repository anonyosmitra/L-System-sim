import matplotlib.pyplot as plt
import numpy as np
from math import radians,sin,cos
R1={"X":"a","F":"b"}
R2={"a":"F+[[X]-X]-F[-FX]+X","b":"FF"}
cmd="X"
fig, ax = plt.subplots()
ax.set_facecolor('black')
for i in range(7):
    for j in R1.keys():
        cmd=cmd.replace(j,R1[j])
    for j in R2.keys():
        cmd=cmd.replace(j,R2[j])
print(cmd)
xs=[0]
ys=[0]
stack=[]
x=0
y=0
a=radians(25)
def plotLine():
    global xs,ys
    ax.plot(np.array(xs),np.array(ys),"g")
    xs.clear()
    ys.clear()

for i in cmd:
    match i:
        case "F":
            x+=cos(a)
            y+=sin((a))
            xs.append(x)
            ys.append(y)
        case "+":
            a+=radians(25)
        case "-":
            a-=radians(25)
        case "[":
            stack.append((x,y,a))
        case "]":
            plotLine()
            x,y,a=stack.pop()
plotLine()
plt.show()