"""Markov Decision Processes (Chapter 17)

First we define an MDP, and the special case of a GridMDP, in which
states are laid out in a 2-dimensional grid. We also represent a policy
as a dictionary of {state:action} pairs, and a Utility function as a
dictionary of {state:number} pairs. We then define the value_iteration
and policy_iteration algorithms."""

from utils import argmax, vector_add, orientations, turn_right, turn_left

import random


class MDP:

    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. We also keep track of a gamma value, for use by
    algorithms. The transition model is represented somewhat differently from
    the text. Instead of P(s' | s, a) being a probability number for each
    state/state/action triplet, we instead have T(s, a) return a
    list of (p, s') pairs. We also keep track of the possible states,
    terminal states, and actions for each state. [page 646]"""

    def __init__(self, init, actlist, terminals, transitions = {}, reward = None, states=None, gamma=.9):
        if not (0 < gamma <= 1):
            raise ValueError("An MDP must have 0 < gamma <= 1")

        if states:
            self.states = states
        else:
            ## collect states from transitions table
            self.states = self.get_states_from_transitions(transitions)
            
        
        self.init = init
        
        if isinstance(actlist, list):
            ## if actlist is a list, all states have the same actions
            self.actlist = actlist
        elif isinstance(actlist, dict):
            ## if actlist is a dict, different actions for each state
            self.actlist = actlist
        
        self.terminals = terminals
        self.transitions = transitions
        if self.transitions == {}:
            print("Warning: Transition table is empty.")
        self.gamma = gamma
        if reward:
            self.reward = reward
        else:
            self.reward = {s : 0 for s in self.states}
        #self.check_consistency()

    def R(self, state):
        """Return a numeric reward for this state."""
        return self.reward[state]

    def T(self, state, action):
        """Transition model. From a state and an action, return a list
        of (probability, result-state) pairs."""
        if(self.transitions == {}):
            raise ValueError("Transition model is missing")
        else:
            return self.transitions[state][action]

    def actions(self, state):
        """Set of actions that can be performed in this state. By default, a
        fixed list of actions, except for terminal states. Override this
        method if you need to specialize by state."""
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

    def get_states_from_transitions(self, transitions):
        if isinstance(transitions, dict):
            s1 = set(transitions.keys())
            s2 = set([tr[1] for actions in transitions.values() 
                              for effects in actions.values() for tr in effects])
            return s1.union(s2)
        else:
            print('Could not retrieve states from transitions')
            return None

    def check_consistency(self):
        # check that all states in transitions are valid
        assert set(self.states) == self.get_states_from_transitions(self.transitions)
        # check that init is a valid state
        assert self.init in self.states
        # check reward for each state
        #assert set(self.reward.keys()) == set(self.states)
        assert set(self.reward.keys()) == set(self.states)
        # check that all terminals are valid states
        assert all([t in self.states for t in self.terminals])
        # check that probability distributions for all actions sum to 1
        for s1, actions in self.transitions.items():
            for a in actions.keys():
                s = 0
                for o in actions[a]:
                    s += o[0]
                assert abs(s - 1) < 0.001


class GridMDP(MDP):

    """A two-dimensional grid MDP, as in [Figure 17.1]. All you have to do is
    specify the grid as a list of lists of rewards; use None for an obstacle
    (unreachable state). Also, you should specify the terminal states.
    An action is an (x, y) unit vector; e.g. (1, 0) means move east."""

    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        grid.reverse()  # because we want row 0 on bottom, not on top
        reward = {}
        states = set()
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        for x in range(self.cols):
            for y in range(self.rows):
                if grid[y][x] is not None:
                    states.add((x, y))
                    reward[(x, y)] = grid[y][x]
        self.states = states
        actlist = orientations
        transitions = {}
        for s in states:
            transitions[s] = {}
            for a in actlist:
                transitions[s][a] = self.calculate_T(s, a)
        MDP.__init__(self, init, actlist=actlist,
                     terminals=terminals, transitions = transitions, 
                     reward = reward, states = states, gamma=gamma)

    def calculate_T(self, state, action):
        if action is None:
            return [(0.0, state)]
        else:
            return [(0.8, self.go(state, action)),
                    (0.1, self.go(state, turn_right(action))),
                    (0.1, self.go(state, turn_left(action)))]
    
    def T(self, state, action):
        if action is None:
            return [(0.0, state)]
        else:
            return self.transitions[state][action]
 
    def go(self, state, direction):
        """Return the state that results from going in this direction."""
        state1 = vector_add(state, direction)
        return state1 if state1 in self.states else state

    def to_grid(self, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        return list(reversed([[mapping.get((x, y), None)
                               for x in range(self.cols)]
                              for y in range(self.rows)]))

    def to_arrows(self, policy):
        chars = {
            (1, 0): '>', (0, 1): '^', (-1, 0): '<', (0, -1): 'v', None: '.'}
        return self.to_grid({s: chars[a] for (s, a) in policy.items()})


class POMDP(MDP):
    
    def __init__(self, init, actlist, terminals, transitions={}, sensor=None, reward=None, states=None, gamma=.9):
        if not (0 < gamma <= 1):
            raise ValueError('An MDP must have 0 < gamma <= 1')

        if states:
            self.states = states
        else:
            self.states = self.get_states_from_transitions(transitions)

        self.init = init
        self.terminals = self.terminals
        self.transitions = transitions
        if self.transitions == {}:
            print('Warning: Transition table is empty.')
        self.gamma = gamma
        if reward:
            self.reward = reward
        else:
            self.reward = {s : 0 for s in self.states}

    def R(self, state):
        return self.reward[state]

    def S(self, state):
        # The sensor model specifies the probability of perceiving evidence e in state s
        return self.sensor[state]

    def T(self, state, action):
        if self.transitions == {}:
            raise ValueError('Transition model is missing.')
        else:
            self.transitions[state][action]

    def actions(self, state):
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

    def get_states_from_transitions(self, transitions):
        if isinstance(transitions, dict):
            s1 = set(transitions.keys())
            s2 = set([tr[1] for actions in transitions.values() for effects in actions.values() for tr in effects])
            return s1.union(s2)
        else:
            print('Could not retrieve states from transitions')
            return None
'''
belief_state for grid mdp:
b = [_, _, _, 0]
    [_, 0, _, 0]
    [_, _, _, _]
sum(b) = 1
b = [1/9, 1/9, 1/9,   0]
    [1/9,   0, 1/9,   0]
    [1/9, 1/9, 1/9, 1/9]
Let s = (1, 1)
b(s) = 1/9
P(s` | s, a)
s = (1, 1)
a = 'right', 'left', 'up', 'down'
Let a = 'right'
s` = {(1, 1):0.1, (2, 1):0.8, (1, 2):0.1}
'''


    def get_belief_state(self, belief, action, evidence, alpha):
        new_belief_state = alpha * P(evidence | state`) * sum(P(state` | state, action) * belief[state])
        return new_belief_state

def pomdp_value_iteration(pomdp, epsilon=0.001):
    '''Solving a POMDP by value iteration.'''
    U1 = # To initialize
    R, T, S, gamma = pomdp.R, pomdp.T, pomdp.S, pomdp.gamma
    while True:
        U = U1.copy()
        U1 = # The set of all plans consisting of an action and, for eachpossible next percept, a plan U with utility vectors computed according to equation (17.13)
        U1 = remove_dominated_plans(U1)

# ______________________________________________________________________________


""" [Figure 17.1]
A 4x3 grid environment that presents the agent with a sequential decision problem.
"""

sequential_decision_environment = GridMDP([[-0.04, -0.04, -0.04, +1],
                                           [-0.04, None, -0.04, -1],
                                           [-0.04, -0.04, -0.04, -0.04]],
                                          terminals=[(3, 2), (3, 1)])

# ______________________________________________________________________________


def value_iteration(mdp, epsilon=0.001):
    """Solving an MDP by value iteration. [Figure 17.4]"""
    U1 = {s: 0 for s in mdp.states}
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
            return U


def best_policy(mdp, U):
    """Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
    return pi


def expected_utility(a, s, U, mdp):
    """The expected utility of doing a in state s, according to the MDP and U."""
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])

