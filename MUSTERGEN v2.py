#COLOR PALLET IG
import tkinter as tk
import random
import time



# v2 better loading speeds
#setting ig
biggness= 4   #visiuel size(1-...)           (5)     (2)     (1)      (1)
size=100     #size(3-250)                   (100)   (250)   (500)    (1000)
rand=4        #random change(0-255)          (4-5)   (3-4)   (2-3)    (1-2)
rand2=2       #chance to change(0-255)       (2)     (2)     (2)      (2)
#time         #the average time              (1s)    (8s)    (1.1min) (8.5min)
show=1          # when to draw 1 always "x" when finished (higher faster loading)

#variables
size2 = size**2
ticks=0
nt=0
ot=0
green = []
red = []
blue = []
tt=time.time()

#cord:(red,green,blue)
#d={size2//2+size//2:(0,138,128)} #cyan in middle
#d={size2//2+size//2:(128,0,128)} #purple in middle
#d={size2//2:(0,138,128),size2//2+size-1:(128,0,128)}#both pruple and cyan
#d=dict((random.randint(0,size2),tuple([random.randint(0,255) for i in range(3)])) for i in range(10))
d={size2//2:(255, 192, 203),size2//2+size-1:(255, 255, 0)}#custom



window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * biggness) + "x" + str(size * biggness))
canvas = tk.Canvas(window, width=(size * biggness), height=(size * biggness), bg="white")
canvas.pack()


def reset():
    global green,red,blue
    for i in range(size):
        red.append("x")
        green.append("x")
        blue.append("x")
    for i in range(size-2):
        red.append("x")
        green.append("x")
        blue.append("x")
        for i in range(size-2):
            red.append("X")
            green.append("X")
            blue.append("X")
        red.append("x")
        green.append("x")
        blue.append("x")
    for i in range(size):
        red.append("x")
        green.append("x")
        blue.append("x")
    for i in d:
        red[i]=d[i][0]
        green[i]=d[i][1]
        blue[i]=d[i][2]
reset()

def render():
    global cube,green,red,blue,biggness,size
    x=0
    y=biggness*size
    weg=0
    canvas.delete("all")
    img=tk.PhotoImage(width=size,height=size)
    for y in range(size):
        row=[]
        for x in range(size):
            weg=y*size+x
            if green[weg]=="X" or green[weg]=="x":
                row.append("#000000")
            else:
                color=f"#{max(0,min(255,red[weg])):02x}{max(0,min(255,green[weg])):02x}{max(0,min(255,blue[weg])):02x}"
                row.append(color)
        img.put("{" + " ".join(row) + "}", to=(0, y))
    scaled = img.zoom(biggness, biggness)
    canvas.image = scaled
    canvas.delete("all")
    canvas.create_image(0, 0, image=scaled, anchor="nw")





def tick():
    global cube,green,red,blue,rand,size,size2,ticks,show,nt,ot
    change=[]
    for i in range(size2):
        change.append(0)
    weg=0
    for i in range(size2-1):
        if green[weg]!="X" and green[weg]!="x" and change[weg]==0 and random.randint(0,rand2)==0:

            if weg+1<size2 and green[weg+1]=="X" and ((weg+1)%size!=0 and (weg+1)>=size and (weg+1)<=(size2-size)and(weg+1)%size!=size-1):
                green[weg+1]=green[weg]+random.randint(-rand,rand)
                blue[weg+1]=blue[weg]+random.randint(-rand,rand)
                red[weg+1]=red[weg]+random.randint(-rand,rand)
                change[weg+1]=1

            if weg-1>=0 and green[weg-1]=="X" and ((weg-1)%size!=0 and (weg-1)>=size and (weg-1)<=(size2-size)and(weg-1)%size!=size-1):
                green[weg-1]=green[weg]+random.randint(-rand,rand)
                blue[weg-1]=blue[weg]+random.randint(-rand,rand)
                red[weg-1]=red[weg]+random.randint(-rand,rand)
                change[weg-1]=1

            if weg+size<size2 and green[weg+size]=="X" and ((weg+size)%size!=0 and (weg+size)>=size and (weg+size)<=(size2-size)and(weg+size)%size!=size-1):
                green[weg+size]=green[weg]+random.randint(-rand,rand)
                blue[weg+size]=blue[weg]+random.randint(-rand,rand)
                red[weg+size]=red[weg]+random.randint(-rand,rand)
                change[weg+size]=1

            if weg-size>=0 and green[weg-size]=="X" and ((weg-size)%size!=0 and (weg-size)>=size and (weg-size)<=(size2-size)and(weg-size)%size!=size-1):
                green[weg-size]=green[weg]+random.randint(-rand,rand)
                blue[weg-size]=blue[weg]+random.randint(-rand,rand)
                red[weg-size]=red[weg]+random.randint(-rand,rand)
                change[weg-size]=1

        weg=weg+1
    if show!="x" and ticks >=show :
        ticks=0
        render()
        window.after(1, tick)
    elif (not("X" in green)):
        render()
        print("sec:",time.time()-tt)
    else:
        ticks+=1
        window.after(1, tick)
        ot = nt
        nt = time.time()
        print("ms:",(nt-ot)*1000,"left:",green.count("X"))
render()
tick()

window.mainloop()
