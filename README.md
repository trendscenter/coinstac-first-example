# coinstac_first_example
COINSTAC Example for Beginners

## Summary of the Computation
In this current repo, we will demonstrate a simple example of finding the average of three (i.e., we are assuming three local sites) scalars. At each site, the scalar is read from a file which are then sent to the remote/aggregator where the average is computed and displayed.

**Note:** The use case of reading scalars from a file has been chosen to demonstrate 'reading from files', an important aspect of most computations that are written to be run on the COINSTAC architecture.

## Requirements
  - Latest version of [node.js](https://nodejs.org/en/download/)
    - Test 1: ```npm -v ```
    - Test 2: ```node -v ```
  - Latest version of [docker](https://docs.docker.com/install/)
    - Test: ```docker --version```
  - Latest version of [coinstac-simulator](https://npm.org/packages/coinstac-simulator)
    - Installation: ```sudo npm i -g coinstac-simulator```
    - Test: ```coinstac-simulator --version```

**Caveats:** (Installation on Linux Distributions)

## Getting Started
To successfully run computation in the simulator we need to
- [Create a dockerfile](#Creating-a-dockerfile)
- [Create a compsec](#Creating-a-compsec)
- [Create an inputspec](#Creating-an-inputspec)
- [Create scripts](#Writing-computation-scripts)

### Creating the Docker file (_Dockerfile_)
To run your computation in COINSTAC you'll need to encapsulate it in a docker image, for now we have one base python 3.6 image that all computations must inherit from. The Docker file use that image as a base, puts your code into `/computation`, and does any install required by your code.

**Note**: please ignore any test or extraneous files using a `.dockerignore`, this keeps image size down
```sh
FROM coinstac/coinstac-base-python-stream
# Set the working directory
WORKDIR /computation
# Copy the current directory contents into the container
COPY requirements.txt /computation
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# Copy the current directory contents into the container
COPY . /computation
```
**Explanation of Dockerfile Contents:**
- ```FROM coinstac/coinstac-base-python-stream```
  - This is the base image upon which the current computation image will be built
- ```WORKDIR /computation```
  - This is the working directory from where your computation scripts are called.
  -  Later you will notice in the `compspec.json` couple of lines `python /computation/local.py` and `python /computation/remote.py`.
- **need to explain the other lines in the code but have to test something before I do that**

### Creating the Input Specification (_inputspec.json_)

The contents of the `inputspec.json` for the current computation (with 3 local sites) is as follows:

```
[{"covariates":{"value":"value0.txt"}},
{"covariates":{"value":"value1.txt"}},
{"covariates":{"value":"value2.txt"}}]
```

Note that it's an array of size 3 (corresponding to 3 local sites). Consider the line

```
{"covariates":{"value":"value0.txt"}}
```

which is basically parsed at the local site. This line indicates to the `local.py` script the file `value0.txt` from which the scalar is read.

Notice the use of “value”, that’s the way it is according to the simulator (need to write this better).

### Creating the Computation Specification (_compspec.json_)

More on this here at [https://github.com/MRN-Code/coinstac/blob/master/algorithm-development/computation-specification-api.md](https://github.com/MRN-Code/coinstac/blob/master/algorithm-development/computation-specification-api.md)
