from utils import ga
import sys

N_MAX = 50
B_MAX = 50000
WEIGHT_MAX = 50000
VALUE_MAX = 5000

# **************************
# ********** MAIN **********
# **************************

if __name__ == "__main__":
    best_sol = ga.ga(
        experiment_name='example',
        end_criterion=1.0,
        tc_size=5, # greater than 2
        gen_limit=3,
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
        method = 3 # 1(random), 2(budget proportion), 3(norm CP select), 4(apply both)
    )

