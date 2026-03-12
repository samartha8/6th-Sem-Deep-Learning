def convert_units(conversion_type, value):
    """
    Converts units based on the selected conversion type.

    Parameters:
    conversion_type (str): The type of conversion to perform.
    value (float): The numeric value to convert.

    Returns:
    tuple: (converted_value, from_unit, to_unit)
    """

    if conversion_type == '1':  # Meters to Feet
        return value * 3.28084, "m", "ft"
    elif conversion_type == '2':  # Feet to Meters
        return value / 3.28084, "ft", "m"
    elif conversion_type == '3':  # Kilograms to Pounds
        return value * 2.20462, "kg", "lbs"
    elif conversion_type == '4':  # Pounds to Kilograms
        return value / 2.20462, "lbs", "kg"
    elif conversion_type == '5':  # Liters to Gallons
        return value * 0.264172, "L", "gal"
    elif conversion_type == '6':  # Gallons to Liters
        return value / 0.264172, "gal", "L"
    else:
        return None


def main():
    print("===== Unit Conversion Program =====")
    print("Select Conversion Type:")
    print("\nLength:")
    print("  1. Meters (m) → Feet (ft)")
    print("  2. Feet (ft) → Meters (m)")
    print("\nWeight:")
    print("  3. Kilograms (kg) → Pounds (lbs)")
    print("  4. Pounds (lbs) → Kilograms (kg)")
    print("\nVolume:")
    print("  5. Liters (L) → Gallons (gal)")
    print("  6. Gallons (gal) → Liters (L)")

    conversion_type = input("\nEnter your choice (1-6): ")

    try:
        value = float(input("Enter the value to convert: "))
        result = convert_units(conversion_type, value)

        if result is not None:
            converted_value, from_unit, to_unit = result
            print(f"\n{value:.4f} {from_unit} = {converted_value:.4f} {to_unit}")
        else:
            print("Error: Unsupported conversion type selected.")

    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()