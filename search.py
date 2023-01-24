# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    visited.add(problem.getStartState()[0])
    commands = []
    fringes = util.Stack()
    for (location, direction, _) in problem.getSuccessors(problem.getStartState()):
        fringes.push((location, direction, commands.copy()))

    while not fringes.isEmpty():
        (fringe_pos, fringe_direction, fringe_commands) = fringes.pop()
        if fringe_pos in visited:
            continue
        visited.add(fringe_pos)
        fringe_commands_copy = fringe_commands.copy()
        fringe_commands_copy.append(fringe_direction)
        
        if problem.isGoalState(fringe_pos):
            return fringe_commands_copy

        successors = problem.getSuccessors(fringe_pos)
        for (location, direction, _) in successors:
            fringes.push((location, direction, fringe_commands_copy.copy()))
    return None
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    visited.add(problem.getStartState()[0])
    commands = []
    fringes = util.Queue()
    for (location, direction, _) in problem.getSuccessors(problem.getStartState()):
        fringes.push((location, direction, commands))

    while not fringes.isEmpty():
        (fringe_pos, fringe_direction, commands) = fringes.pop()
        if fringe_pos in visited:
            continue
        visited.add(fringe_pos)
        cmds = commands.copy()
        cmds.append(fringe_direction)
        if problem.isGoalState(fringe_pos):
            return cmds
        successors = problem.getSuccessors(fringe_pos)
        for (location, direction, _) in successors:
            fringes.push((location, direction, cmds))
    return None
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    visited.add(problem.getStartState()[0])
    commands = []
    fringes = util.PriorityQueue()
    for (location, direction, cost) in problem.getSuccessors(problem.getStartState()):
        fringes.push((location, direction, commands, cost), cost)

    while not fringes.isEmpty():
        (fringe_pos, fringe_direction, commands, fringe_cost) = fringes.pop()
        if fringe_pos in visited:
            continue
        visited.add(fringe_pos)
        cmds = commands.copy()
        cmds.append(fringe_direction)
        if problem.isGoalState(fringe_pos):
            return cmds
        successors = problem.getSuccessors(fringe_pos)
        for (location, direction, cost) in successors:
            fringes.push((location, direction, cmds, fringe_cost + cost), fringe_cost + cost)
    return None
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set()
    visited.add(problem.getStartState()[0])
    commands = []
    fringes = util.PriorityQueue()
    for (location, direction, cost) in problem.getSuccessors(problem.getStartState()):
        actual_cost = cost + heuristic(location, problem)
        fringes.push((location, direction, commands, actual_cost), actual_cost)

    while not fringes.isEmpty():
        (fringe_pos, fringe_direction, commands, fringe_cost) = fringes.pop()
        if fringe_pos in visited:
            continue
        visited.add(fringe_pos)
        cmds = commands.copy()
        cmds.append(fringe_direction)
        if problem.isGoalState(fringe_pos):
            return cmds
        successors = problem.getSuccessors(fringe_pos)
        for (location, direction, cost) in successors:
            actual_cost = cost + heuristic(location, problem) + problem.getCostOfActions(cmds)
            fringes.push((location, direction, cmds, actual_cost), actual_cost)
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
