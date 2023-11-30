from utils import ga
import sys

N_MAX = 100
B_MAX = 100000
WEIGHT_MAX = 100000
VALUE_MAX = 10000

# **************************
# ********** MAIN **********
# **************************

if __name__ == "__main__":
    best_sol = ga.ga(
        experiment_name='hyunsun_01',
        end_criterion=0.95,
        tc_size=10, # greater than 2
        gen_limit=sys.maxsize,
        selection=2, # less than tc_size
        cross_rate=1.0,
        cross_at_invalid_rate=0.0,
        mutate_rate=1.0,
        mutate_type_rate=0.2,
        mutate_at_invalid_rate=0.5,
        n_max=N_MAX,
        b_max=B_MAX,
        weight_max=WEIGHT_MAX,
        value_max=VALUE_MAX,
        method = 4 # 1(random), 2(budget proportion), 3(norm CP select), 4(apply both)
    )

