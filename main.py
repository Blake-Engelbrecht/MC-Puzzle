"""
Project:            Missionaries and Cannibals 
Description:        Solve the MC puzzle using BFS, see README for further details.
Contributors:       Blake Engelbrecht
Date:               1/28/2021 
"""

import math

#this class represents the state of the game at a moment in time, used to determine next action as well as checking if the state is valid.
class State():
    def __init__(self, cLeft, mLeft, boat, cRight, mRight):
        self.cLeft = cLeft
        self.mLeft = mLeft
        self.boat = boat
        self.cRight = cRight
        self.mRight = mRight
        self.parent = None
    
    def is_goal_state(self):
        if self.cRight == 0 and self.mRight == 0:
            return True
        else:
            return False

    def is_valid_state(self):
        if (self.mLeft >= 0 and self.mRight >= 0 
            and self.cLeft >= 0 and self.cRight >= 0 
            and (self.mLeft == 0 or self.mLeft >= self.cLeft) 
            and (self.mRight == 0 or self.mRight >= self.cRight)):
            return True
        else:
            return False

    def __eq__(self, other):
        return (self.cLeft == other.cLeft and self.mLeft == other.mLeft and self.boat == other.boat 
                and self.cRight == other.cRight and self.mRight == other.mRight)

    def __hash__(self):
        return hash((self.cLeft, self.mLeft, self.boat, self.cRight, self.mRight))

#all valid moves within the current state space.
def successors(current_state):
    moves = [];
    if current_state.boat == 'right':
        new_state = State(current_state.cLeft, current_state.mLeft +2, 'left',
                    current_state.cRight, current_state.mRight - 2) # 2 missionaries cross left <- right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft + 2, current_state.mLeft, 'left', 
                            current_state.cRight - 2, current_state.mRight) # 2 cannibals cross left <- right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft + 1, current_state.mLeft + 1, 'left',
                            current_state.cRight - 1, current_state.mRight -1) # 1 missionary and 1 cannibal cross left <- right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft, current_state.mLeft + 1, 'left',
                            current_state.cRight, current_state.mRight - 1) # 1 missionary crosses left <- right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft + 1, current_state.mLeft, 'left',
                            current_state.cRight - 1, current_state.mRight) # 1 cannibal crosses left <- right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state) #state is created and validated but no moves are made 

    else:
        new_state = State(current_state.cLeft, current_state.mLeft - 2, 'right',
                    current_state.cRight, current_state.mRight + 2) # 2 missionaries cross left -> right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft - 2, current_state.mLeft, 'right',
                            current_state.cRight + 2, current_state.mRight) # 2 cannibals cross left -> right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft - 1, current_state.mLeft - 1, 'right',
                            current_state.cRight + 1, current_state.mRight + 1) # 1 missionary and 1 cannibal cross left -> right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft, current_state.mLeft - 1, 'right',
                            current_state.cRight, current_state.mRight + 1) # 1 missionary crosses left -> right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state)
        new_state = State(current_state.cLeft - 1, current_state.mLeft, 'right',
                            current_state.cRight + 1, current_state.mRight) # 1 cannibal crosses left -> right

        if new_state.is_valid_state():
            new_state.parent = current_state
            moves.append(new_state) #state is created and validated but no moves are made 

    return moves

#search algorithm used to find the goal state. 
def BFS():
    initial_state = State(0,0,'right',3,3)
    if initial_state.is_goal_state():
        return initial_state

    queue = list()
    visited = set()
    queue.append(initial_state)

    while queue:
        state = queue.pop(0)
        if state.is_goal_state():
            return state
        visited.add(state)
        graph = successors(state)
        for neighbor in graph:
            if (neighbor not in visited) or (neighbor not in queue):
                queue.append(neighbor)
    
    return None

def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print("{}c, {}m --------------- {} --------------- {}c, {}m".format(state.cLeft, state.mLeft, state.boat, state.cRight, state.mRight))


solution = BFS()

print("\n")
print("            MISSIONARIES AND CANNIBALS")
print("______________________________________________________")
print("LEFT SIDE OF RIVER, Boat Position, RIGHT SIDE OF RIVER")

print_solution(solution)