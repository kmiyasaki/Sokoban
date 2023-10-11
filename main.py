from copy import deepcopy
from game_settings import *

gameboard = deepcopy(board)
wincondition = False

def boardsetup(boardtype, wincondition):
    unsatisfiedcount = 0
    for line in boardtype:
        spaceindex = 0
        for space in line:
            spaceindex += 1
            if spaceindex == len(line):
                print(space)
            else:
                print(space, end=' ')
    
    for line in boardtype:
        if BOX_NS in line:
            unsatisfiedcount += 1
        
    if unsatisfiedcount == 0:
        wincondition = True

    if wincondition == False:
        print()
    elif wincondition == True:
        print("You Win!")
    return wincondition

def getX(boardtype):
    for line in boardtype:
        if SPRITE in line:
            global xcoord
            xcoord = line.index(SPRITE)
            return xcoord
        if SPRITE_T in line:
            xcoord = line.index(SPRITE_T)
            return xcoord

def getY(boardtype):
    for line in boardtype:
        if SPRITE in line or SPRITE_T in line:
            global ycoord
            ycoord = boardtype.index(line)
            return ycoord

# CHECK POSITION
def checkPosition(direction):
    if direction == "right":
        rightobject = gameboard[ycoord][xcoord + 1]
        return rightobject
   
    elif direction == "left":
        leftobject = gameboard[ycoord][xcoord - 1]
        return leftobject
    
    elif direction == "up":
        upobject = gameboard[ycoord - 1][xcoord]
        return upobject
    
    elif direction == "down":
        downobject = gameboard[ycoord + 1][xcoord]
        return downobject

# MOVE
def moveDirection(direction, ycoord, xcoord):
    if gameboard[ycoord][xcoord] == SPRITE_T:
        gameboard[ycoord][xcoord] = TARGET
    else:
        gameboard[ycoord][xcoord] = EMPTY
    
    if direction == "right":
        xcoord += 1
        gameboard[ycoord][xcoord] = SPRITE

    elif direction == "left":
        xcoord -= 1
        gameboard[ycoord][xcoord] = SPRITE
    
    elif direction == "up":
        ycoord -= 1
        gameboard[ycoord][xcoord] = SPRITE
    
    elif direction == "down":
        ycoord += 1
        gameboard[ycoord][xcoord] = SPRITE

# CHECK POSITION A SPACE AWAY
def checkDoublePosition(direction, xcoord, ycoord):
    if direction == "right":
        doublerightobject = gameboard[ycoord][xcoord + 2]
        return doublerightobject
   
    elif direction == "left":
        doubleleftobject = gameboard[ycoord][xcoord - 2]
        return doubleleftobject
    
    elif direction == "up":
        doubleupobject = gameboard[ycoord - 2][xcoord]
        return doubleupobject
    
    elif direction == "down":
        doubledownobject = gameboard[ycoord + 2][xcoord]
        return doubledownobject

boardsetup(gameboard, False)

