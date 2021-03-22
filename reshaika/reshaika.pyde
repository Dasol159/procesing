final="no"
def setup():
    size(400,600)
    background(255)
def draw():
    fill(184,145,159)
    rect(250,400,100,50)
    rect(50,400,100,50)
    fill(0)
    textSize(15)
    text(u"Черный",270,430)
    text(u"Белый",70,430)
def mouseClicked():
    if mouseX>250 and mouseX<350 and mouseY>400 and mouseY<450:
        final="fail"
        background(255,0,0)
        textSize(20)
        text(u"ХАХА, БОТ, СЛИТ, РАСИСТ!!!!",50,300)
    if mouseX>50 and mouseX<150 and mouseY>400 and mouseY<450:
        final="win"
        background(0,200,200)
        textSize(20)
        text(u"ПОЗДРАВЛЯЮ ТЫ НЕ РАСИСТ",50,300)
