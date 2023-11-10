import random

BUDGET_FIXED = 150
N_RANGE = 30
WEIGHT_RANGE = 20

class Solution:
    # N: int -> number of item choices
    # weights: list -> list of each item's weight
    # profits: list -> list of each item's profit
    # len(weights) and len(pofits) MUST EQuAL to N
    def __init__(self, N, weights, profits):
        self.N = N
        self.weights = weights
        self.profits = profits
        self.fitness = 0
    
    def evaluate(self):
        self.fitness = fitness(self.N, self.items)
    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "weights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "profits ({}): {}\n".format(len(self.profits), self.profits)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "======================"

        return out_str

# generates one random solution
# output: Solution (N, weights, profits)
def random_solution():
    N = random.randint(1, N_RANGE)
    weights = [random.randint(1, WEIGHT_RANGE) for i in range(N)]

    profits = []
    x = [random.random() for i in range(N)]
    for i in range(N):
        profits.append(int(weights[i]*(x[i]*3+0.5)))
    
    sol = Solution(N, weights, profits)
    
    return sol

# input: solution
# output: fitness value
def fitness(solution: Solution):
    # TODO: Sumin
    True

def select(k, population):
    True

def crossover(rate: float, s1: Solution, s2: Solution):
    # TODO: Heechan
    True

def mutate(rate: float, s: Solution):
    # TODO: Heechan
    True

def ga():
    True


if __name__ == "__main__":
    sol = random_solution()
    print(sol)