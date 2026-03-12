def extract_every_other(lst):
    """
    Extracts every other element from a list starting from the first element.

    Parameters:
    lst (list): A list of elements.

    Returns:
    list: A new list containing every other element from the original list.
    """
    return lst[::2]


def main():
    print("===== Extract Every Other Element Program =====")

    try:
        user_input = input("Enter elements separated by spaces: ").strip()

        if not user_input:
            print("Error: Input list cannot be empty.")
            return

        # Convert input to list of numbers
        number_list = [float(num) for num in user_input.split()]

        result = extract_every_other(number_list)

        print(f"Original List: {number_list}")
        print(f"Every Other Element: {result}")

    except ValueError:
        print("Error: Please enter only numeric values separated by spaces.")


if __name__ == "__main__":
    main()