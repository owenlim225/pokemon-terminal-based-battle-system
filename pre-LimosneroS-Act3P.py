# Limosnero, Sherwin P.
# J2S
# Activity #3 P

import os

transpo = {
    "Jeepney": {
        "Regular": 12.00,
        "Student": 10.00,
        "Senior": 09.50
    },

    "Tricycle": {
        "Regular" : 50.00,
        "Student" : 40.00,
        "Senior": 38.00
    },

    "Bus": {
        "Regular": 12.00,
        "Student": 10.00,
        "Senior": 9.50
        }
}


def main():
    print ("Transportation Cost Dictionary")

    while True:
        print("\nTransportation:\n")
        PUV = input("\n > Jeepney\n > Tricycle\n > Bus\n\n").strip().capitalize()

        if PUV not in transpo:
            os.system('cls') # clean terminal
            print("Invalid. Please choose one of the options below.")
            continue

        else:
            break

    while True:
        print("\nCost:\n")
        passenger = input("\n > Regular\n > Student\n > Bus\n").strip().capitalize()

        if passenger not in transpo[PUV]:
            os.system('cls') # clean terminal
            print("Invalid. Please choose one of the options below.")
            continue
        else:
            break

    os.system('cls') # clean terminal
    print(f"₱{transpo[PUV][passenger]:.2f} for {PUV} -> {passenger} ")


if __name__ == "__main__":
    os.system('cls') # clean terminal
    main()