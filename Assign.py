#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This calculates asks for the size o your burger, if you want fries and drinks, and calculates the total

import sys, time  # allows for the typing effect and delay to how many characters per second
import math
import colorama  # alloys for text to be colorized, install colorama (pip3 install colorama)
from colorama import init


def main():
    # Caution note
    print(colorama.Fore.RED + "CAUTION!!!!")
    print("THE PROGRAM ONLY ACCEPTS PROVIDED NUMBERS or Y/N INPUTS FROM USER")
    print("ANYTHING ELSE WILL END THE PROGRAM AND WILL REQUIRE A RESTART ")
    print(colorama.Fore.RESET + "You have been warned")
    time.sleep(2)

    # Greeting
    print()
    print("Hello and welcome to Wacdonalds, the best fastfood place to eat.")
    print("Here is the provided menu.")

    print(
        "-----------------------------------------------------------------------------------------------------------------"
    )
    print(
        "1. Simple beef burger order ------ $12.00\n"
        "2. THE MINECRAFT combo order -----  SOULD OUT  "
    )
    print(
        "-----------------------------------------------------------------------------------------------------------------\n"
    )

    # User choice in int
    print("May I have your order?")
    order_choice_as_str = input("> ")

    try:

        # Converts order_choice_as_str into an integer
        order_choice_as_int = int(order_choice_as_str)

        # Checks if the user_input was the one of the desired input
        if order_choice_as_int < 1 or order_choice_as_int > 2:
            print("\nThis input was not part of the program please restart")
            sys.exit()

        # First choice
        elif order_choice_as_int == 1:
            price_choice_1 = 12.00

            # Asks the user for the size of the burger
            print(
                "\nWhat size would like your beef burger to be:\n",
                "1. Large\n",
                "2. Small",
            )
            size_choice1_str = input("> ")

            # Nested Try Catch
            try:

                # Converts size_choice1_str into an integer
                size_choice1_int = int(size_choice1_str)

                # Checks if the user input was the desired input using or gate
                if size_choice1_int < 1 or size_choice1_int > 2:
                    print("\nThis input was not part of the program please restart")
                    sys.exit()
                else:

                    # Asks if they want fries and soda. If yes adds more money to the original price
                    print("\nWould you like fries with that (y/n)? ")
                    fries_choice_1 = input("> ")

                    if (
                        fries_choice_1 == "y"
                        or fries_choice_1 == "Y"
                        or fries_choice_1 == "Yes"
                        or fries_choice_1 == "yes"
                    ):
                        price_choice_1 = price_choice_1 + 2.29
                        print("")
                    elif (
                        fries_choice_1 == "n"
                        or fries_choice_1 == "N"
                        or fries_choice_1 == "no"
                        or fries_choice_1 == "NO"
                    ):
                        print("")
                    else:
                        print("Invalid input")
                        sys.exit()

                    print("Would you like beverage with you meal (y/n)?")
                    soda_choice1 = input("> ")

                    if (
                        soda_choice1 == "y"
                        or soda_choice1 == "Y"
                        or soda_choice1 == "yes"
                        or soda_choice1 == "Yes"
                    ):
                        price_choice_1 = price_choice_1 + 3.89
                        print("")
                    elif (
                        soda_choice1 == "n"
                        or soda_choice1 == "N"
                        or soda_choice1 == "no"
                        or soda_choice1 == "NO"
                    ):
                        print("")
                    else:
                        print("Invalid input")
                        sys.exit()

                    # Calculates the tax and total of the meal.
                    subtotal = price_choice_1
                    tax = subtotal * 0.13
                    total = subtotal + tax
                    print("Your total rounds up to $ {:.2f}".format(total))

            # Catches any error when trying to convert size_choice1_str into an integer
            except ValueError:
                print("This input was not part of the program please restart")
                sys.exit()

        # second choice
        elif order_choice_as_int == 2:
            print("My apologies but the MINECRAFT combo is sould out. ")
            print("Please try again later\n")

    # Catches any error when trying to convert order_choice_as_str into an integer
    except Exception:
        print("This input was not part of the program please restart")
        sys.exit()

    finally:
        print("")
        print("Thanks for playing\n")


if __name__ == "__main__":
    main()
