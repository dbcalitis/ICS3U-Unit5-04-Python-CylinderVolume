#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # This function calculates the volume of a cylinder
    volume = round(math.pi * radius ** 2 * height, 1)
    return volume


def main():
    # This function is the main function
    print("This program calculates the volume of a cylinder.")
    print("Please enter the radius and height.\n")

    # input
    radius_input = input("The radius is (mm): ")
    height_input = input("The height is (mm): ")

    # process
    try:
        radius_input = float(radius_input)
        height_input = float(height_input)

        volume = calculate_volume(radius_input, height_input)

        print(
            "\nThe volume of a cylinder with radius of {0} mm and height of {1} mm is {2} mm³.".format(
                radius_input, height_input, volume
            )
        )
    except (Exception):
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
