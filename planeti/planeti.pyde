x=1
y = 0
x1=80
x2=150
x3=250
x4=350
x5=450
x6=550
x7=650
x8=750
def setup():
    global x,y
    fullScreen()
    x = width/2
    y = height/2
    background(0)
def draw():
    global x,x1,x2,x3,x4,x5,x6,x7,x8
    translate(x,y)
    fill(255,255,0)
    ellipse(0,0,120,120)
    fill(64, 58, 58)
    ellipse(x1,0,20,20)
    fill(169, 116, 47)
    ellipse(x2,0,25,25)
    fill(66,145,255)
    ellipse(x3,0,45,45)
    fill(255,83,73)
    ellipse(x4,0,30,30)
    fill(145,117,94)
    ellipse(x5,0,60,60)
    fill(205,190,167)
    ellipse(x6,0,65,65)
    fill(162,219,249)
    ellipse(x7,0,70,70)
    
    
    
