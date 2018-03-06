import pytest
from search import *


romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
vacumm_world = GraphProblemStochastic('State_1', ['State_7', 'State_8'], vacumm_world)
LRTA_problem = OnlineSearchProblem('State_3', 'State_5', one_dim_state_space)
eight_puzzle = EightPuzzle([6, 3, 5, 1, 8, 4, 2, 0, 7])
eight_puzzle2 = EightPuzzle([1, 0, 6, 8, 7, 5, 4, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8])

def test_find_min_edge():
    assert romania_problem.find_min_edge() == 70


def test_breadth_first_tree_search():
    assert breadth_first_tree_search(
        romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def test_breadth_first_search():
    assert breadth_first_search(romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def test_best_first_graph_search():
    # uniform_cost_search and astar_search test it indirectly
    assert best_first_graph_search(
        romania_problem,
        lambda node: node.state).solution() == ['Sibiu', 'Fagaras', 'Bucharest']
    assert best_first_graph_search(
        romania_problem,
        lambda node: node.state[::-1]).solution() == ['Timisoara',
                                                      'Lugoj',
                                                      'Mehadia',
                                                      'Drobeta',
                                                      'Craiova',
                                                      'Pitesti',
                                                      'Bucharest']


def test_uniform_cost_search():
    assert uniform_cost_search(
        romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']


def test_depth_first_graph_search():
    solution = depth_first_graph_search(romania_problem).solution()
    assert solution[-1] == 'Bucharest'


def test_iterative_deepening_search():
    assert iterative_deepening_search(
        romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


def test_depth_limited_search():
    solution_3 = depth_limited_search(romania_problem, 3).solution()
    assert solution_3[-1] == 'Bucharest'
    assert depth_limited_search(romania_problem, 2) == 'cutoff'
    solution_50 = depth_limited_search(romania_problem).solution()
    assert solution_50[-1] == 'Bucharest'


def test_bidirectional_search():
    assert bidirectional_search(romania_problem) == 418


def test_astar_search():
    assert astar_search(romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']


def test_find_blank_square():
    assert eight_puzzle.find_blank_square([0, 1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert eight_puzzle.find_blank_square([6, 3, 5, 1, 8, 4, 2, 0, 7]) == 7
    assert eight_puzzle.find_blank_square([3, 4, 1, 7, 6, 0, 2, 8, 5]) == 5
    assert eight_puzzle.find_blank_square([1, 8, 4, 7, 2, 6, 3, 0, 5]) == 7
    assert eight_puzzle.find_blank_square([4, 8, 1, 6, 0, 2, 3, 5, 7]) == 4
    assert eight_puzzle.find_blank_square([1, 0, 6, 8, 7, 5, 4, 2, 3]) == 1
    assert eight_puzzle.find_blank_square([1, 2, 3, 4, 5, 6, 7, 8, 0]) == 8


def test_actions():
    assert eight_puzzle.actions([0, 1, 2, 3, 4, 5, 6, 7, 8]) == ['DOWN', 'RIGHT']
    assert eight_puzzle.actions([6, 3, 5, 1, 8, 4, 2, 0, 7]) == ['UP', 'LEFT', 'RIGHT']
    assert eight_puzzle.actions([3, 4, 1, 7, 6, 0, 2, 8, 5]) == ['UP', 'DOWN', 'LEFT']
    assert eight_puzzle.actions([1, 8, 4, 7, 2, 6, 3, 0, 5]) == ['UP', 'LEFT', 'RIGHT']
    assert eight_puzzle.actions([4, 8, 1, 6, 0, 2, 3, 5, 7]) == ['UP', 'DOWN', 'LEFT', 'RIGHT']
    assert eight_puzzle.actions([1, 0, 6, 8, 7, 5, 4, 2, 3]) == ['DOWN', 'LEFT', 'RIGHT']
    assert eight_puzzle.actions([1, 2, 3, 4, 5, 6, 7, 8, 0]) == ['UP', 'LEFT']


def test_result():
    assert eight_puzzle.result([0, 1, 2, 3, 4, 5, 6, 7, 8], 'DOWN') == (3, 1, 2, 0, 4, 5, 6, 7, 8)
    assert eight_puzzle.result([6, 3, 5, 1, 8, 4, 2, 0, 7], 'LEFT') == (6, 3, 5, 1, 8, 4, 0, 2, 7)
    assert eight_puzzle.result([3, 4, 1, 7, 6, 0, 2, 8, 5], 'UP') == (3, 4, 0, 7, 6, 1, 2, 8, 5)
    assert eight_puzzle.result([1, 8, 4, 7, 2, 6, 3, 0, 5], 'RIGHT') == (1, 8, 4, 7, 2, 6, 3, 5, 0)
    assert eight_puzzle.result([4, 8, 1, 6, 0, 2, 3, 5, 7], 'LEFT') == (4, 8, 1, 0, 6, 2, 3, 5, 7)
    assert eight_puzzle.result([1, 0, 6, 8, 7, 5, 4, 2, 3], 'DOWN') == (1, 7, 6, 8, 0, 5, 4, 2, 3)
    assert eight_puzzle.result([1, 2, 3, 4, 5, 6, 7, 8, 0], 'UP') == (1, 2, 3, 4, 5, 0, 7, 8, 6)
    assert eight_puzzle.result([4, 8, 1, 6, 0, 2, 3, 5, 7], 'RIGHT') == (4, 8, 1, 6, 2, 0, 3, 5, 7)


def test_goal_test():
    assert eight_puzzle.goal_test([0, 1, 2, 3, 4, 5, 6, 7, 8]) == False
    assert eight_puzzle.goal_test([6, 3, 5, 1, 8, 4, 2, 0, 7]) == False
    assert eight_puzzle.goal_test([3, 4, 1, 7, 6, 0, 2, 8, 5]) == False
    assert eight_puzzle.goal_test([1, 2, 3, 4, 5, 6, 7, 8, 0]) == True
    assert eight_puzzle2.goal_test([4, 8, 1, 6, 0, 2, 3, 5, 7]) == False
    assert eight_puzzle2.goal_test([3, 4, 1, 7, 6, 0, 2, 8, 5]) == False
    assert eight_puzzle2.goal_test([1, 2, 3, 4, 5, 6, 7, 8, 0]) == False
    assert eight_puzzle2.goal_test([0, 1, 2, 3, 4, 5, 6, 7, 8]) == True


def test_recursive_best_first_search():
    assert recursive_best_first_search(
        romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']


def test_hill_climbing():
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                           [-3, 7, 11, 5]])
    assert hill_climbing(prob) == (0, 3)
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    assert hill_climbing(prob) == (0, 2)
    prob = PeakFindingProblem((2, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    assert hill_climbing(prob) == (1, 3)


def test_simulated_annealing():
    random.seed("aima-python")
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]], directions4)
    sols = {prob.value(simulated_annealing(prob)) for i in range(100)}
    assert max(sols) == 20
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]], directions8)
    sols = {prob.value(simulated_annealing(prob)) for i in range(100)}
    assert max(sols) == 999


def test_BoggleFinder():
    board = list('SARTELNID')
    """
    >>> print_boggle(board)
        S  A  R
        T  E  L
        N  I  D
    """
    f = BoggleFinder(board)
    assert len(f) == 206


def test_and_or_graph_search():
    def run_plan(state, problem, plan):
        if problem.goal_test(state):
            return True
        if len(plan) is not 2:
            return False
        predicate = lambda x: run_plan(x, problem, plan[1][x])
        return all(predicate(r) for r in problem.result(state, plan[0]))
    plan = and_or_graph_search(vacumm_world)
    assert run_plan('State_1', vacumm_world, plan)


def test_LRTAStarAgent():
    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_3') == 'Right'
    assert my_agent('State_4') == 'Left'
    assert my_agent('State_3') == 'Right'
    assert my_agent('State_4') == 'Right'
    assert my_agent('State_5') is None

    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_4') == 'Left'

    my_agent = LRTAStarAgent(LRTA_problem)
    assert my_agent('State_5') is None


def test_genetic_algorithm():
    # Graph coloring
    edges = {
        'A': [0, 1],
        'B': [0, 3],
        'C': [1, 2],
        'D': [2, 3]
    }

    def fitness(c):
        return sum(c[n1] != c[n2] for (n1, n2) in edges.values())

    solution_chars = GA_GraphColoringChars(edges, fitness)
    assert solution_chars == ['R', 'G', 'R', 'G'] or solution_chars == ['G', 'R', 'G', 'R']

    solution_bools = GA_GraphColoringBools(edges, fitness)
    assert solution_bools == [True, False, True, False] or solution_bools == [False, True, False, True]

    solution_ints = GA_GraphColoringInts(edges, fitness)
    assert solution_ints == [0, 1, 0, 1] or solution_ints == [1, 0, 1, 0]

    # Queens Problem
    gene_pool = range(8)
    population = init_population(100, gene_pool, 8)

    def fitness(q):
        non_attacking = 0
        for row1 in range(len(q)):
            for row2 in range(row1+1, len(q)):
                col1 = int(q[row1])
                col2 = int(q[row2])
                row_diff = row1 - row2
                col_diff = col1 - col2

                if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                    non_attacking += 1

        return non_attacking


    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=25)
    assert fitness(solution) >= 25


def GA_GraphColoringChars(edges, fitness):
    gene_pool = ['R', 'G']
    population = init_population(8, gene_pool, 4)

    return genetic_algorithm(population, fitness, gene_pool=gene_pool)


def GA_GraphColoringBools(edges, fitness):
    gene_pool = [True, False]
    population = init_population(8, gene_pool, 4)

    return genetic_algorithm(population, fitness, gene_pool=gene_pool)


def GA_GraphColoringInts(edges, fitness):
    population = init_population(8, [0, 1], 4)

    return genetic_algorithm(population, fitness)


def test_simpleProblemSolvingAgent():
    class vacuumAgent(SimpleProblemSolvingAgentProgram):
        def update_state(self, state, percept):
            return percept

        def formulate_goal(self, state):
            goal = [state7, state8]
            return goal  

        def formulate_problem(self, state, goal):
            problem = state
            return problem   
    
        def search(self, problem):
            if problem == state1:
                seq = ["Suck", "Right", "Suck"]
            elif problem == state2:
                seq = ["Suck", "Left", "Suck"]
            elif problem == state3:
                seq = ["Right", "Suck"]
            elif problem == state4:
                seq = ["Suck"]
            elif problem == state5:
                seq = ["Suck"]
            elif problem == state6:
                seq = ["Left", "Suck"]
            return seq

    state1 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
    state2 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
    state3 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
    state4 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
    state5 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]]
    state6 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]]
    state7 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]
    state8 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]

    a = vacuumAgent(state1)

    assert a(state6) == "Left"
    assert a(state1) == "Suck"
    assert a(state3) == "Right"
    


