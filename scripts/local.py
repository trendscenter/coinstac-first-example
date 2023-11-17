import os

from ancillary import list_recursive


def local_1(args):
    """local_1
    args is the COINSTAC argument dictionary
    """
    input_list = args["input"]
    myFile = input_list["covariates"]

    with open(os.path.join(args["state"]["baseDirectory"], myFile)) as fh:
        myval = fh.readlines()

    myval = list(map(int, myval))
    computation_output = {
            "output": {"output_val": myval, "computation_phase": 'local_1'}
    }

    return computation_output


def start(PARAM_DICT):
    """start
    entry point and control flow for remote computations
    """
    PHASE_KEY = list(list_recursive(PARAM_DICT, "computation_phase"))

    if not PHASE_KEY:
        return local_1(PARAM_DICT)
    else:
        raise ValueError("Error occurred at Local")
