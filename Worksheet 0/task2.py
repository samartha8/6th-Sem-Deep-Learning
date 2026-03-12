def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The sum of the numbers.
    """
    return sum(numbers)


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)


def find_maximum(numbers):
    """
    Finds the maximum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The maximum number in the list.
    """
    return max(numbers)


def find_minimum(numbers):
    """
    Finds the minimum value in a list of numbers.

    Parameters:
    numbers (list): A list of numeric values.

    Returns:
    float: The minimum number in the list.
    """
    return min(numbers)


def main():
    print("===== Mathematical Operations Program =====")
    print("Choose an operation:")
    print("1. Sum")
    print("2. Average")
    print("3. Maximum")
    print("4. Minimum")

    choice = input("Enter your choice (1-4): ")

    try:
        user_input = input("Enter numbers separated by spaces: ")
        number_list = [float(num) for num in user_input.split()]

        if len(number_list) == 0:
            print("Error: The list is empty.")
            return

        if choice == '1':
            result = calculate_sum(number_list)
            print(f"Sum = {result}")
        elif choice == '2':
            result = calculate_average(number_list)
            print(f"Average = {result}")
        elif choice == '3':
            result = find_maximum(number_list)
            print(f"Maximum = {result}")
        elif choice == '4':
            result = find_minimum(number_list)
            print(f"Minimum = {result}")
        else:
            print("Error: Invalid operation selected.")

    except ValueError:
        print("Error: Please enter only numeric values separated by spaces.")


if __name__ == "__main__":
    main()