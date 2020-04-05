class Tree(object):
    def __init__(self, parent=None, data=[], heuristic=-1, isGoal=False, modifiedValue=-1, depth=0):
        self.parent = parent
        self.children = []
        self.data = data
        self.heuristic = heuristic
        self.isGoal = isGoal
        self.modifiedValue = modifiedValue
        self.depth = depth
    
    def addChild(self, child):
        self.children.append(child)

def expand(node: Tree, goal, forbidden):
    if(node.data == goal):
        return
    if len(node.children) > 0:
        return

    for i in range(3):
        if node.modifiedValue == i:
            continue
        # Subtract
        newValue = list(node.data)
        if int(newValue[i]) > 0:
            newValue[i] = str(int(newValue[i]) - 1)
            isForbidden = False
            for j in range(len(forbidden)):
                if newValue == forbidden[j]:
                    isForbidden = True
            if not isForbidden:
                isGoal = (newValue == goal)
                heuristicValue = 0
                for j in range(len(node.data)):
                    heuristicValue += abs(int(newValue[j]) - int(goal[j]))
                newNode = Tree(node, newValue, heuristicValue, isGoal, i, node.depth + 1)
                node.addChild(newNode)

        # Add
        newValue = list(node.data)
        if int(newValue[i]) < 9:
            newValue[i] = str(int(newValue[i]) + 1)
            isForbidden = False
            for j in range(len(forbidden)):
                if newValue == forbidden[j]:
                    isForbidden = True
            if not isForbidden:
                isGoal = (newValue == goal)
                heuristicValue = 0
                for j in range(3):
                    heuristicValue += abs(int(newValue[j]) - int(goal[j]))
                newNode = Tree(node, newValue, heuristicValue, isGoal, i, node.depth + 1)
                node.addChild(newNode)

def compare(node1: Tree, node2: Tree):
    areEqual = False
    if node1.data == node2.data:
        node1Data = []
        for child in node1.children:
            node1Data.append(child.data)
        hasDifference = False
        for child in node2.children:
            if not child.data in node1Data:
                hasDifference = True
                break
        if not hasDifference:
            areEqual = True
    return areEqual
    
