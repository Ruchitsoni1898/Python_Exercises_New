def find_maximum(numbers):
    if not numbers:
        return None  # Return None for an empty list

    max_number = numbers[0]  # Initialize max_number with the first element

    for num in numbers:
        if num > max_number:
            max_number = num  # Update max_number if a larger number is found

    return max_number

numbers = [5, 10, 3, 8, 15, 7]
max_number = find_maximum(numbers)

if max_number is not None:
    print(f"The maximum number in the list is: {max_number}")
else:
    print("The list is empty.")

