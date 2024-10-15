"""
    Author: Dan Shaw w0190983
    Title: Auto Insurance
    Description: Computes monthly insurance according to the provided schedule.
"""

from DanMath import Validation

MALE_RATES = [(0.25 / 12), (0.17 / 12), (0.1 / 12)]
FEMALE_RATES = [(0.25 / 12), (0.15 / 12), (0.1 / 12)]

def main():
    i = input("Enter your gender (M/F).\n> ")
    i2 = input("Enter your age.\n> ")
    i3 = input("Enter the price of your vehicle\n> ")

    if i.lower() == "m":
        rates = MALE_RATES
    else:
        rates = FEMALE_RATES

    if (int(i2) >= 15) and (int(i2) < 25):
        print(int(i3) * rates[0])
    elif (int(i2) >= 25) and (int(i2) < 40):
        print(int(i3) * rates[1])
    elif (int(i2) >= 40) and (int(i2) < 70):
        print(int(i3) * rates[2])
    else:
        print("You are not within the age range to be insured.")

if __name__ == "__main__":
    main()