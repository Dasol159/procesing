x=150
y=100
def setup():
    size(400,600)
def draw():
    global x, y
    rectMode(CENTER)
    background(200)
    rect(x,y,100,50)
    if mousePressed and mouseX > x - 50 and mouseX < x + 50 and mouseY > y - 50 and mouseY < y + 50:
        x=mouseX
        y=mouseY
