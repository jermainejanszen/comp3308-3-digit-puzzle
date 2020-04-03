import sys

import tree
import algorithms

algo = sys.argv[1]

inputFilePath = sys.argv[2]
inputFile = open(inputFilePath, "r")

startState = inputFile.readline().rsplit()[0]
startState = [char for char in startState]

goalState = inputFile.readline().rsplit()[0]
goalState = [char for char in goalState]

forbidden = []
try:
    forbiddenString = inputFile.readline().split(",")
except:
    pass
if forbiddenString != ['']:
    for i in range(len(forbiddenString)):
        forbidden.append([char for char in forbiddenString[i]])
root = tree.Tree(data=startState, isGoal=(startState == goalState))

fringe = []
expanded = []
pathFound = []

# Call algorithms
if algo == 'B':
    pathFound = algorithms.bfs(root, goalState, forbidden, fringe, expanded)
elif algo == 'D':
    pathFound = algorithms.dfs(root, goalState, forbidden, fringe, expanded)
elif algo == 'I':
    pathFound = algorithms.ids(root, goalState, forbidden, fringe, expanded)
elif algo == 'G':
    pathFound = algorithms.greedy(root, goalState, forbidden, fringe, expanded)
elif algo == 'A':
    pathFound = algorithms.aStar(root, goalState, forbidden, fringe, expanded)
elif algo == 'H':
    pathFound = algorithms.hillClimbing(root, goalState, forbidden, fringe, expanded)
else:
    sys.exit(0)

# Format output
foundSolution = True
if expanded[-1].data != goalState:
    foundSolution = False

pathFoundValues = []
for i in range(len(pathFound)):
    pathFoundValues.append("".join(pathFound[i].data))

expandedValues = []
for i in range(len(expanded)):
    expandedValues.append("".join(expanded[i].data))

outputPath = ""
if foundSolution:
    for i in range(len(pathFoundValues)):
        outputPath += pathFoundValues[i] + ","
    outputPath = outputPath.rstrip(",")
else:
    outputPath = "No solution found."

outputExpanded = ""
for i in range(len(expandedValues)):
    outputExpanded += expandedValues[i] + ","
outputExpanded = outputExpanded.rstrip(",")

print(outputPath)
print(outputExpanded)