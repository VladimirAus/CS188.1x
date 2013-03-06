Introduction

In this project, you will implement generic search algorithms applicable to wide classes of problems. The course staff has supplied an autograder which includes test cases based on small graphs to help you debug your implementations. Once you have debugged on the graph based test cases, you can apply your search algorithm implementations to pacman to help him find paths through his maze world.

As in Project 0, the autograder can be invoked locally for you to grade your answers on your machine. This can be run with the command:

python autograder.py
See the autograder tutorial in Project 0 for more information about using the autograder.

The code for this project consists of several Python files, some of which you will need to read and understand in order to complete the assignment, and some of which you can ignore. You can download all the code and supporting files as a zip archive.

Files you'll edit:
search.py
- Where all of your search algorithms will reside.
searchAgents.py
- Where all of your search-based agents will reside.

Files you might want to look at:
pacman.py
- The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project.
game.py	
- The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.
util.py
- Useful data structures for implementing search algorithms.

Supporting files you can ignore:
graphicsDisplay.py
- Graphics for Pacman
graphicsUtils.py
- Support for Pacman graphics
textDisplay.py
- ASCII graphics for Pacman
ghostAgents.py
- Agents to control ghosts
keyboardAgents.py
- Keyboard interfaces to control Pacman
layout.py
- Code for reading layout files and storing their contents
autograder.py
- Project autograder
testParser.py
- Parses autograder test and solution files
testClasses.py
- General autograding test classes
test_cases/
- Directory containing the test cases for each question
searchTestClasses.py	Project 1 specific autograding test classes

===================================

Welcome to Pacman

After downloading the code (search.zip), unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:

python pacman.py
Pacman lives in a shiny blue world of twisting corridors and tasty round treats. Navigating this world efficiently will be Pacman's first step in mastering his domain.

The simplest agent in searchAgents.py is called the GoWestAgent, which always goes West (a trivial reflex agent). This agent can occasionally win:

python pacman.py --layout testMaze --pacman GoWestAgent
But, things get ugly for this agent when turning is required:

python pacman.py --layout tinyMaze --pacman GoWestAgent
If Pacman gets stuck, you can exit the game by typing CTRL-c into your terminal.

Soon, your agent will solve not only tinyMaze, but any maze you want.

Note that pacman.py supports a number of options that can each be expressed in a long way (e.g., --layout) or a short way (e.g., -l). You can see the list of all options and their default values via:

python pacman.py -h

===================================

Question 1: Depth First Search (2 points)

In this question, you will implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py. To make your algorithm complete, write the graph search version of DFS, which avoids expanding any already visited states. As you work through the following questions, you might find it useful to refer to the object glossary (the second to last tab in the navigation bar above).

To help you get started, pseudocode for the search algorithms you'll write can be found in the lecture slides. Remember that a search node must contain not only a state but also the information necessary to reconstruct the path (plan) which gets to that state.

Important note: Make sure to use the Stack, Queue and PriorityQueue data structures provided to you in util.py! These data structure implementations have particular properties which are required for compatibility with the autograder.

Important note: All of your search functions need to return a list of actions that will reach a goal state from a start state.

Hint: Each algorithm is very similar. Algorithms for DFS, BFS, UCS, and A* differ only in the details of how the fringe is managed. So, concentrate on getting DFS right and the rest should be relatively straightforward. Indeed, one possible implementation requires only a single generic search method which is configured with an algorithm-specific queuing strategy. (Your implementation need not be of this form to receive full credit).

As you complete your implementation, you may test it using the command

python autograder.py -q q1
Notice that the autograder includes a graph based test (test_cases/q1/graph_infinite) designed to make sure you have implemented the graph version of DFS as this will be a necessary improvement in the Pacman world.

Applying Your Search Implementations to Pacman

In searchAgents.py, you'll find a fully implemented SearchAgent, which plans out a path through Pacman's world and then executes that path step-by-step. The search algorithms you implement in questions 1-4 will formulate the plan.

First, test that the SearchAgent is working correctly by running:

python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
The command above tells the SearchAgent to use tinyMazeSearch as its search algorithm, which is implemented in search.py. Pacman should navigate the maze successfully.

Once your DFS implementation is complete, your code should quickly find a solution for:

python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
The Pacman board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). Is the exploration order what you would have expected? Does Pacman actually go to all the explored squares on his way to the goal?

Hint: If you use a Stack as your data structure, the solution found by your DFS algorithm for mediumMaze should have a length of 130 (provided you push successors onto the fringe in the order provided by getSuccessors; you might get 246 if you push them in the reverse order). Is this a least cost solution? If not, think about what depth-first search is doing wrong.

=======================================