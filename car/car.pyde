
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
    global tank,tankVerh,tras,trasVerh,pah,pahVerh
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
    global tank,rotat, tras,pah
    imageMode(CENTER)
    rectMode(CENTER)    
    background(0,255,0)
    translate(width / 2, height / 2)
    image(tras,0,0)
    translate(x,y)
    rotate(radians(rotat))
    fill(128, 79, 179)
    image(tank, 0, 0)

    
    
    
    
def keyPressed():
    global x, y, tank, tankVerh, rotat, pah,pahVerh
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
        pah=pahVerh
        image(pah,x,y)
        x=x+1
        y=y+1
