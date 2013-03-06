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
    return  [s,s,w,s,w,w,s,w]

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
    solution = breadthFirstSearchCheck(problem, [problem.getStartState()], vq, [problem.getStartState()])
    return solution

def breadthFirstSearchCheck(problem, nodesToCheck, visitedQueue, path):
    
    layerToSend = []

    walkedPath = path

    "First check width"
    for currentNode in nodesToCheck:
        visitedQueue.push(currentNode);
        
        successors = problem.getSuccessors(currentNode)
        for (state,direction,depth) in successors:
            if not visitedQueue.contains(state):
                layerToSend.append(state)
                if problem.isGoalState(state):
                    path.append(direction)
                    return path
    
    #print "Layer to send",layerToSend

    "New layer check"
    for currentNode in nodesToCheck:
        path = walkedPath
        path.append(currentNode)
        return breadthFirstSearchCheck(problem, layerToSend, visitedQueue, path)
    
    """
    if None not in q:
        #q.insert(0,getDerection(direction))
        q.insert(0,direction)
        return q

    #q = util.Queue()
    #q.push(None)
    
    """
    return [None]

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