# INFINITE LOOP
while True:
    move = input("What move would you like to make?\nUse w, a, s, d to control sprite, space to restart, or q to quit.\n")
    getX(gameboard)
    getY(gameboard)
    
    if move in CONTROLS:
        
        # QUIT
        if move == QUIT:
            print("Goodbye")
            break
    
        # RESTART
        elif move == RESTART:
            gameboard = deepcopy(board)
            boardsetup(gameboard, False)
        
        # MOVE UP
        elif move == "w":
            ycoord = getY(gameboard)
            
            # if up position is empty
            if checkPosition("up") == EMPTY:
                moveDirection("up", ycoord, xcoord)
                boardsetup(gameboard, False)
            
            # if up position is wall
            elif checkPosition("up") == WALL:
                boardsetup(gameboard, False)
                
            # if up position is target
            elif checkPosition("up") == TARGET:
                gameboard[ycoord][xcoord] = EMPTY
                ycoord -= 1
                gameboard[ycoord][xcoord] = SPRITE_T
                boardsetup(gameboard, False)
            
            # if up position is satisfied box
            elif checkPosition("up") == BOX_S:
                
                # if up positions are box, wall
                if checkDoublePosition("up", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                # if up positions are box, box
                elif checkDoublePosition("up", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if up positions are box, empty
                elif checkDoublePosition("up", xcoord, ycoord) == EMPTY:
                    gameboard[ycoord][xcoord] = EMPTY
                    ycoord -= 1
                    gameboard[ycoord][xcoord] = SPRITE_T
                    gameboard[ycoord][ycoord - 1] = BOX_NS
                    boardsetup(gameboard, False)
            
            # if up position is unsatisfied box
            elif checkPosition("up") == BOX_NS:
                
                # if up positions are box, wall
                if checkDoublePosition("up", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                
                # if up positions are box, box
                elif checkDoublePosition("up", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                
                # if up positions are box, box
                elif checkDoublePosition("up", xcoord, ycoord) == BOX_S:
                    boardsetup(gameboard, False)
                    
                # if up positions are box, empty
                elif checkDoublePosition("up", xcoord, ycoord) == EMPTY:
                    moveDirection("up", ycoord, xcoord)
                    getY(gameboard)
                    gameboard[ycoord - 1][xcoord] = BOX_NS
                    boardsetup(gameboard, False)
                    
                # if up positions are box, target
                elif checkDoublePosition("up", xcoord, ycoord) == TARGET:
                    moveDirection("up", ycoord, xcoord)
                    getY(gameboard)
                    gameboard[ycoord - 1][xcoord] = BOX_S
                    boardsetup(gameboard, False)

        # MOVE DOWN
        elif move == "s":
            ycoord = getY(gameboard)
            
            # if down position is empty
            if checkPosition("down") == EMPTY:
                moveDirection("down", ycoord, xcoord)
                boardsetup(gameboard, False)
            
            # if down position is wall
            elif checkPosition("down") == WALL:
                boardsetup(gameboard, False)
            
            # if down position is target
            elif checkPosition("down") == TARGET:
                gameboard[ycoord][xcoord] = EMPTY
                ycoord += 1
                gameboard[ycoord][xcoord] = SPRITE_T
                boardsetup(gameboard, False)
            
            # if down position is satisfied box
            elif checkPosition("down") == BOX_S:
                
                # if down positions are box, wall
                if checkDoublePosition("down", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                # if down positions are box, box
                elif checkDoublePosition("down", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if down positions are box, empty
                elif checkDoublePosition("down", xcoord, ycoord) == EMPTY:
                    gameboard[ycoord][xcoord] = EMPTY
                    ycoord += 1
                    gameboard[ycoord][xcoord] = SPRITE_T
                    gameboard[ycoord][ycoord + 1] = BOX_NS
                    boardsetup(gameboard, False)
            
            # if down position is unsatisfied box
            elif checkPosition("down") == BOX_NS:
                
                # if down positions are box, wall
                if checkDoublePosition("down", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                
                # if down positions are box, box
                elif checkDoublePosition("down", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if down positions are box, box
                elif checkDoublePosition("down", xcoord, ycoord) == BOX_S:
                    boardsetup(gameboard, False)
                
                # if down positions are box, empty
                elif checkDoublePosition("down", xcoord, ycoord) == EMPTY:
                    moveDirection("down", ycoord, xcoord)
                    getY(gameboard)
                    gameboard[ycoord + 1][xcoord] = BOX_NS
                    boardsetup(gameboard, False)
                
                # if down positions are box, target
                elif checkDoublePosition("down", xcoord, ycoord) == TARGET:
                    moveDirection("down", ycoord, xcoord)
                    getY(gameboard)
                    gameboard[ycoord + 1][xcoord] = BOX_S
                    boardsetup(gameboard, False)
        
        # MOVE LEFT
        elif move == "a":
            xcoord = getX(gameboard)
            
            # if left position is empty
            if checkPosition("left") == EMPTY:
                moveDirection("left", ycoord, xcoord)
                boardsetup(gameboard, False)
            
            # if left position is wall
            elif checkPosition("left") == WALL:
                boardsetup(gameboard, False)
            
            # if left position is target
            elif checkPosition("left") == TARGET:
                gameboard[ycoord][xcoord] = EMPTY
                xcoord -= 1
                gameboard[ycoord][xcoord] = SPRITE_T
                boardsetup(gameboard, False)
            
            # if left position is satisfied box
            elif checkPosition("left") == BOX_S:
                
                # if left positions are box, wall
                if checkDoublePosition("left", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                # if left positions are box, box
                elif checkDoublePosition("left", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if left positions are box, empty
                elif checkDoublePosition("left", xcoord, ycoord) == EMPTY:
                    gameboard[ycoord][xcoord] = EMPTY
                    xcoord -= 1
                    gameboard[ycoord][xcoord] = SPRITE_T
                    gameboard[ycoord][xcoord - 1] = BOX_NS
                    boardsetup(gameboard, False)
                
            # if left position is unsatisfied box
            elif checkPosition("left") == BOX_NS:
                
                # if left positions are box, wall or box, box
                if checkDoublePosition("left", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                if checkDoublePosition("left", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if left positions are box, box
                elif checkDoublePosition("left", xcoord, ycoord) == BOX_S:
                    boardsetup(gameboard, False)
                
                # if left positions are box, empty
                elif checkDoublePosition("left", xcoord, ycoord) == EMPTY:
                    moveDirection("left", ycoord, xcoord)
                    getX(gameboard)
                    gameboard[ycoord][xcoord - 1] = BOX_NS
                    boardsetup(gameboard, False)
                
                # if left positions are box, target
                elif checkDoublePosition("left", xcoord, ycoord) == TARGET:
                    moveDirection("left", ycoord, xcoord)
                    getX(gameboard)
                    gameboard[ycoord][xcoord - 1] = BOX_S
                    boardsetup(gameboard, False)

        # MOVE RIGHT
        elif move == "d":
            xcoord = getX(gameboard)
            
            # if right position is empty
            if checkPosition("right") == EMPTY:
                    moveDirection("right", ycoord, xcoord)
                    boardsetup(gameboard, False)
                
            # if right position is wall
            elif checkPosition("right") == WALL:
                boardsetup(gameboard, False)
            
            # if right position is target
            elif checkPosition("right") == TARGET:
                gameboard[ycoord][xcoord] = EMPTY
                xcoord += 1
                gameboard[ycoord][xcoord] = SPRITE_T
                boardsetup(gameboard, False)
            
            # if right position is satisfied box
            elif checkPosition("right") == BOX_S:
                
                # if right positions are box, wall
                if checkDoublePosition("right", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                # if right positions are box, box
                elif checkDoublePosition("right", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if right positions are box, empty
                elif checkDoublePosition("right", xcoord, ycoord) == EMPTY:
                    gameboard[ycoord][xcoord] = EMPTY
                    xcoord += 1
                    gameboard[ycoord][xcoord] = SPRITE_T
                    gameboard[ycoord][xcoord + 1] = BOX_NS
                    boardsetup(gameboard, False)
            
            # if right position is unsatisfied box
            elif checkPosition("right") == BOX_NS:
                
                # if right positions are box, wall
                if checkDoublePosition("right", xcoord, ycoord) == WALL:
                    boardsetup(gameboard, False)
                    
                # if right positions are box, box
                elif checkDoublePosition("right", xcoord, ycoord) == BOX_NS:
                    boardsetup(gameboard, False)
                    
                # if right positions are box, box
                elif checkDoublePosition("right", xcoord, ycoord) == BOX_S:
                    boardsetup(gameboard, False)
                    
                # if right positions are box, empty
                elif checkDoublePosition("right", xcoord, ycoord) == EMPTY:
                    moveDirection("right", ycoord, xcoord)
                    getX(gameboard)
                    gameboard[ycoord][xcoord + 1] = BOX_NS
                    boardsetup(gameboard, False)
                
                # if right positions are box, target
                elif checkDoublePosition("right", xcoord, ycoord) == TARGET:
                    moveDirection("right", ycoord, xcoord)
                    getX(gameboard)
                    gameboard[ycoord][xcoord + 1] = BOX_S
                    boardsetup(gameboard, False)
    
    else:
        print("enter a valid move:")