# ______________________________________________________________________________


def policy_iteration(mdp):
    """Solve an MDP by policy iteration [Figure 17.7]"""
    U = {s: 0 for s in mdp.states}
    pi = {s: random.choice(mdp.actions(s)) for s in mdp.states}
    while True:
        U = policy_evaluation(pi, U, mdp)
        unchanged = True
        for s in mdp.states:
            a = argmax(mdp.actions(s), key=lambda a: expected_utility(a, s, U, mdp))
            if a != pi[s]:
                pi[s] = a
                unchanged = False
        if unchanged:
            return pi


def policy_evaluation(pi, U, mdp, k=20):
    """Return an updated utility mapping U from each state in the MDP to its
    utility, using an approximation (modified policy iteration)."""
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    for i in range(k):
        for s in mdp.states:
            U[s] = R(s) + gamma * sum([p * U[s1] for (p, s1) in T(s, pi[s])])
    return U


__doc__ += """
>>> pi = best_policy(sequential_decision_environment, value_iteration(sequential_decision_environment, .01))

>>> sequential_decision_environment.to_arrows(pi)
[['>', '>', '>', '.'], ['^', None, '^', '.'], ['^', '>', '^', '<']]

>>> from utils import print_table

>>> print_table(sequential_decision_environment.to_arrows(pi))
>   >      >   .
^   None   ^   .
^   >      ^   <

>>> print_table(sequential_decision_environment.to_arrows(policy_iteration(sequential_decision_environment)))
>   >      >   .
^   None   ^   .
^   >      ^   <
"""  # noqa

"""
s = { 'a' : {	'plan1' : [(0.2, 'a'), (0.3, 'b'), (0.3, 'c'), (0.2, 'd')],
				'plan2' : [(0.4, 'a'), (0.15, 'b'), (0.45, 'c')],
				'plan3' : [(0.2, 'a'), (0.5, 'b'), (0.3, 'c')],
			},
	  'b' : {	'plan1' : [(0.2, 'a'), (0.6, 'b'), (0.2, 'c'), (0.1, 'd')],
				'plan2' : [(0.6, 'a'), (0.2, 'b'), (0.1, 'c'), (0.1, 'd')],
				'plan3' : [(0.3, 'a'), (0.3, 'b'), (0.4, 'c')],
			},
	  'c' : {	'plan1' : [(0.3, 'a'), (0.5, 'b'), (0.1, 'c'), (0.1, 'd')],
				'plan2' : [(0.5, 'a'), (0.3, 'b'), (0.1, 'c'), (0.1, 'd')],
				'plan3' : [(0.1, 'a'), (0.3, 'b'), (0.1, 'c'), (0.5, 'd')],
	  		},
	}
"""