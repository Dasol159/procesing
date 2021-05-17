rejim=0
x1=0
y1=0
rotat=0
tank = 0
tankVerh = 0
x=0
y=0
tras=0
trasVerh=0
pah=0
pahVerh=0
def setup():
    frameRate(30)
    global tank,tankVerh,tras,trasVerh,pah,pahVerh,x1,y1
    fullScreen()
    imageMode(CENTER)
    rectMode(CENTER)    
    tank = loadImage("pravo.png")
    tankVerh = loadImage("pravo.png")
    tras = loadImage("tras.png")
    trasVerh = loadImage("tras.png")
    pah = loadImage("pah.png")
    pahVerh = loadImage("pah.png")
def draw():
    global tank,rotat, tras,pah,x1,y1,rejim
    rejim="не стрелять"
    
    imageMode(CENTER)
    rectMode(CENTER)    
    background(0,255,0)
    push()
    translate(width / 2, height / 2)
    image(tras,0,0)
    translate(x,y)
    rotate(radians(rotat))
    fill(128, 79, 179)
    #image(tank, 0, 0)
    image(tank, 0, 0, 300, 200)   
    pop()
    if rejim == "cтрелять":
            image(pah,x1,y1)
            x1=x1+1
    elif rejim == "не стрелять":
            pah=pahVerh    
def keyPressed():
    global x, y, tank, tankVerh, rotat, pah,pahVerh,x1,y1,rejim
    if key == CODED:
        if keyCode == LEFT: 
            rotat=rotat-5
            tank = tankVerh
        elif keyCode == RIGHT:
            rotat=rotat+5
            tank = loadImage("pravo.png")
        if keyCode == UP: 
            x = x + cos(radians(rotat)) * 10
            y = y + sin(radians(rotat)) * 10
            tank = loadImage("pravo.png")
        elif keyCode == DOWN:
            x = x - cos(radians(rotat)) * 10
            y = y - sin(radians(rotat)) * 10
            tank = loadImage("pravo.png")
        if key == " ":
            rejim="стрелять"
            image(pah,x1,y1)
            x1=x
            y1=y
