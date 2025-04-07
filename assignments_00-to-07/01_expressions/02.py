C : int = 299792458
def main():
    mass_in_kg : float = float(input("Enter kilos of mass: "))

    energy_in_joules : float = mass_in_kg * (C**2)

    # Display work to the user
    print("formula: e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print()
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == "__main__":
    main()