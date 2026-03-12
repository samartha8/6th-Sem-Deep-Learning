def get_sublist(lst, start, end):
    """
    Returns a sublist from the given list starting at index 'start'
    and ending at index 'end' (inclusive).

    Parameters:
    lst (list): The original list.
    start (int): Starting index.
    end (int): Ending index (inclusive).

    Returns:
    list: A sublist from start to end (inclusive).

    Raises:
    ValueError: If indices are invalid.
    """
    if start < 0 or end >= len(lst):
        raise ValueError("Start or end index is out of range.")
    if start > end:
        raise ValueError("Start index cannot be greater than end index.")

    return lst[start:end + 1]  # +1 because Python slicing excludes end


def main():
    print("===== Slice a Sublist Program =====")

    try:
        user_input = input("Enter elements separated by spaces: ").strip()

        if not user_input:
            print("Error: Input list cannot be empty.")
            return

        # Convert to list of numbers
        number_list = [float(num) for num in user_input.split()]

        start = int(input("Enter starting index: "))
        end = int(input("Enter ending index: "))

        result = get_sublist(number_list, start, end)

        print(f"\nOriginal List: {number_list}")
        print(f"Sublist from index {start} to {end}: {result}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()