x=10
y=10
x1=10
def setup():
    size(600,600)
    background(255)

def draw():
    global x, y, x1


    strokeWeight(tolsh)
    if keyPressed:
        if key == 'w' or key == 'W':
            
        if key == 's' or key == 'S':

        if key == '1':
            stroke(129,223,122)
        if key == '2':
            stroke(209,243,6)
        if key == '3':
            stroke(63,165,203)
        if key == '4':
            stroke(247,150,4)
        if key == '5':
            stroke(254,195,124)
        if key == '6':
            stroke(93,190,246)
        if key == '7':
            stroke(7,237,217)
        if key == '8':
            stroke(59,17,97)
        if key == '9':
            stroke(228,145,244)
        if key == '0':
            stroke(60,130,166)
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
