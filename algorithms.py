from tree import *

def bfs(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        expand(fringe[0], goal, forbidden)
        alreadyExpanded = False
        for i in range(len(expanded)):
            if compare(fringe[0], expanded[i]):
                fringe.pop(0)
                alreadyExpanded = True
                break
        if alreadyExpanded:
            continue
        expanded.append(fringe[0])
        if fringe[0].data == goal:
            foundGoal = True
            break
        else:
            for i in range(len(fringe[0].children)):
                fringe.append(fringe[0].children[i])
        fringe.pop(0)
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound

def dfs(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        expand(fringe[0], goal, forbidden)
        alreadyExpanded = False
        for i in range(len(expanded)):
            if compare(fringe[0], expanded[i]):
                fringe.pop(0)
                alreadyExpanded = True
                break
        if alreadyExpanded:
            continue
        expanded.append(fringe[0])
        if fringe[0].data == goal:
            foundGoal = True
            break
        else:
            for i in range(len(fringe[0].children) - 1, -1, -1):
                fringe.insert(1, fringe[0].children[i])
        fringe.pop(0)
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound

def idsHelper(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list, depth: int):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        if fringe[0].depth > depth:
            fringe.pop(0)
            continue
        expand(fringe[0], goal, forbidden)
        alreadyExpanded = 0
        for i in range(len(expanded)):
            if compare(fringe[0], expanded[i]):
                alreadyExpanded += 1
        if alreadyExpanded > depth - fringe[0].depth:
            fringe.pop(0)
            continue
        expanded.append(fringe[0])
        if fringe[0].data == goal:
            foundGoal = True
            break
        elif fringe[0].depth == depth + 1:
            pass
        else:
            for i in range(len(fringe[0].children) - 1, -1, -1):
                fringe.insert(1, fringe[0].children[i])
        fringe.pop(0)
    return foundGoal

def ids(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    for i in range(1000):
        fringe.clear()
        foundGoal = idsHelper(node, goal, forbidden, fringe, expanded, i)
        if foundGoal:
            break
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound

def greedy(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        currentExpanding = -1
        currentMinH = 1000
        for i in range(len(fringe) - 1, -1, -1):
            if fringe[i].heuristic < currentMinH:
                currentMinH = fringe[i].heuristic
                currentExpanding = i
        if currentExpanding < 0:
            break
        expand(fringe[currentExpanding], goal, forbidden)
        alreadyExpanded = False
        for i in range(len(expanded)):
            if compare(fringe[currentExpanding], expanded[i]):
                alreadyExpanded = True
                break
        if alreadyExpanded:
            fringe.pop(currentExpanding)
            continue
        expanded.append(fringe[currentExpanding])
        if fringe[currentExpanding].data == goal:
            foundGoal = True
            break
        else:
            for i in range(len(fringe[currentExpanding].children)):
                fringe.append(fringe[currentExpanding].children[i])
        fringe.pop(currentExpanding)
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound

def aStar(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        currentExpanding = -1
        currentMinF = 1000
        for i in range(len(fringe) - 1, -1, -1):
            if fringe[i].heuristic + fringe[i].depth < currentMinF:
                currentMinF = fringe[i].heuristic + fringe[i].depth
                currentExpanding = i
        if currentExpanding < 0:
            break
        expand(fringe[currentExpanding], goal, forbidden)
        alreadyExpanded = False
        for i in range(len(expanded)):
            if compare(fringe[currentExpanding], expanded[i]):
                alreadyExpanded = True
                break
        if alreadyExpanded:
            fringe.pop(currentExpanding)
            continue
        expanded.append(fringe[currentExpanding])
        if fringe[currentExpanding].data == goal:
            foundGoal = True
            break
        else:
            for i in range(len(fringe[currentExpanding].children)):
                fringe.append(fringe[currentExpanding].children[i])
        fringe.pop(currentExpanding)
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound

def hillClimbing(node: Tree, goal: list, forbidden: list, fringe: list, expanded: list):
    expand(node, goal, forbidden)
    expanded.append(node)
    foundGoal = False
    if node.data == goal:
        foundGoal == True
    for i in range(len(node.children)):
        fringe.append(node.children[i])
    heuristicValue = 0
    for j in range(len(node.data)):
        heuristicValue += abs(int(node.data[j]) - int(goal[j]))
    node.heuristic = heuristicValue
    bestV = node.heuristic
    while(len(fringe) > 0 and len(expanded) <= 1000 and not foundGoal):
        currentExpanding = -1
        currentMinH = 1000
        for i in range(len(fringe) - 1, -1, -1):
            if fringe[i].heuristic < bestV:
                bestV = fringe[i].heuristic
                currentExpanding = i
        if currentExpanding < 0:
            break
        expand(fringe[currentExpanding], goal, forbidden)
        alreadyExpanded = False
        for i in range(len(expanded)):
            if compare(fringe[currentExpanding], expanded[i]):
                alreadyExpanded = True
                break
        if alreadyExpanded:
            fringe.pop(currentExpanding)
            continue
        expanded.append(fringe[currentExpanding])
        if fringe[currentExpanding].data == goal:
            foundGoal = True
            break
        else:
            for i in range(len(fringe[currentExpanding].children)):
                fringe.append(fringe[currentExpanding].children[i])
        fringe.pop(currentExpanding)
    # Backtrack
    pathFound = []
    if foundGoal:
        pathFound.append(expanded[-1])
        backtracking = True
        while(backtracking):
            if pathFound[0].parent != None:
                pathFound.insert(0, pathFound[0].parent)
            else:
                backtracking = False
    return pathFound