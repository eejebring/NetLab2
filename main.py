file = open("/home/eejebring/Downloads/score2.txt","r")
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

topScore = 0
for person in pointDict:
    if topScore < pointDict[person]:
        topScore = pointDict[person]
        winner = person
    elif topScore == pointDict[person]:
        winner += f" and {person}"



print(f"\nAnd the winner is!:\n {winner} with {topScore} points")

#the winner in my simmulation is Maria Johansson and Kristina Larsson with 37 points!
