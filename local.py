import json
import os
import sys
from ancillary import list_recursive


def local_1(args):

    input_list = args["input"]
    myFile = input_list["covariates"]

    with open(os.path.join(args["state"]["baseDirectory"], myFile)) as fh:
        myval = fh.readlines()

    myval = list(map(int, myval))
    computation_output = {
        "output": {
            "output_val": myval,
            "computation_phase": 'local_1'
        }
    }

    return json.dumps(computation_output)


if __name__ == '__main__':

    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))

    if not phase_key:
        computation_output = local_1(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
