"""
Example 1 for commandline-arguments
book p. 520

example call: path... calc1.py -o "minus" 7.4 9.1

Author: Oliver Zott
Version: 1.0 / 14.09.2019
"""


from argparse import ArgumentParser


# -------------------------------------------------------
# Argument Parser
parser = ArgumentParser()   # Argument Parser instance

# method to add argument or  option to program
parser.add_argument("-o", "--operation",
                    dest="operation",
                    default="plus")

parser.add_argument("op1", type=float)
parser.add_argument("op2", type=float)

# Method which reads cmd-line arguments and executes
args = parser.parse_args()


# -------------------------------------------------------
# dictionary for calculator operations
calc = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "mal": lambda a, b: a * b,
    "geteilt": lambda a, b: a / b
}


# -------------------------------------------------------
# Access to options (operations) via pars_args instance "args"
op = args.operation
if op in calc:
    print("Solution: ", calc[op](args.op1, args.op2))
else:
    parser.error("{} no valid operation!".format(op))
