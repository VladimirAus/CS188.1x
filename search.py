# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

class VisitedQueue(util.Queue):
    """
    This class extends queue to provide list.
    """

    def __getitem__(self, index):
        return self.list[index]

    def index(self, elem):
        if (elem != None):
            return self.list.index(elem)
        else:
            return None

    def contains(self, elem):
        return elem in self.list

    def getList(self):
        return self.list

class VisitedStack(util.Stack):
    """
    This class extends queue to provide list.
    """

    def contains(self, elem):
        return elem in self.list

    def getList(self):
        return self.list

def getDerection(strDir):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    if strDir == 'North': return n
    if strDir == 'South': return s
    if strDir == 'East': return e
    if strDir == 'West': return w




def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #print "Start:", problem.getVisitedList()
    #print "Solution:", depthFirstSearchCheck(problem, problem.getStartState())

    vq = VisitedQueue()
    vq.push(problem.getStartState())
    solution = depthFirstSearchCheck(problem, problem.getStartState(), vq)
    #print "Solution:", solution
    #q = util.Queue()
    #for state in solution:
    #    q.push(state)
    return solution

    #util.raiseNotDefined()

def depthFirstSearchCheck(problem, currentNode, visitedQueue):
    
    "I fnow a goal, expand and check successors first"
    visitedQueue.push(currentNode);
    for (state,direction,depth) in problem.getSuccessors(currentNode):
        if not visitedQueue.contains(state):
        #direction, state, depth = successor
            if problem.isGoalState(state):
                #return [getDerection(direction)]
                return [direction]
            else:
                q = depthFirstSearchCheck(problem, state, visitedQueue)
                if None not in q:
                    #q.insert(0,getDerection(direction))
                    q.insert(0,direction)
                    return q

    #q = util.Queue()
    #q.push(None)
    return [None]

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    
    vq = VisitedQueue()
    #vq.push(problem.getStartState())
    (index, solution) = breadthFirstSearchCheck(problem, [[(problem.getStartState(), None, 0)]], vq, -1)
    print solution
    return solution

def breadthFirstSearchCheck(problem, currentLayer, visitedQueue, level):

    if (level == 99):
        print "Error"
        return []

    #print "0"
    nextLayer = []
    branchCount = -1
    level = level + 1

    # Checking layer before solution is found
    #print currentLayer;
    for branch in currentLayer:
        #print "1"
        branchCount = branchCount + 1
        for (state,direction,depth) in branch:
            #if not visitedQueue.contains(state):
            if problem.isGoalState(state):
                #print ("Solution", state)
                return (branchCount, [direction])
            if not visitedQueue.contains(state):
                visitedQueue.push(state)
                #print visitedQueue.getList()
                nextLayer.append(problem.getSuccessors(state))
            else:
                nextLayer.append([])


    
    """
    for branch2 in currentLayer:
        #print "2"
        for (state,direction,depth) in branch2:
            #print state
            if not visitedQueue.contains(state):
                visitedQueue.push(state)
                #print visitedQueue.getList()
                nextLayer.append(problem.getSuccessors(state))
    """

    (index, solution) = breadthFirstSearchCheck(problem, nextLayer, visitedQueue, level)
    #print (index, solution, currentLayer)
    if (level == 0):
        return (None, solution)
    branchCount = -1
    nodeCount = -1

    # Checking layer after solution was found
    for branch in currentLayer:
        branchCount = branchCount + 1
        for (state,direction,depth) in branch:
            nodeCount = nodeCount + 1
            if (index == nodeCount):
                #print direction
                solution.insert(0,direction)
                #print (branchCount, solution)
                return (branchCount, solution)


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    
    pq = util.PriorityQueue()
    vq = VisitedQueue()
    pq.push((problem.getStartState(), None, 0, []), 0)
    result = uniformCostSearchCheck(problem, pq, vq)
    print result
    return result

def uniformCostSearchCheck(problem, priorityQueue, visitedQueue):
    #print visitedQueue.getList()

    (coord,direction,cost,path) = priorityQueue.pop();
    print ("pop", coord,direction,cost)
    visitedQueue.push(coord);
    #if (direction != None):
    #    path.append(direction)

    if not problem.isGoalState(coord):
        for (cldCoord,cldDir,cldCost) in problem.getSuccessors(coord):
            pathNew = path[:]
            print ("Path", pathNew)
            if not visitedQueue.contains(cldCoord):
                print ("push", cldCoord,cldDir,cldCost, cost + cldCost)
                pathNew.append(cldDir)
                priorityQueue.push((cldCoord,cldDir,cost + cldCost,pathNew), cost + cldCost)

        path = uniformCostSearchCheck(problem, priorityQueue, visitedQueue);

    return path

"""
def uniformCostSearch2(problem):
    "Search the node of least total cost first. "
    
    pq = util.PriorityQueue()
    vq = VisitedQueue()
    prq = VisitedQueue()
    dq = VisitedQueue()
    iq = VisitedQueue()
    #print problem.getStartState()
    #s = problem.getStartState()
    #pa.push(None)
    pq.push((problem.getStartState(), None, 0, None), 0)
    (direct, coord) = uniformCostSearchCheck2(problem, pq, vq, prq, dq, iq, 0)
    #print convertPathToDir(solution)
    #direct = []
    #print direct
    direct.pop(len(direct)-1)
    return (direct)


def uniformCostSearchCheck2(problem, priorityQueue, visitedQueue, parentsQueue, dirQueue, indexQueue, index):

    #print "ucs"
    #print priorityQueue.pop()
    #return [];

    (coord,direction,cost,parent, oldIndex) = priorityQueue.pop();
    visitedQueue.push(coord);
    #if (parent != None):
    parentsQueue.push(parent);
    dirQueue.push(direction);
    indexQueue.push(oldIndex)
    
    q = []
    if problem.isGoalState(coord):
        #print "goals"
        return ([direction],[coord])
    index = index + 1

    else:
        for (cldCoord,cldDir,cldCost) in problem.getSuccessors(coord):
            if not visitedQueue.contains(cldCoord):
                priorityQueue.push((cldCoord,cldDir,cldCost,coord), cost + cldCost)
                #(x,y) = cldCoord
                #parentsArray[x][y] = coord
        (d,q) = uniformCostSearchCheck2(problem, priorityQueue, visitedQueue, parentsQueue, dirQueue, indexQueue, index);
        ind = visitedQueue.index(q[0])
        #(x1,y1) = q[0]
        if (parentsQueue[ind] != None):
            q.insert(0,parentsQueue[ind])
            d.insert(0,dirQueue[ind])
        return (d,q)

    print "No solution"
    #return q

def convertPathToDir(path):
    #print path
    dir = []
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    for i in range(len(path)-1):
        (x1,y1) = path[i]
        (x2,y2) = path[i+1]
        if (x1-x2 == 1): 
            dir.append(w)
        if (x2-x1 == 1): 
            dir.append(e)
        if (y1-y2 == 1): 
            dir.append(s)
        if (x2-x1 == 1): 
            dir.append(n)

    return dir
"""

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
