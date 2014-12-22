# Alexander Herbig and Nia Hall
# aherbig3@gatech.edu nhall35@gatech.edu
# GTID: 903035515
# Section B04
# We worked on this homework assignment alone, using this semester's course materials

# This code takes input from a person using the arrow keys on a computer, and moves the robot in the direction specified.
# The robot is then able to play back it's movements by reading from a file that stored the inputs in raw text.

from Myro import *
from Graphics import *
#init("/dev/tty.Fluke2-02A9-Fluke2")

# This creates the file or clears it out. For use in the rest of the program.
f = open('myMovements.txt', 'w')


# This moves the robot when the user inputs an arrow key.
# Each conditional creates a string called "data" that gets written to the myMovements file at the end of the function.
# This has part 1 and part 2.
def robotMover(win,event):
    key = event.key
    data = ""
    f = open('myMovements.txt', 'a')
    sensorValue = getLight("left")/(getLight("right")+getObstacle("right"))
    sensorValue = round(sensorValue, 3)
    sensorValue = str(sensorValue)
    if key=="Up":
        forward(1,0.1)
        data = "forward" + " .1 " + sensorValue
    elif key=="Down":
        backward(1,0.1)
        data = "backward" + " .1 " + sensorValue
    elif key=="Left":
        turnLeft(1,0.1)
        data = "turnLeft" + " .1 " + sensorValue
    elif key=="Right":
        turnRight(1,0.1)
        data = "turnRight" + " .1 " + sensorValue
    elif key=="b":
        beep(0.2,800)
        data = "beep" + " .2 " 
    else:
        print("Not a valid command! Closing the window")
        win.close()
    if data != "":
        f.write(data + "\n")
    f.close()

# This function reads the file of movements and adds up the moves and times spent moving.
# Then it returns a sentence with all the correct data.
def collectData(filename, direction):
    x = 0
    b = 0
    time = 0
    f = open(filename, "r")
    aStr = f.read()
    aList = aStr.split()
    for i in range(len(aList)):
        if aList[i] == direction:
            x = x + 1
        elif aList[i] == "beep":
            b = b + 1
        if aList[i]=="forward" or aList[i]=="backward" or aList[i]=="turnRight" or aList[i]=="turnLeft":
            moveTime = aList[i+1] # if it's a command, it looks at the next term to tell how long it is.
            moveTime = float(moveTime)
            time = time + moveTime
    x = str(x)
    time = str(time)
    b = str(b)
    retString = ("The robot traveled for " + time + " seconds total, beeping " + b + " times. This robot moved " + direction + " a total of " + x + " times.")
    f.close()
    return retString
    

# This replays the robots movements from the myMovements file.
def replay(filename):
    f = open(filename, "r")
    aStr = f.read()
    aList = aStr.split()
    for i in range(len(aList)):
        if aList[i] == "forward":
            moveTime = float(aList[i+1])
            forward(1, moveTime)
        elif aList[i] == "backward":
            moveTime = float(aList[i+1])
            backward(1, moveTime)
        elif aList[i] == "turnRight":
            moveTime = float(aList[i+1])
            turnRight(1, moveTime)
        elif aList[i] == "turnLeft":
            moveTime = float(aList[i+1])
            turnLeft(1, moveTime)
        elif aList[i] == "beep":
            moveTime = float(aList[i+1])
            beep(moveTime, 800)
    f.close()
    
# Using calico's graphics window, the user is able to input commands at any time.

win  = Window("KeyHandler",200,200)
onKeyPress(robotMover)

f.close()