# TODO: for .ipynb:
"""
>>> compare_graph_searchers()
    Searcher                      romania_map(A, B)        romania_map(O, N)         australia_map
    breadth_first_tree_search     <  21/  22/  59/B>   <1158/1159/3288/N>    <   7/   8/  22/WA>
    breadth_first_search          <   7/  11/  18/B>   <  19/  20/  45/N>    <   2/   6/   8/WA>
    depth_first_graph_search      <   8/   9/  20/B>   <  16/  17/  38/N>    <   4/   5/  11/WA>
    iterative_deepening_search    <  11/  33/  31/B>   < 656/1815/1812/N>    <   3/  11/  11/WA>
    depth_limited_search          <  54/  65/ 185/B>   < 387/1012/1125/N>    <  50/  54/ 200/WA>
    recursive_best_first_search   <   5/   6/  15/B>   <5887/5888/16532/N>   <  11/12/  43/WA>

>>> ' '.join(f.words())
'LID LARES DEAL LIE DIETS LIN LINT TIL TIN RATED ERAS LATEN DEAR TIE LINE INTER
STEAL LATED LAST TAR SAL DITES RALES SAE RETS TAE RAT RAS SAT IDLE TILDES LEAST
IDEAS LITE SATED TINED LEST LIT RASE RENTS TINEA EDIT EDITS NITES ALES LATE
LETS RELIT TINES LEI LAT ELINT LATI SENT TARED DINE STAR SEAR NEST LITAS TIED
SEAT SERAL RATE DINT DEL DEN SEAL TIER TIES NET SALINE DILATE EAST TIDES LINTER
NEAR LITS ELINTS DENI RASED SERA TILE NEAT DERAT IDLEST NIDE LIEN STARED LIER
LIES SETA NITS TINE DITAS ALINE SATIN TAS ASTER LEAS TSAR LAR NITE RALE LAS
REAL NITER ATE RES RATEL IDEA RET IDEAL REI RATS STALE DENT RED IDES ALIEN SET
TEL SER TEN TEA TED SALE TALE STILE ARES SEA TILDE SEN SEL ALINES SEI LASE
DINES ILEA LINES ELD TIDE RENT DIEL STELA TAEL STALED EARL LEA TILES TILER LED
ETA TALI ALE LASED TELA LET IDLER REIN ALIT ITS NIDES DIN DIE DENTS STIED LINER
LASTED RATINE ERA IDLES DIT RENTAL DINER SENTI TINEAL DEIL TEAR LITER LINTS
TEAL DIES EAR EAT ARLES SATE STARE DITS DELI DENTAL REST DITE DENTIL DINTS DITA
DIET LENT NETS NIL NIT SETAL LATS TARE ARE SATI'

>>> boggle_hill_climbing(list('ABCDEFGHI'), verbose=False)
(['E', 'P', 'R', 'D', 'O', 'A', 'G', 'S', 'T'], 123)
"""

if __name__ == '__main__':
    pytest.main()
