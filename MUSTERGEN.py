#COLOR PALLET IG
import tkinter as tk
import random
import time


#setting ig
biggness =1    #visiuel size
size = 1000      #size(3-250)        (100)
rand = 2        #random change(0-255)   (5)
rand2 = 2       #chance to change(0-255)       (2)
show="x"          # when to draw 1 always "x" when finished (higher faster loading)

#variables
size2 = size**2
ticks=0
nt=0
ot=0
green = []
red = []
blue = []

#cord:(red,green,blue)
#d={size2//2+size//2:(0,138,128)} #cyan in middle
#d={size2//2+size//2:(128,0,128)} #purple in middle
d={size2//2:(0,138,128),size2//2+size-1:(128,0,128)}
#d={size2//2:(255, 192, 203),size2//2+size-1:(255, 255, 0)}



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
    global cube,green,red,blue,biggness
    x = 0
    y = biggness*size
    weg = 0
    canvas.delete("all")
    cube = canvas.create_rectangle(0, 0, size * biggness, size * biggness, fill="white",outline="black")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if green[weg]!="X" and green[weg]!="x":
                if blue[weg]<0: blue[weg]=0
                if blue[weg]>255: blue[weg]=255
                if red[weg]<0: red[weg]=0
                if red[weg]>255: red[weg]=255
                if green[weg]<0: green[weg]=0
                if green[weg]>255: green[weg]=255
                farbe = f"#{red[weg]:02x}{green[weg]:02x}{blue[weg]:02x}"
            else:
                farbe ="Black"
            cube = canvas.create_rectangle(x, y, x + biggness, y - biggness, fill=farbe,outline=farbe)
            weg = weg + 1
            x = x + biggness
        x = 0
        y = y - biggness






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
    else:
        ticks+=1
        window.after(1, tick)
        ot = nt
        nt = time.time()
        print("ms:",(nt-ot)*1000)

#and ( and(weg+1)%size!=size-1 and (weg+1)>=size and (weg+1)<=(size2-size))

render()
tick()

window.mainloop()# Schreibe hier Deinen Code :-)
