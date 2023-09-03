#virtual environment: venv/Script/activate
#import pygame
import random, time

#functions
def horizontal(length):
    rangeMax = 9-length
    column = str(random.randint(1, rangeMax))
    startCoord = random.choice(colList[column])
    index = coordList.index(startCoord)
    boat = []
    for i in range(length):
        pos = coordList[index+i]
        boat.append(pos)
    return boat, True

def vertical(length):
    ltrRange = "ABCDEFGH"
    rangeMax = 9-length
    row = ltrRange[:rangeMax]
    startCoord = random.choice(rowList[str(random.choice(row))])
    index = coordList.index(startCoord)
    boat = []
    for i in range(length):
        pos = coordList[index+i*8]
        boat.append(pos)
    return boat, True

def hint(correct):
    hints = {
        "1,2": "x=1,2",
        "1,3": "x=1,3",
        "1,4": "x=1,4",
        "1,5": "x=1,5",
        "1,6": "x=1,6",
        "1,7": "x=1,7",
        "1,8": "x=1,8",
        "2,3": "x=2,3",
        "2,4": "x=2,4",
        "2,5": "x=2,5",
        "2,6": "x=2,6",
        "2,7": "x=2,7",
        "2,8": "x=2,8",
        "3,4": "x=3,4",
        "3,5": "x=3,5",
        "3,6": "x=3,6",
        "3,7": "x=3,7",
        "3,8": "x=3,8",
        "4,5": "x=4,5",
        "4,6": "x=4,6",
        "4,7": "x=4,7",
        "4,8": "x=4,8",
        "5,6": "x=5,6",
        "5,7": "x=5,7",
        "5,8": "x=5,8",
        "6,7": "x=6,7",
        "6,8": "x=6,8",
        "7,8": "x=7,8"
        }
    correct = int(correct)
    n = random.randint(1, 8)
    while n == correct:
        n = random.randint(1, 8)
    if n < correct:
        msg = str(n) + "," + str(correct)
    else:
        msg = str(correct) + "," + str(n)
    return hints[msg]

def positionCheck(position):
    if len(playerPos) != 9:#check number of positions
        print("Incorrect number of positions")
        return False
    for i in playerPos:#check for valid coordinates
        if i not in coordList:
            print("Invalid input")
            return False
    tempList = []
    for i in position:#check duplicates
        if i in tempList:
            print("Duplicate input")
            return False
        else:
            tempList.append(i)
    tempDict = {}
    for pos in position:#get neighbouring positions
        tempList = []
        index = coordList.index(pos)
        row = rowList[pos[0]]
        tempDict[pos] = []
        if (index - 8)>=0 and coordList[index - 8] in position:#check up
            tempList.append(coordList[index - 8])
            tempDict[pos] = tempList
        if (index + 8)<=63 and coordList[index + 8] in position:#check down
            tempList.append(coordList[index + 8])
            tempDict[pos] = tempList
        if (index - 1)>=0 and coordList[index - 1] in position and coordList[index - 1] in row:#check left
            tempList.append(coordList[index - 1])
            tempDict[pos] = tempList
        if (index + 1)<=63 and coordList[index + 1] in position and coordList[index + 1] in row:#check right
            tempList.append(coordList[index + 1])
            tempDict[pos] = tempList
    boat4 = []
    boat3 = []
    boat2 = []

#default values
ltnConvert = str.maketrans("ABCDEFGH", "12345678")
coordList = [
    'A1','A2','A3','A4','A5','A6','A7','A8',
    'B1','B2','B3','B4','B5','B6','B7','B8',
    'C1','C2','C3','C4','C5','C6','C7','C8',
    'D1','D2','D3','D4','D5','D6','D7','D8',
    'E1','E2','E3','E4','E5','E6','E7','E8',
    'F1','F2','F3','F4','F5','F6','F7','F8',
    'G1','G2','G3','G4','G5','G6','G7','G8',
    'H1','H2','H3','H4','H5','H6','H7','H8']
rowList = {
    "A":['A1','A2','A3','A4','A5','A6','A7','A8'],
    "B":['B1','B2','B3','B4','B5','B6','B7','B8'],
    "C":['C1','C2','C3','C4','C5','C6','C7','C8'],
    "D":['D1','D2','D3','D4','D5','D6','D7','D8'],
    "E":['E1','E2','E3','E4','E5','E6','E7','E8'],
    "F":['F1','F2','F3','F4','F5','F6','F7','F8'],
    "G":['G1','G2','G3','G4','G5','G6','G7','G8'],
    "H":['H1','H2','H3','H4','H5','H6','H7','H8']}
instructions= "Instructions:\nplaceholder"
playerTargeted = []
botTargeted = []
playerPos = ""

botPos = []
boatLength = [4, 3, 2]#change numbers to change boats (1-8)
while len(boatLength) > 0:
    direction = random.choice("12")
    if direction == "1":
        boat, loop = horizontal(boatLength[0])
    if direction == "2":
        boat, loop = vertical(boatLength[0])
    botPos.append(boat)
    boatLength.pop(0)
print(botPos)
print(instructions)
while playerPos == "":
    playerPos = input("Set your positions: ")
    playerPos.upper()
    playerPos = playerPos.split(",")
    valid = positionCheck(playerPos)
    if valid == True:
        break
    else:
        playerPos = ""

while botPos != [] or playerPos != []:
    hintType = ""
    check = ""
    while hintType == "":
        hintType = input("Hint (Row/Column): ")
        hintType = hintType.lower()
        if hintType == "row":
            posTarget = random.choice(botPos)
            temp = posTarget[0]
            temp = temp.translate(ltnConvert)
        elif hintType == "column":
            posTarget = random.choice(botPos)
            temp = posTarget[1]
        else:
            print("Invalid input")
            hintType = ""
    print(posTarget)
    print(hint(temp))
    while check == "":
        check = input("Pick a target coordinate: ")
        check = check.upper()
        if check in coordList:
            if check not in playerTargeted:
                if check in botPos:
                    botPos.remove(check)
                    print("-Hit")
                    if botPos == []:
                        break
                else:
                    print("-Miss")
                playerTargeted.append(check)
            else:
                print("Already chosen previously")
                check = ""
        else:
            print("Invalid input")
            check = ""
    print("Bot thinking...")
    botTarget = random.choice(coordList)
    while botTarget in botTargeted:
        botTarget = random.choice(coordList)
    time.sleep(2)
    print(f"Bot Target: {botTarget}")
    if botTarget in playerPos:
        playerPos.remove(botTarget)
        print("-Hit")
        if playerPos == []:
            break
    else:
        print("-Miss")
    botTargeted.append(botTarget)
    time.sleep(1)
if botPos == []:
    print("You Win!")
elif playerPos == []:
    print("Bot Wins!")