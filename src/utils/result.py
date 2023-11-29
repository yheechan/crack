from pathlib import Path
import os
import json

def get_exp_dir(exp_name):
    # record population individuals per generation
    script_file_path = Path(os.path.realpath(__file__))
    src_path = script_file_path.parent.parent

    # make result directory
    result_dir = src_path / "result"
    if not result_dir.exists():
        result_dir.mkdir()

    # make specific experiment directory
    experiment_dir = result_dir / exp_name
    if not experiment_dir.exists():
        experiment_dir.mkdir()
    
    return experiment_dir

def record_individuals(exp_name, test_suite, gen, tot_gen):
    exp_dir = get_exp_dir(exp_name)

    json_dir = exp_dir / "individuals_json"
    if not json_dir.exists():
        json_dir.mkdir()

    txt_dir = exp_dir / "individuals_txt"
    if not txt_dir.exists():
        txt_dir.mkdir()

    # record current generation's individuals
    json_file = json_dir / "gen_{}_{}.json".format(gen, tot_gen)
    txt_file = txt_dir / "gen_{}_{}.txt".format(gen, tot_gen)
    with open(json_file, "w") as json_fp, open(txt_file, "w") as txt_fp:
        ind_dict = {}
        for i in range(test_suite.tc_num):
            tc_name = "tc_{}_{}".format(i+1, test_suite.tc_num)
            ind_dict[tc_name] = {}

            ind_dict[tc_name]["N"] = test_suite.tc_list[i].N
            ind_dict[tc_name]["budget"] = test_suite.tc_list[i].budget
            ind_dict[tc_name]["weights"] = test_suite.tc_list[i].weights
            ind_dict[tc_name]["values"] = test_suite.tc_list[i].values
            ind_dict[tc_name]["fitness"] = test_suite.tc_list[i].fitness
            ind_dict[tc_name]["ratio"] = test_suite.tc_list[i].ratio
            
            txt_fp.write(test_suite.tc_list[i].__str__())
            txt_fp.write("\n")
        
        json_object = json.dumps(ind_dict, indent=4)
        json_fp.write(json_object)


        print(">> wrote individuals from generation {}".format(gen))
    
    # record current generations test_suite
    json_file = exp_dir / "test_suite_evolution.json"
    txt_file = exp_dir / "test_suite_evolution.txt"
    with open(json_file, "a") as json_fp, open(txt_file, "a") as txt_fp:
        ts_json = {}
        ts_name = "ts_{}_{}".format(gen, tot_gen)

        ts_json[ts_name] = {}
        ts_json[ts_name]["generation"] = gen
        ts_json[ts_name]["tc_num"] = test_suite.tc_num
        ts_json[ts_name]["data_num"] = test_suite.data_num
        ts_json[ts_name]["state"] = test_suite.state
        ts_json[ts_name]["fitness"] = test_suite.fitness

        json_object = json.dumps(ts_json)
        json_fp.write(json_object)
        json_fp.write("\n")

        txt_fp.write(test_suite.__str__())
        txt_fp.write("\n")

        print(">> wrote test suite from generation {}".format(gen))
        ts_print = json.dumps(ts_json, indent=4)
        print(test_suite)

def record_parameter(exp_param):
    exp_dir = get_exp_dir(exp_param["experiment_name"])

    # record exp_param
    param_file = exp_dir / "parameters.json"
    with open(param_file, "w") as fp:
        json_object = json.dumps(exp_param, indent=4)
        fp.write(json_object)
    
        print(">> wrote parameters for experiment: {}".format(exp_param["experiment_name"]))
        print(json_object)