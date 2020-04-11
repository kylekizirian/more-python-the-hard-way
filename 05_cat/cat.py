#!/usr/bin/env python3
"""
 -b      Number the non-blank output lines, starting at 1.

 -n      Number the output lines, starting at 1.

 -s      Squeeze multiple adjacent empty lines, causing the output to be
 single spaced.


Note: seems that if -b and -n flag supplied then -b behavior is used
"""
import argparse


def number_line(
    line: str, count: int, number: bool = False, number_non_blank: bool = False
):
    if number_non_blank:
        if line.strip():
            line = str(count).rjust(6) + "  " + line

    elif number:
        line = str(count).rjust(6) + "  " + line

    return line


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="files to concatenate together")

    parser.add_argument("files", help="files to concatenate together", nargs="+")

    parser.add_argument(
        "-n",
        dest="number",
        help="Number output lines, starting at 1",
        action="store_true",
    )

    parser.add_argument(
        "-b",
        dest="number_non_blank",
        help="Number the non-blank output lines, starting at 1",
        action="store_true",
    )

    args = parser.parse_args()

    for file_ in args.files:
        with open(file_) as f:
            count = 1
            for line in f.readlines():
                line = number_line(
                    line,
                    count,
                    number=args.number,
                    number_non_blank=args.number_non_blank,
                )
                count += 1

                print(line, end="")
