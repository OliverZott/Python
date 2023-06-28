"""
Simple Example for command line argument usage
    
Example:
python3 command_line_args.py --help
python3 command_line_args.py --name "Olli" --age 37 --admin True

Debugging:
see launch file: 
    - Python: Command Line Args Example"
"""

import argparse


def check_for_boolean_value(val):
    if val == "True":
        return True
    elif val == "False":
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main() -> None:
    parser = argparse.ArgumentParser(description='Check for boolean value.')
    parser.add_argument(
        '--age', help="Enter your age", type=int, required=True
    )
    parser.add_argument(
        "--name", help="Enter your name", type=str, required=True
    )
    parser.add_argument(
        "--admin",
        help="Enter true or false if admin or not",
        type=check_for_boolean_value,
        required=False,
        default=False
    )

    # this step is required to parse the arguments (read the input in console)
    # this is a special namespace/container for all the arguments
    args = parser.parse_args()

    age = args.age
    name = args.name
    is_admin = args.admin

    print(f"Age: {age}")
    print(f"Name: {name}")
    print(f"Is admin: {is_admin}")


if __name__ == '__main__':
    main()
