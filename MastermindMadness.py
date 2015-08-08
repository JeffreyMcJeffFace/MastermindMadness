#Jeff Luxmore
#Simple visual interface for mastermind.
#Note that the graphics file was saved in the visual folder of python.

from graphics import *
from random import randrange
import time
import math

##########################-Visuals-#########################################

def createHiddenDots():
    g1dot1=g1dot2=g1dot3=g1dot4=0
    g2dot1=g2dot2=g2dot3=g2dot4=0
    g3dot1=g3dot2=g3dot3=g3dot4=0
    g4dot1=g4dot2=g4dot3=g4dot4=0
    g5dot1=g5dot2=g5dot3=g5dot4=0
    g6dot1=g6dot2=g6dot3=g6dot4=0
    g7dot1=g7dot2=g7dot3=g7dot4=0

    g1dots=[g1dot1, g1dot2, g1dot3, g1dot4]
    g2dots=[g2dot1, g2dot2, g2dot3, g2dot4]
    g3dots=[g3dot1, g3dot2, g3dot3, g3dot4]
    g4dots=[g4dot1, g4dot2, g4dot3, g4dot4]
    g5dots=[g5dot1, g5dot2, g5dot3, g5dot4]
    g6dots=[g6dot1, g6dot2, g6dot3, g6dot4]
    g7dots=[g7dot1, g7dot2, g7dot3, g7dot4]

    masterDots=[g1dots,g2dots,g3dots,g4dots,g5dots,g6dots,g7dots]

    for i in range(7):
        for x in range(4):
            masterDots[i][x]=Circle(Point(3.5+2.5*x,2+3*i),1)
    return masterDots

def createResultObjects(win):

    ob1Dot1=ob1Dot2=ob1Dot3=ob1Dot4=0
    ob2Dot1=ob2Dot2=ob2Dot3=ob2Dot4=0
    ob3Dot1=ob3Dot2=ob3Dot3=ob3Dot4=0
    ob4Dot1=ob4Dot2=ob4Dot3=ob4Dot4=0
    ob5Dot1=ob5Dot2=ob5Dot3=ob5Dot4=0
    ob6Dot1=ob6Dot2=ob6Dot3=ob6Dot4=0
    ob7Dot1=ob7Dot2=ob7Dot3=ob7Dot4=0

    g1objects=[ob1Dot1,ob1Dot2,ob1Dot3,ob1Dot4]
    g2objects=[ob2Dot1,ob2Dot2,ob2Dot3,ob2Dot4]
    g3objects=[ob3Dot1,ob3Dot2,ob3Dot3,ob3Dot4]
    g4objects=[ob4Dot1,ob4Dot2,ob4Dot3,ob4Dot4]
    g5objects=[ob5Dot1,ob5Dot2,ob5Dot3,ob5Dot4]
    g6objects=[ob6Dot1,ob6Dot2,ob6Dot3,ob6Dot4]
    g7objects=[ob7Dot1,ob7Dot2,ob7Dot3,ob7Dot4]

    resultObjects=[g1objects,g2objects,g3objects,
                   g4objects,g5objects,g6objects,g7objects]

    #Make circle and set initial color assignments for peg dots.           
    for i in range(7):
        for x in range(4):
            resultObjects[i][x]=Circle(Point(13.2+(x%2), 1.5+(i*3)+(x/2)), .4)
            resultObjects[i][x].setFill("gray")

    #outputKey will track the color of each result dot as
    #the graphics package offers no getColor function. 
    global outputKey
    outputKey=[[1,1,1,1],
               [1,1,1,1],
               [1,1,1,1],
               [1,1,1,1],
               [1,1,1,1],
               [1,1,1,1],
               [1,1,1,1]] 

    return resultObjects

#This will draw four colored dots to represent guess.
def showGuess(guess,code,win):
    drawObjects(guess,win)
    animate(guess,win)
    for i in range(4):
        if code[i]=="c": color="cyan"
        if code[i]=="p": color="purple"
        if code[i]=="b": color="blue"
        if code[i]=="g": color="green"
        if code[i]=="y": color="yellow"
        if code[i]=="r": color="red"
        masterDots[guess][i].undraw()
        masterDots[guess][i].setFill(color)
        masterDots[guess][i].draw(win)
        
