def get_integer_input():

    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):

    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

def main():

    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if _name_ == "_main_":
    main()
