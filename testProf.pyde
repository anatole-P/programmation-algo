ballX = 0
ballY = 0

ballSpeed = 0.2
ballSpeedX = 0
ballSpeedY = 0
ballAngle = PI/5

ballRadius = 10
ballAngleMax = PI/1.9

racketWidth = 100
racketHeight = 10
racketX = 0
racketY = 0

lastFrameTime = 0
deltaTime = 0

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    #on dit qu'on va faire référence à la variable global
    global ballX, ballY, racketX, racketY, racketWidth
    global lastFrameTime
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(600, 600)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(244)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 50
    
    lastFrameTime = millis()
    
def draw():
    global deltaTime, lastFrameTime
    
    clear()
    
    deltaTime = millis() - lastFrameTime
    lastFrameTime = millis()
    
    drawRacket()
    drawBall()
    drawBricks()
    
    
    
def drawRacket():
    global racketX, racketY, racketWidth, racketHeight
    fill(255)
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, racketHeight, 6)
    
def drawBall():
    global ballX, ballY, ballRadius, ballAngle, ballSpeed, ballSpeedX, ballSpeedY
    global racketX, racketY, racketWidth, racketHeight
    global deltaTime
    global ballAngleMax
    
    #idem a ce qu'il y a au dessus
    ballSpeedX = cos(ballAngle) * ballSpeed * deltaTime
    ballSpeedY = sin(ballAngle) * ballSpeed * deltaTime
    ballX += ballSpeedX
    ballY -= ballSpeedY
    
    #haut et bas   
    if(ballY-ballRadius < 0):
        ballAngle = -ballAngle
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballAngle = -ballAngle
        ballY = height-ballRadius
    
    #droite et gauche
    if(ballX+ballRadius > width):
        ballAngle = PI - ballAngle
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballAngle = PI - ballAngle
        ballX = ballRadius
    
    if(racketY < ballY+ballRadius < racketY+racketHeight and ballSpeedY < 0):
        if(racketX < ballX < racketX + racketWidth):
            ratio = (ballX - racketX - racketWidth/2) / (racketWidth/2)
            ballAngle = PI/2 - ratio * ballAngleMax
            ballY = racketY-ballRadius
    
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius);
    
def drawBricks():
    
    global ballX, ballY, ballRadius, ballSpeedX, ballSpeedY, ballAngle
    
    bX = 150
    bY = 250
    bW = 150
    bH = 100
    
    rect(bX, bY, bW, bH)
   
    if (bY+bH >= ballY+ballRadius >= bY and bX+bW>= ballX >= bX):
        ballAngle = -ballAngle

        ballY = bY-ballRadius
    elif(bY < ballY-ballRadius <= bY + bH and bX+bW>= ballX >= bX):
        ballAngle = -ballAngle

        ballY = bY+bH+ballRadius

    if (bX+bW >= ballX+ballRadius >= bX and bY+bH>= ballY >= bY):
        ballAngle = PI-ballAngle

        ballX = bX-ballRadius
    elif(bX < ballX-ballRadius <= bX + bW and bY+bH>= ballY >= bY):
        ballAngle = PI-ballAngle

        ballX = bX+bW+ballRadius
 


    
    
    
