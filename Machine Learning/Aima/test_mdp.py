from mdp import *

sequential_decision_environment_1 = GridMDP([[-0.1, -0.1, -0.1, +1],
                                             [-0.1, None, -0.1, -1],
                                             [-0.1, -0.1, -0.1, -0.1]],
                                            terminals=[(3, 2), (3, 1)])

def test_value_iteration():
    assert value_iteration(sequential_decision_environment, .01) == {
        (3, 2): 1.0, (3, 1): -1.0,
        (3, 0): 0.12958868267972745, (0, 1): 0.39810203830605462,
        (0, 2): 0.50928545646220924, (1, 0): 0.25348746162470537,
        (0, 0): 0.29543540628363629, (1, 2): 0.64958064617168676,
        (2, 0): 0.34461306281476806, (2, 1): 0.48643676237737926,
        (2, 2): 0.79536093684710951}

    assert value_iteration(sequential_decision_environment_1, .01) == {(0, 1): 0.14641970739896784, (1, 2): 0.5073901933808274, (3, 2): 1.0, (0, 0): 0.00633408092008296, (3, 0): -0.0897388258468311, (3, 1): -1.0, (2, 1): 0.35830904365421257, (2, 0): 0.1507224214521201, (2, 2): 0.7167549361899784, (1, 0): 0.010092796415625799, (0, 2): 0.30596200514385086}


def test_policy_iteration():
    assert policy_iteration(sequential_decision_environment) == {
        (0, 0): (0, 1), (0, 1): (0, 1), (0, 2): (1, 0),
        (1, 0): (1, 0), (1, 2): (1, 0), (2, 0): (0, 1),
        (2, 1): (0, 1), (2, 2): (1, 0), (3, 0): (-1, 0),
        (3, 1): None, (3, 2): None}


def test_best_policy():
    pi = best_policy(sequential_decision_environment,
                     value_iteration(sequential_decision_environment, .01))
    assert sequential_decision_environment.to_arrows(pi) == [['>', '>', '>', '.'],
                                                             ['^', None, '^', '.'],
                                                             ['^', '>', '^', '<']]


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
