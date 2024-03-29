import numpy as np
from ancillary import list_recursive


def remote_1(args):

    input_list = args["input"]
    myval = np.mean([input_list[site]["output_val"] for site in input_list])

    computation_output = {"output": {"output_list": myval}, "success": True}
    return computation_output


def start(PARAM_DICT):
    PHASE_KEY = list(list_recursive(PARAM_DICT, "computation_phase"))

    if "local_1" in PHASE_KEY:
        return remote_1(PARAM_DICT)
    else:
        raise ValueError("Error occurred at Remote")
