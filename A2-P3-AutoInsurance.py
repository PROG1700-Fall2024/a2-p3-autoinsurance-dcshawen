"""
    Author: Dan Shaw w0190983
    Title: Auto Insurance
    Description: Computes monthly insurance according to the provided schedule.
"""

from DanMath import Validate

MALE_RATES = [(0.25 / 12), (0.17 / 12), (0.1 / 12)]
FEMALE_RATES = [(0.25 / 12), (0.15 / 12), (0.1 / 12)]
AGE_THRESHOLDS = [15, 25, 40, 70]

def main():
    banner = "| AUTO INSURANCE CALCULATOR |"
    greeting = "Compute your monthly auto insurance rate!"

    print("-" * len(banner))
    print(banner)
    print("-" * len(banner))
    print(greeting)
    print("-" * len(banner))

    sex = getSex()
    age = getAge()
    vehiclePrice = getVehiclePrice()

    if sex == 0:
        rates = MALE_RATES
    else:
        rates = FEMALE_RATES

    if (age >= AGE_THRESHOLDS[0]) and (age < AGE_THRESHOLDS[1]):
        monthlyRate = vehiclePrice * rates[0]
    elif (age >= AGE_THRESHOLDS[1]) and (age < AGE_THRESHOLDS[2]):
        monthlyRate = vehiclePrice * rates[1]
    elif (age >= AGE_THRESHOLDS[2]) and (age < AGE_THRESHOLDS[3]):
        monthlyRate = vehiclePrice * rates[2]
    
    print("Your monthly insurance will be ${0:,.2f}".format(monthlyRate))

def getVehiclePrice():
    while (vehiclePrice := Validate.validateInt(input("Enter the price of your vehicle\n> "))) is None:
        print("You have entered an invalid vehicle price.")
    return vehiclePrice

def getAge():
    while (age := Validate.validateInt(input("Enter your age.\n> "))) is None:
        print("You have entered an invalid age.")
    if age >= 70:
        print("You do not qualify for insurance.")
        exit()

    return age

def getSex():
    sex = input("Enter your gender (M/F).\n> ")
    if sex.upper() == "M":
        return 0
    elif sex.upper() == "F":
        return 1
    else:
        getSex()

if __name__ == "__main__":
    main()