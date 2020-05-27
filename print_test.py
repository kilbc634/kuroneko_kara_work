"""
輸入為三個整數，
第一個整數為矩陣維度，其值介於1到10之間（亦即1 <= size <= 10）。
第二個整數為旋轉方向，1為順時鐘方向，2為逆時鐘方向。
第三個整數為內折處，1為在第一個角內折，2為在第二個角內折。
"""
import copy


###############################################################
#
#    Init Zone
#
###############################################################

xyLen = int(input("矩陣邊長(1 or more):"))
rotationType = int(input("旋轉方向(1 is positive, 2 is negative):"))
fold = int(input("內折處(1 or 2 or 3):"))

nowPos = {
    "x": 1,
    "y": 1,
    "count": 0
}

ROW = xyLen
COL = xyLen
directionRoll = ["y-", "y-x+", "x+", "x+y+", "y+", "y+x-", "x-", "x-y-"]
#       (y-)
#        │
# (x-) ──┼┬┬┬────> (x+)
#        ├┼┼┘
#        ├┼┘
#        ├┘
#        │
#        V
#       (y+)
rotationCount = 0
array2D = [["N" for _ in range(ROW)] for _ in range(COL)]
# array2D same as...
# ex: [ [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ],
#       [ "N" , "N" , "N" , "N" , "N" ] ]


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
    print(nowPos)
    array2D[ nowPos["y"]-1 ][ nowPos["x"]-1 ] = nowPos["count"]


def set_block(x, y):
    global nowPos
    global array2D # will modify global variable
    # yo man
    # test
    # select me
    array2D[y - 1][x - 1] = "B"


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
    if array2D[ pos["y"]-1 ][ pos["x"]-1 ] != "N":
        return False
    return True


def goToWall(direction, setBlock=None):
    global nowPos
    stepCount = 0
    while True:
        if check_nextStep(direction) == False:
            return stepCount
        if check_nextStep(direction) == True:
            pos = get_nextStep(direction, nowPos)
            set_step(pos["x"], pos["y"])
            stepCount = stepCount + 1
            if setBlock:
                pos = get_nextStep(setBlock, nowPos)
                set_block(pos["x"], pos["y"])


def get_nextStep(direction, pos=None):
    global nowPos
    if pos == None:
        pos = nowPos
    tempPos = copy.deepcopy(pos)
    if "x+" in direction:
        tempPos["x"] = tempPos["x"] + 1
    if "x-" in direction:
        tempPos["x"] = tempPos["x"] - 1
    if "y+" in direction:
        tempPos["y"] = tempPos["y"] + 1
    if "y-" in direction:
        tempPos["y"] = tempPos["y"] - 1
    return tempPos


def get_direction(rotationType, startRoll="y-", extraMod=False):
    global directionRoll
    rollIndex = directionRoll.index(startRoll)
    if rotationType == 1: # positive
        for limit in range(8):
            index = rollIndex % 8
            if check_nextStep(directionRoll[index]) == True:
                if extraMod == True:
                    return directionRoll[ (index+1) % 8]
                return directionRoll[index]
            else:
                rollIndex = rollIndex + 1
        return startRoll
    if rotationType == 2: # negative
        for limit in range(8):
            index = rollIndex % 8
            if check_nextStep(directionRoll[index]) == True:
                if extraMod == True:
                    return directionRoll[ (index-1) % 8]
                return directionRoll[index]
            else:
                rollIndex = rollIndex - 1
        return startRoll


def check_end():
    for direction in directionRoll:
        if check_nextStep(direction) == True:
            return False
    return True


###############################################################
#
#    Main Zone
#
###############################################################

if __name__ == "__main__":
    set_step(nowPos["x"], nowPos["y"])
    direction = "y-"
    rotationCount = 0

    while True:
        if rotationCount == fold:
            directionOrigin = copy.deepcopy(direction)
            direction = get_direction(rotationType, direction, extraMod=True)
            print('direction = ' + direction)
            rotationCount = rotationCount + 1
            stepCount = goToWall(direction, setBlock=directionOrigin)
        else:
            direction = get_direction(rotationType, direction)
            print('direction = ' + direction)
            rotationCount = rotationCount + 1
            stepCount = goToWall(direction)
        if check_end() == True or stepCount == 0:
            break

    print('-------------- END --------------')
    # change all element to STR for data type 00,01,02,03......
    temp2D = list()
    for row in array2D:
        tempList = list()
        for element in row:
            if isinstance(element, int):
                if element < 10:
                    tempList.append("0" + str(element))
                else:
                    tempList.append(str(element))
            if element == "N" or element == "B":
                tempList.append("00")
        temp2D.append(tempList)
    
    for aList in temp2D:
        print(aList)