#This will draw the other visual objects for a guess line.
def drawObjects(guess,win):
    Text(Point(1.5, 2+(3*guess)), str(guess+1)).draw(win)
    Rectangle(Point(15.5, 1.2+(3*guess)),Point(18.5, 2.8+(guess*3))).draw(win)
    Text(Point(17, 2+(guess*3)), "Submit").draw(win)
    Rectangle(Point(12.7, 1+(guess*3)), Point(14.7, 3+(guess*3))).draw(win)
    for i in range(4):
        resultObjects[guess][i].draw(win)
        
def animate(guess, win):
    colors=["red","blue","purple","green","yellow","cyan"]
    for i in range(10):
        for x in range(4):
            masterDots[guess][x].undraw()
            masterDots[guess][x].setFill(colors[randrange(0,6)])
            masterDots[guess][x].draw(win)
            time.sleep(.01)

#Controls user clicks on result dots. A click on the submit button will
#exit loop and send result for computer to make next guess.
def outputClicks(guess,win):
    submitGuess=0
    click=win.getMouse()
    if click.x>=15.5 and click.x<=18.5:
        if click.y>=(1.2+guess*3) and click.y<=(2.8+guess*3):
            submitGuess=1
    while submitGuess==0:
        row=column=editDot=5
        if click.x>=12.8 and click.x<=13.6:
            column=1
        if click.x>=13.8 and click.x<=14.6:
            column=2
        if click.y>=(1.1+guess*3) and click.y<=(1.9+guess*3):
            row=1
        if click.y>=(2.1+guess*3) and click.y<=(2.9+guess*3):
            row=2
        if row==1 and column==1: editDot=0
        if row==2 and column==1: editDot=2
        if row==1 and column==2: editDot=1
        if row==2 and column==2: editDot=3
        if editDot!=5:
            resultObjects[guess][editDot].undraw()
            if outputKey[guess][editDot]==1:
                color="black"
                outputKey[guess][editDot]=2
            elif outputKey[guess][editDot]==2:
                color="white"
                outputKey[guess][editDot]=3
            elif outputKey[guess][editDot]==3:
                color="gray"
                outputKey[guess][editDot]=1        
            resultObjects[guess][editDot].setFill(color)
            resultObjects[guess][editDot].draw(win)
        click=win.getMouse()
        if click.x>=15.5 and click.x<=18.5:
            if click.y>=(1.2+guess*3) and click.y<=(2.8+guess*3):
                submitGuess=1
    output=""
    for i in range(4):
        if outputKey[guess][i]==2: output=output+"1"
        if outputKey[guess][i]==3: output=output+"0"
    return output

    
def welcomeBox():
    welcome = GraphWin("Welcome to Mastermind Madness", 500,300)
    welcome.setCoords(0, 0, 10, 10)
    welcome.setBackground("Orange")
    Text(Point(5,9),"Make up a 4-letter code using these colors and write it down:").draw(welcome)
    Text(Point(5,8),"(c)yan, (p)urple, (b)lue, (g)reen, (y)ellow, (r)ed").draw(welcome)
    Text(Point(5,7),"I will guess a color code and you tell me the output by clicking").draw(welcome)
    Text(Point(5,6),"the small circles next the code. A black dot means I have a correct").draw(welcome)
    Text(Point(5,5),"color in the correct spot. A white dot means I have a correct color").draw(welcome)
    Text(Point(5,4),"but in the wrong spot.").draw(welcome)
    Text(Point(5,3),"CLICK to continue.").draw(welcome)
    welcome.getMouse()
    welcome.close()    
       

def createGUI():
    welcomeBox()
    
    win = GraphWin("Mastermind Madness", 466,550)
    win.setCoords(0.0, 0.0, 19.6, 23.5)
    win.setBackground("gray")

    global resultObjects
    resultObjects=createResultObjects(win)
    
    global masterDots
    masterDots = createHiddenDots()
    
    Text(Point(1.5,21), "Guess").draw(win)
    
    playBox=Rectangle(Point(.25, .25), Point(19.5,23.25))
    playBox.setFill("pink")
    playBox.draw(win)

    #Display Banner on top of display.
    mmBanner=Text(Point(9,22),"MASTERMIND MADNESS!")
    mmBanner.setFace("times roman")
    mmBanner.setSize(15)
    mmBanner.setStyle("bold")
    mmBanner.setFill("Blue")
    mmBanner.draw(win) 

    startText=Text(Point(10,15), "Click and I'll make my first guess.")
    startText.draw(win)

    win.getMouse()
    startText.undraw()
    
    return win

