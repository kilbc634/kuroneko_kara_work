"""
輸入為三個整數，
第一個整數為矩陣維度，其值介於1到10之間（亦即1 <= size <= 10）。
第二個整數為旋轉方向，1為順時鐘方向，2為逆時鐘方向。
第三個整數為內折處，1為在第一個角內折，2為在第二個角內折。
"""


########## Init ##########

xyLen = int(input("矩陣維度:"))
rotationType = int(input("旋轉方向:"))
fold = int(input("內折處:"))

nowPos = {
    "x": 1,
    "y": 1,
    "count": 0
}

ROW = xyLen
COL = xyLen
directionRoll = ["y+", "y+x+", "x+", "x+y-", "y-", "y-x-", "x-", "x-y+"]
rotationCount = 0
array2D = [["N" for _ in range(ROW)] for _ in range(COL)]
# array2D same as...
# ex: [ [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ] ]

########## Init ##########

###############################################################
#
#    Function Zone
#
###############################################################

def set_step(x, y):
    global nowPos # will modify global variable
    global array2D # will modify global variable
    #move pos and update conut
    nowPos["x"] = x
    nowPos["y"] = y
    nowPos["count"] = nowPos["count"] + 1
    #write value
    array2D[ nowPos["x"]-1 ][ nowPos["y"]-1 ] = nowPos["count"]


def check_nextStep(direction):
    global nowPos
    global ROW
    global COL
    global array2D
    pos = get_nextStep(direction, nowPos)
    #check not in domain
    if pos["x"] not in range(1, ROW+1):
        return False
    if pos["y"] not in range(1, COL+1):
        return False
    #check value have
    if array2D[ pos["x"]-1 ][ pos["y"]-1 ] != "N":
        return False
    return True


def goToWall(direction):
    global nowPos
    stepCount = 0
    while True:
        if check_nextStep(direction) == False:
            return stepCount
        if check_nextStep(direction) == True:
            pos = get_nextStep(direction, nowPos)
            set_step(pos["x"], pos["y"])
            stepCount = stepCount + 1


def check_end():
    if check_nextStep("x+")==False and \
    check_nextStep("x-")==False and \
    check_nextStep("y+")==False and \
    check_nextStep("y-")==False:
        return True
    else:
        return False

def get_nextStep(direction, tempPos):
    if "x+" in direction:
        tempPos["x"] = tempPos["x"] + 1
    if "x-" in direction:
        tempPos["x"] = tempPos["x"] - 1
    if "y+" in direction:
        tempPos["y"] = tempPos["y"] + 1
    if "y-" in direction:
        tempPos["y"] = tempPos["y"] - 1
    return tempPos


def get_direction(rotationType, startRoll="y+"):
    global directionRoll
    global rotationCount # will modify
    global fold
    rollIndex = directionRoll.index(startRoll)
    if rotationType == 1: # positive
        for limit in range(8):
            index = rollIndex % 8
            if check_nextStep(directionRoll[index]) == True:
                rotationCount = rotationCount + 1
                if rotationCount == fold:
                    return directionRoll[ (index+1) % 8]
                return directionRoll[index]
            else:
                rollIndex = rollIndex + 1
        return "Error"
    if rotationType == 2: # negative
        for limit in range(8):
            index = rollIndex % 8
            if check_nextStep(directionRoll[index]) == True:
                rotationCount = rotationCount + 1
                if rotationCount == fold:
                    return directionRoll[ (index-1) % 8]
                return directionRoll[index]
            else:
                rollIndex = rollIndex - 1
        return "Error"


###############################################################
#
#    Main Zone
#
###############################################################

if __name__ == "__main__":
    set_step(nowPos["x"], nowPos["y"])
    direction = "y+"

    while True:
        direction = get_direction(rotationType, direction)
        goToWall(direction)
        if check_end() == True:
            break

    for aList in array2D:
        print(aList)







