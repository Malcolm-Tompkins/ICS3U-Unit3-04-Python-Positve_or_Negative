#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 5, 2021
# Program that displays the sign of an integer


def main():
    # Function that displays the sign of an integer

    # User input
    user_int = int(input("Input an integer: "))


# Process
    if user_int > 0:

        # Output
        print("{} is a positive number".format(user_int))

    # Process
    elif user_int < 0:

        # Output
        print("{} is a negative number".format(user_int))

    # Process
    else:

        # Output
        print("{} zero has no sign".format(user_int))


if __name__ == "__main__":
    main()
