chet=0
mode=5
mode2=5
x=5
modeX=5
y=5
modeY=-5
y1=0
x1=0
x3=200
y3=400
x4=390
x5=0
x6=0
y4=0
y5=0
y6=0
x8=50
y8=10
def setup():
    size(400,600)
    background(255)
def draw():
    global x, modeX, mode, mode2, y, modeY, y1, x1, x8, y8, x3, y3, x4, x5, x6, y4, y5, y6, chet
    background(255)
    fill(153,50,204)
    rect(x3,y3,x8,y8)
    ellipse(x,y,15,15)
    fill(0)
    rect(x4,y4,10,500)
    rect(x5,y5,400,10)
    rect(x6,y6,10,500)
    x=x+int(mode)
    textSize(20)
    fill(153,50,204)
    text(chet,50,50)
    y = y + mode2
    if x >= 380:
        mode=-2
    if x <= 10:
        mode=2
    if y > 600:
         background(255,50,0)
         fill(0,0,0)
         textSize(20)
         text(u"ТЫ ПРОИГРАЛ",135,300)
    if y <= 10:
        mode2=5
    if keyPressed:
        if keyCode == LEFT:
            x3=x3-3
        if keyCode == RIGHT:
            x3=x3+3
    if x>x3 and x<x3+x8 and y>y3 and y<y3+y8:
        mode2=-5
        chet=chet+1
    

