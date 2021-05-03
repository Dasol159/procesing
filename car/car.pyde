rotat=0
img = 0
imgVerh = 0
x=0
y=0
def setup():
    global img,imgVerh
    fullScreen()
    img = loadImage("pravo.png")
    imgVerh = loadImage("pravo.png")
    imageMode(CENTER)
    rectMode(CENTER)
def draw():
    translate(x,y)
    global img,imgVerh,rotat
    rotate(radians(rotat))
    img = loadImage("pravo.png")
    rect(0, 0, 50, 50)
    background(0,255,0)
    fill(128, 79, 179)
    image(img, 0, 0)
    imageMode(CENTER)
    rectMode(CENTER)
    img = loadImage("tras.png")

    
    
    
    
def keyPressed():
    global x, y, img, imgVerh, rotat
    if key == CODED:
        if keyCode == UP: 
            rotat=rotat-5
            img = imgVerh
        elif keyCode == DOWN:
            rotat=rotat+5
            img = loadImage("pravo.png")
        if keyCode == RIGHT: 
            x = x + cos(radians(rotat)) * 10
            y = y + sin(radians(rotat)) * 10
            img = loadImage("pravo.png")

        elif keyCode == LEFT:
            x = x - cos(radians(rotat)) * 10
            y = y - sin(radians(rotat)) * 10
            img = loadImage("pravo.png")
