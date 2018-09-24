import json
import numpy as np
import sys
from ancillary import list_recursive


def remote_1(args):

    input_list = args["input"]
    myval = np.mean([input_list[site]["output_val"] for site in input_list])

    computation_output = {"output": {"output_list": myval}, "success": True}
    return json.dumps(computation_output)


if __name__ == '__main__':

    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))

    if "local_1" in phase_key:
        computation_output = remote_1(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Remote")
