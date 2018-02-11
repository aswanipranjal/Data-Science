from mdp import *

sequential_decision_environment_1 = GridMDP([[-0.1, -0.1, -0.1, +1],
                                             [-0.1, None, -0.1, -1],
                                             [-0.1, -0.1, -0.1, -0.1]],
                                            terminals=[(3, 2), (3, 1)])

sequential_decision_environment_2 = GridMDP([[-2, -2, -2, +1],
                                             [-2, None, -2, -1],
                                             [-2, -2, -2, -2]],
                                            terminals=[(3, 2), (3, 1)])

sequential_decision_environment_3 = GridMDP([[-0.04, -0.04, -0.04, -0.04, -0.04, 1.0, -1.0],
                                             [-0.04, None, -1.0, -0.04, -0.04, -0.04, -0.04],
                                             [-0.04, None, None, 4.0, None, None, -0.04],
                                             [-0.04, -0.04, -0.04, -0.04, -1.0, None, -0.04],
                                             [-1.0, 1.0, -0.04, -0.04, -0.04, -0.04 -0.04]], 
                                             terminals=[(3, 2), (2, 3), (4, 1), (1, 0), (5, 4)])

def test_value_iteration():
    assert value_iteration(sequential_decision_environment, .01) == {
        (3, 2): 1.0, (3, 1): -1.0,
        (3, 0): 0.12958868267972745, (0, 1): 0.39810203830605462,
        (0, 2): 0.50928545646220924, (1, 0): 0.25348746162470537,
        (0, 0): 0.29543540628363629, (1, 2): 0.64958064617168676,
        (2, 0): 0.34461306281476806, (2, 1): 0.48643676237737926,
        (2, 2): 0.79536093684710951}

    assert value_iteration(sequential_decision_environment_1, .01) == {
        (3, 2): 1.0, (3, 1): -1.0,  
        (3, 0): -0.0897388258468311, (0, 1): 0.146419707398967840, 
        (0, 2): 0.30596200514385086, (1, 0): 0.010092796415625799,
        (0, 0): 0.00633408092008296, (1, 2): 0.507390193380827400, 
        (2, 0): 0.15072242145212010, (2, 1): 0.358309043654212570, 
        (2, 2): 0.71675493618997840}

    assert value_iteration(sequential_decision_environment_2, .01) == {
        (3, 2): 1.0, (3, 1): -1.0, 
        (3, 0): -3.5141584808407855, (0, 1): -7.8000009574737180,
        (0, 2): -6.1064293596058830, (1, 0): -7.1012549580376760,
        (0, 0): -8.5872244532783200, (1, 2): -3.9653547121245810,
        (2, 0): -5.3099468802901630, (2, 1): -3.3543366255753995,
        (2, 2): -1.7383376462930498}


def test_policy_iteration():
    assert policy_iteration(sequential_decision_environment) == {
        (0, 0): (0, 1), (0, 1): (0, 1), (0, 2): (1, 0),
        (1, 0): (1, 0), (1, 2): (1, 0), (2, 0): (0, 1),
        (2, 1): (0, 1), (2, 2): (1, 0), (3, 0): (-1, 0),
        (3, 1): None, (3, 2): None}

    assert policy_iteration(sequential_decision_environment_1) == {
        (0, 0): (0, 1), (0, 1): (0, 1), (0, 2): (1, 0),
        (1, 0): (1, 0), (1, 2): (1, 0), (2, 0): (0, 1),
        (2, 1): (0, 1), (2, 2): (1, 0), (3, 0): (-1, 0),
        (3, 1): None, (3, 2): None}

    assert policy_iteration(sequential_decision_environment_2) == {
        (0, 0): (1, 0), (0, 1): (0, 1), (0, 2): (1, 0),
        (1, 0): (1, 0), (1, 2): (1, 0), (2, 0): (1, 0),
        (2, 1): (1, 0), (2, 2): (1, 0), (3, 0): (0, 1),
        (3, 1): None, (3, 2): None}


def test_best_policy():
    pi = best_policy(sequential_decision_environment,
                     value_iteration(sequential_decision_environment, .01))
    assert sequential_decision_environment.to_arrows(pi) == [['>', '>', '>', '.'],
                                                             ['^', None, '^', '.'],
                                                             ['^', '>', '^', '<']]

    pi_1 = best_policy(sequential_decision_environment_1,
                     value_iteration(sequential_decision_environment_1, .01))
    assert sequential_decision_environment_1.to_arrows(pi_1) == [['>', '>', '>', '.'],
                                                                 ['^', None, '^', '.'],
                                                                 ['^', '>', '^', '<']]

    pi_2 = best_policy(sequential_decision_environment_2,
                     value_iteration(sequential_decision_environment_2, .01))
    assert sequential_decision_environment_2.to_arrows(pi_2) == [['>', '>', '>', '.'],
                                                                 ['^', None, '>', '.'],
                                                                 ['>', '>', '>', '^']]                                                             


def test_transition_model():
    transition_model = {
        "A": {"a1": (0.3, "B"), "a2": (0.7, "C")},
        "B": {"a1": (0.5, "B"), "a2": (0.5, "A")},
        "C": {"a1": (0.9, "A"), "a2": (0.1, "B")},
    }

    mdp = MDP(init="A", actlist={"a1","a2"}, terminals={"C"}, states={"A","B","C"}, transitions=transition_model)

    assert mdp.T("A","a1") == (0.3, "B")
    assert mdp.T("B","a2") == (0.5, "A")
    assert mdp.T("C","a1") == (0.9, "A")
