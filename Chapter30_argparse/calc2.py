"""
Example 2 for commandline-arguments
book p. 524

example call: path... calc1.py -o "minus" 7.4 9.1

Author: Oliver Zott
Version: 1.0 / 14.09.2019
"""


from argparse import ArgumentParser


# -------------------------------------------------------
# Argument Parser
parser = ArgumentParser(description="Calculator program")   # Argument Parser instance

# method to add argument or  option to program
parser.add_argument("-o", "--operation",
                    dest="operation",
                    default="plus",
                    help="Rechenoperation; default = addition")

parser.add_argument("operands", metavar="Operaaaaand",
                    type=float,
                    nargs="+",
                    help="Operanden fuer Berechnung")

parser.add_argument("-i", "--integer",
                    dest="type",
                    action="store_const",
                    const=int,
                    default=float,
                    help="Ganzzahlige Berechnung")

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
    result = args.type(args.operands[0])
    for z in args.operands[1:]:
        result = calc[op](result, args.type(z))
    print("Solution: ", result)
else:
    parser.error("{} no valid operation!".format(op))
