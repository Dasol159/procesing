x=1
y = 0
x1=100
x2=170
x3=270
x4=370
x5=470
x6=570
x7=670
x8=770
angle=1
angle1=1
angle2=1
angle3=1
angle4=1
angle5=1
angle6=1
angle7=1
angle8=1
mode="по часовой"
def setup():
    global x,y
    fullScreen()
    x = width/2
    y = height/2
    background(0)
def draw():
    global x,x1,x2,x3,x4,x5,x6,x7,x8,mode
    global angle,angle1,angle2,angle3,angle4,angle5,angle6,angle7,angle8
    background(0)
    translate(x,y)
    push()
    fill(255,255,0)
    ellipse(0,0,120,120)
    pop()
    push()
    rotate(radians(angle1))
    fill(64, 58, 58)
    ellipse(x1,0,20,20)
    pop()
    push()
    rotate(radians(angle2))
    fill(169, 116, 47)
    ellipse(x2,0,25,25)
    pop()
    push()
    rotate(radians(angle3))
    fill(66,145,255)
    ellipse(x3,0,45,45)
    pop()
    push()
    rotate(radians(angle4))
    fill(255,83,73)
    ellipse(x4,0,30,30)
    pop()
    push()
    rotate(radians(angle5))
    fill(145,117,94)
    ellipse(x5,0,60,60)
    pop()
    push()
    rotate(radians(angle6))
    fill(205,190,167)
    ellipse(x6,0,65,65)
    pop()
    push()
    rotate(radians(angle7))
    fill(162,219,249)
    ellipse(x7,0,70,70)
    pop()
    push()
    rotate(radians(angle8))
    fill(29,110,254)
    ellipse(x8,0,80,80)
    pop()
    angle=angle+1
    angle1=angle1+0.9
    angle2=angle2+0.8
    angle3=angle3+0.7
    angle4=angle4+0.6
    angle5=angle5+0.5
    angle6=angle6+0.4
    angle7=angle7+0.3
    angle8=angle8+0.2
    
    
    
