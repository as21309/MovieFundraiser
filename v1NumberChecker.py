# Number Checker
# Arjun Sharma
# 16/05/2024

def get_valid_number(prompt, min_value=None, max_value=None):
    """
    Prompts the user to enter a valid number based on the specified conditions.

    Args:
        prompt (str): The prompt to display to the user.
        min_value (float, optional): The minimum value allowed. If not provided, any number is accepted.
        max_value (float, optional): The maximum value allowed. If not provided, any number is accepted.

    Returns:
        float: The valid number entered by the user.

    Raises:
        ValueError: If the user enters an invalid input.
    """
    while True:
        try:
            user_input = float(input(prompt))
            if min_value is not None and user_input < min_value:
                print(f"Error: The number must be greater than or equal to {min_value}.")
            elif max_value is not None and user_input > max_value:
                print(f"Error: The number must be less than or equal to {max_value}.")
            elif min_value is not None and max_value is not None and (user_input < min_value or user_input > max_value):
                print(f"Error: The number must be between {min_value} and {max_value}.")
            else:
                return user_input
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

# Example usage
any_number = get_valid_number("Enter a number: ")
print(f"You entered: {any_number}")

print("\nEnter a number greater than or equal to 10:")
number_gte_10 = get_valid_number("Enter a number: ", min_value=10)
print(f"You entered: {number_gte_10}")

print("\nEnter a number less than or equal to 20:")
number_lte_20 = get_valid_number("Enter a number: ", max_value=20)
print(f"You entered: {number_lte_20}")

print("\nEnter a number between 5 and 15:")
number_between_5_and_15 = get_valid_number("Enter a number: ", min_value=5, max_value=15)
print(f"You entered: {number_between_5_and_15}")
