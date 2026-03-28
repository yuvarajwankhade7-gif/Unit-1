import Temperature

def main():
    while True:
        print("1. Celsius to Kelvin")
        print("2. Celsius to Fahrenheit")
        print("3. Fahrenheit to Celsius")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Kelvin:", Temperature.celsius_to_kelvin(celsius))

        elif choice == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit:", Temperature.celsius_to_fahrenheit(celsius))

        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celsius:", Temperature.fahrenheit_to_celsius(fahrenheit))

        elif choice == 4:
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()