def beatDown(guesses):
    win = GraphWin("I BEAT YOU!", 500,500)
    win.setCoords(0.0, 0.0, 30.0, 30.0)
    win.setBackground("red")

    message=Text(Point(11,29), "I guessed the code in only")
    message.setFace("times roman")
    message.setSize(15)
    message.setStyle("bold")
    message.draw(win)
    
    message2=Text(Point(15,27), (guesses,"guesses!!!"))
    message2.setFace("times roman")
    message2.setSize(20)
    message2.setStyle("bold")
    message2.draw(win)

    message3=Text(Point(6,23), " ''I will take over the world!''")
    message3.setFace("helvetica")
    message3.setSize(10)
    message3.setStyle("bold italic")
    message3.draw(win)


    devil=Image(Point(15,12), "computer2.gif")
    devil.draw(win)

    for i in range(30):
        devil.move(math.sin(i),(math.cos(i)*math.sin(i)))
        time.sleep(.1)

    quitBox=Rectangle(Point(.5,.25),Point(6.25,2))
    quitBox.setFill("black")
    quitBox.draw(win)

    quitMess=Text(Point(3.25,1), "Play Again")
    quitMess.setFill("white")
    quitMess.setStyle("bold")
    quitMess.draw(win)

    playBox=Rectangle(Point(25,.25),Point(29.75, 2))
    playBox.setFill("black")
    playBox.draw(win)

    playMess=Text(Point(27,1), "Quit")
    playMess.setFill("white")
    playMess.setStyle("bold")
    playMess.draw(win)

    playAgain=2
    while playAgain==2:
        click=win.getMouse()
        if click.y>=.25 and click.y<=2:
            if click.x <6.25:
                playAgain=1
            if click.x > 25:
                playAgain=0
    win.close()
    return playAgain

########################-Mastermind Functions-#############################

#Pass in the code and a guess and fuction will return the number of
#black and white pegs.
def testGuess(code,guess):
    tempCode=[code[0],code[1],code[2],code[3]]
    tempGuess=[guess[0],guess[1],guess[2],guess[3]]
    correctPeg=0
    correctColor=0

    for i in range(4):
        if guess[i]==code[i]:
            correctPeg=correctPeg+1
            tempCode[i]="x"
            tempGuess[i]="z"

    spaces=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]           

    for i in range(4):
        for s in spaces[i]:
            if tempGuess[i]==tempCode[s]:
                correctColor=correctColor+1
                tempCode[s]="x"
                tempGuess[i]="z"    

    return correctPeg,correctColor


#Turns text result into usable data and checks for certain conditions.
#Colors are eliminated from masterColors if they are not possibilities.
#Returns black and white pegs to main() to develop next guess.
def checkResult(result, guess, masterColors):
    correctPeg=correctColor=0
    for i in range(len(result)):
        if result[i-1]=="0":
            correctColor=correctColor+1
        if result[i-1]=="1":
            correctPeg=correctPeg+1

    if correctPeg==0:
        for i in range(4):
            for x in range(len(masterColors[i])):
                if guess[i]==masterColors[i][x]:
                    del masterColors[i][x]
                    break

    if correctPeg==0 and correctColor==0:
        for i in range(4):
            for p in range(4):
                for x in range(len(masterColors[i])):
                    if masterColors[i][x]==guess[p]:
                        del masterColors[i][x]
                        break

    if correctPeg+correctColor==4:
        colors=[guess[0],guess[1],guess[2],guess[3]]
        for i in range(4):
            masterColors[i]=colors

    return correctPeg, correctColor

def testLetter(letter,string):
    occurs=0
    for i in range(len(string)):
        if letter==string[i]:
            occurs=1
    return occurs

#Pass in a maximum number and randy() will return a random number from
#0-number. Each successive call returns a number not called in the last
#five calls to randy(). The result is a list of numbers randomly ordered.

