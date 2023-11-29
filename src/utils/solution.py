import random
import os

# **********************************************
# ********** Regarding Solution Class **********
# **********************************************

class Solution:
    # N: int -> number of items
    # budget: int -> budget
    # weights: list -> list of each item's weight
    # values: list -> list of each item's profit
    # len(weights) and len(pofits) MUST EQuAL to N
    def __init__(self, N, budget, weights, values, fitness=0):
        self.N = N
        self.budget = budget
        self.weights = weights
        self.values = values
        self.fitness = fitness
    
    def evaluate(self):
        self.fitness = fitness(self)
    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "budget: {}\n".format(self.budget)
        out_str += "\nweights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "\nvalues ({}): {}\n".format(len(self.values), self.values)
        out_str += "\nfitness: {}\n".format(self.fitness)
        out_str += "======================\n"

        return out_str


# ***********************************************
# ********** Random Solution Generator **********
# ***********************************************

# generates one random solution
# output: Solution (N, weights, values)
def random_solution(n_max, b_max, weight_max, value_max):
    N = random.randint(1, n_max)
    budget = random.randint(1, b_max)
    weights = [random.randint(1, weight_max) for i in range(N)]
    values = [random.randint(1, value_max) for i in range(N)]
    
    sol = Solution(N, budget, weights, values)
    
    return sol


# ***************************************
# ********** DP Correct Answer **********
# ***************************************

def dp(N: int, B: int, W: list, V: list) -> int:
    if N == 0 or B == 0:
        return 0
    if (W[N-1] > B):
        return dp(N-1, B, W, V)
    else:
        return max(V[N-1] + dp(N-1,B-W[N-1], W, V), dp(N-1, B, W, V))


# ***************************************
# ********** Regarding Fitness **********
# ***************************************
    
def try_solution(solution):
    gt = dp(solution.N, solution.budget, solution.weights, solution.values)

    sample_list = os.listdir("./data/")
    sample_list = [s for s in sample_list if s.endswith(".py")]
    sample_list = [s.split("/")[-1][:-len(".py")] for s in sample_list]
    sample_list.sort()

    res_list = []
    for sample in sample_list:
        exec(f'import data.{sample} as {sample}')
        code = f"{sample}.{sample}({solution.N}, {solution.budget}, {solution.weights}, {solution.values})"

        res = eval(code)
        # print("result on {}: {}".format(sample, res))
        res_list.append(res)

    return gt, res_list

# input: solution
# output: fitness value
def fitness(solution):
    # TODO: Sumin
    gt_sol, res_list = try_solution(solution)

    # print("gt: ", gt_sol)
    # print("res: ", res_list)
    # wrong_distance = sum([(gt_sol - r) for r in res_list])

    wrong_count = sum([1 if gt_sol != r else 0 for r in res_list])
    # print("{} wrong out of {}".format(wrong_count, len(res_list)))
    final_fitness = wrong_count / len(res_list)

    return final_fitness