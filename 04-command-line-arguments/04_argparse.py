"""04 argparse usage

Should be able to do the following

1. Get help with --help or -h
2. At least three arguments that are flags
3. Three arguments that are options
4. Positional arguments, a list of files at the end of all `--` style arguments
and can handle terminal wildcards like */.txt
"""
import random
import argparse

# supported arguments
# -h, --help
# --hello  print hello world
# --random  print a random integer
# --lower  lower bound of random integer to use for randint, defaults to 0
# --upper  upper bound of random integer to use for randint, defaults to 100
# --file  name of a file to print to

if __name__ == "__main__":

    parser = argparse.ArgumentParser("argparse testing!")
    parser.add_argument(
        "--hello", dest="hello", help="prints hello world", action="store_true"
    )
    parser.add_argument(
        "--random", dest="rand", help="prints random number", action="store_true"
    )
    parser.add_argument(
        "--lower",
        dest="lower",
        help="lower bound for random number",
        type=int,
        default=0,
    )
    parser.add_argument(
        "--upper",
        dest="upper",
        help="upper bound for random number",
        type=int,
        default=100,
    )
    args = parser.parse_args()

    output = ""

    if args.hello:
        output += "Hello, world!\n"

    if args.rand:
        lower = args.lower
        upper = args.upper
        output += f"Random number: {random.randint(args.lower, args.upper)}\n"

    print(output)
