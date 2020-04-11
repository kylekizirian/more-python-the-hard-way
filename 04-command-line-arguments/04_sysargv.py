"""04 sys.argv usage

Should be able to do the following

1. Get help with --help or -h
2. At least three arguments that are flags
3. Three arguments that are options
4. Positional arguments, a list of files at the end of all `--` style arguments
and can handle terminal wildcards like */.txt
"""
import random
import sys

# supported arguments
# -h, --help
# --hello  print hello world
# --random  print a random integer
# --lower  lower bound of random integer to use for randint, defaults to 0
# --upper  upper bound of random integer to use for randint, defaults to 100
# --file  name of a file to print to

if __name__ == "__main__":
    arguments = sys.argv[1:]
    output = ""

    if "--help" in arguments or "-h" in arguments:
        help_str = (
            "Available flags:\n"
            "--hello: prints hello world\n"
            "--random: prints a random number between 0 and 10\n"
        )
        # help just goes to stdout, not to --file
        print(help_str)

    if "--hello" in arguments:
        output += "Hello, world!\n"

    if "--random" in arguments:
        try:
            arg_pos = arguments.index("--lower")
        except ValueError:
            lower = 0
        else:
            lower = int(arguments[arg_pos+1])

        try:
            arg_pos = arguments.index("--upper")
        except ValueError:
            upper = 100
        else:
            upper = int(arguments[arg_pos+1])

        output += f"Random number: {random.randint(lower, upper)}\n"

    try:
        arg_pos = arguments.index("--file")
    except ValueError:
        # --file not supplied, print to stdout
        print(output)
    else:
        # next line should be the position of file, will raise an IndexError if
        # not given
        file_name = arguments[arg_pos+1]
        with open(file_name, 'w') as f:
            f.write(output)