rand1=9
rand2=9
rand3=9
rand4=9
rand5=9

def randy(highNum):
    global rand1, rand2, rand3, rand4, rand5
    number=randrange(0,highNum)
    while number==rand1 or number==rand2 or number==rand3 or number==rand4 or number==rand5:
        number=randrange(0,highNum)
 
    rand5=rand4
    rand4=rand3
    rand3=rand2
    rand2=rand1
    rand1=number
    return number

def reset():
    global rand1, rand2, rand3, rand4, rand5
    rand1=rand2=rand3=rand4=rand5=9


###############################-main-###################################

def main():

    win=createGUI()
    masterColors=[["r","b","g","y","p","c"],
                  ["r","b","g","y","p","c"],
                  ["r","b","g","y","p","c"],
                  ["r","b","g","y","p","c"]]

    result1=result2=result3=result4=result5=result6=0
    masterResults=[result1,result2,result3,result4,result5,result6]
    
    #[correctPeg,correctColor,correctPeg2,correctColor2]
    masterPegs=[[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    masterGuesses=[["1","1","1","1"],
                   ["2","2","2","2"],
                   ["3","3","3","3"],
                   ["4","4","4","4"],
                   ["5","5","5","5"],
                   ["6","6","6","6"],
                   ["7","7","7","7"]]

#!-----Randomly selects four different colors for first guess.-----!
    
    colors=["r","b","g","y","p","c"]
    for i in range(4):
        number=randrange(0,len(colors))
        masterGuesses[0][i]=colors[number]
        if number==len(colors):
            colors=colors[0:number]
        else:
            colors=colors[0:number]+colors[(number+1):len(colors)]

    showGuess(0,masterGuesses[0],win)
    masterResults[0]=outputClicks(0,win)
    
    masterPegs[0][0], masterPegs[0][1] = checkResult(masterResults[0], masterGuesses[0], masterColors)
    guessedTheCode=0
    if masterPegs[0][0]==4: guessedTheCode=1

#All subsequent guesses follow same procedure:
#a: Use feedback from previous guess to make new guess
#b: Check to make sure it is a valid guess, or make a new guess.
#c: Send guess to visual interface and get feeback from user.

    gNum=1
    while guessedTheCode==0:
        while testLetter(str(gNum+1), masterGuesses[gNum])==1:
            reset()
            randyList=[randy(4),randy(4), randy(4), randy(4)]
            for i in range(4):
                space = randyList[i]
                if masterGuesses[gNum][space]==str(gNum+1):
                    reset()
                    randColors=[]
                    for i in range(len(masterColors[space])):
                        randColors=randColors+[randy(len(masterColors[space]))]
                    for c in randColors:
                        color=masterColors[space][randColors[c]]
                        masterGuesses[gNum][space]=color

                        for a in range(gNum):
                            a=a+1
                            masterPegs[gNum-a][2],masterPegs[gNum-a][3]=testGuess(masterGuesses[gNum-a],masterGuesses[gNum])

                        for a in range(7):
                            if masterPegs[a][2]>masterPegs[a][0] or masterPegs[a][3]>masterPegs[a][1]:
                                for r in range(4):
                                    masterGuesses[gNum][r]=str(gNum+1)
                        if masterGuesses[gNum][space]!=str(gNum+1): break
                        if masterGuesses[gNum][space]==str(gNum+1) and i==(len(masterColors[space])): break

            if testLetter(str(gNum+1), masterGuesses[gNum])==1:
                for r in range(4):
                    masterGuesses[gNum][r]=str(gNum+1)

            for a in range(7):
                if masterPegs[a][2]!=masterPegs[a][0] or masterPegs[a][3]!=masterPegs[a][1]:
                    for r in range(4):
                        masterGuesses[gNum][r]=str(gNum+1)

        showGuess(gNum,masterGuesses[gNum],win)
        masterResults[gNum]=outputClicks(gNum,win)

        masterPegs[gNum][0], masterPegs[gNum][1] = checkResult(masterResults[gNum], masterGuesses[gNum], masterColors)

        if masterPegs[gNum][0]==4:
            guessedTheCode=1

        gNum=gNum+1

    again=beatDown(gNum)    
    if again==0:
        win.close()
    elif again==1:
        win.close()
        main()

main()
