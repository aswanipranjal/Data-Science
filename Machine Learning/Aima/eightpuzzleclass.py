class Problem(object):

    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


class EightPuzzle(Problem):

    """The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank. A state is represented as a 3x3 list,
    where element at index i,j represents the tile number (0 if it's an empty square)."""
 
    def __init__(self, initial, goal=None):
        if goal is not None:
            self.goal = goal
        elif goal is None:
            self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        Problem.__init__(self, initial, goal)
    
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)
    
    def actions(self, state):
        """Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment."""
       
        possible_actions = []
        index_blank_square = self.find_blank_square(state)

        if index_blank_square == 0:
            possible_actions = ['DOWN', 'RIGHT']
        elif index_blank_square == 1:
            possible_actions = ['LEFT', 'DOWN', 'RIGHT']
        elif index_blank_square == 2:
            possible_actions = ['LEFT', 'DOWN']
        elif index_blank_square == 3:
            possible_actions = ['UP', 'RIGHT', 'DOWN']
        elif index_blank_square == 4:
            possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        elif index_blank_square == 5:
            possible_actions = ['LEFT', 'UP', 'DOWN']
        elif index_blank_square == 6:
            possible_actions = ['UP', 'RIGHT']
        elif index_blank_square == 7:
            possible_actions = ['UP', 'LEFT', 'RIGHT']
        elif index_blank_square == 8:
            possible_actions = ['LEFT', 'UP']

        return possible_actions

    def result(self, state, action):
        """Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state."""

        # ix is the index of the blank square
        ix = self.find_blank_square(state)
        new_state = [None] * len(state)

        if action == 'UP':
            new_state[ix], new_state[ix - 3] = new_state[ix - 3], 0
        elif action == 'DOWN':
            new_state[ix], new_state[ix + 3] = new_state[ix + 3], 0
        elif action == 'LEFT':
            new_state[ix], new_state[ix - 1] = new_state[ix - 1], 0
        elif action == 'RIGHT':
            new_state[ix], new_state[ix + 1] = new_state[ix + 1], 0
        else:
            print('Invalid Action')

        return new_state

    def goal_test(self, state):
        """Given a state, return True if state is a goal state or False, otherwise"""
        if state == self.goal:
            return True
        return False

    def checkSolvability(self, state):
        inversion = 0
        for i in range(len(state)):
               for j in range(i, len(state)):
                    if (state[i] > state[j] and state[j] != 0):
                                    inversion += 1
        check = True
        if inversion % 2 != 0:
                check = False
        print(check)
    
    def h(self, state):
        """Return the heuristic value for a given state. Heuristic function used is 
        h(n) = number of misplaced tiles."""
        num_misplaced_tiles = 0

        for i in range(len(state)):
            if state[i] != self.goal[i]:
                num_misplaced_tiles += 1

        return num_misplaced_tiles