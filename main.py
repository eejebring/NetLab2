file = open("/home/eejebring/score2.txt","r")
textLines = file.read().split()

pointDict = dict()
person = ""

for lines in textLines:
    try:
        points = int(lines)
        if person != "":
            try:
                pointDict[person]
            except:
                pointDict[person] = 0
            pointDict[person] += points
    except:
        if lines == "upg.":
            person = ""
        else:
            if person != "":
                person += " "
            person += lines


for person in pointDict:
    print(person + f" {pointDict[person]}")
