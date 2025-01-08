def find_second_largest(arr):
    if len(arr) < 2:
        return -1

    # Initialize the largest and second largest elements
    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            # Update both largest and second largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest only
            second_largest = num

    return second_largest if second_largest != float('-inf') else -1

# Input from user
try:
    user_input = input("Enter positive integers separated by spaces: ")
    array = list(map(int, user_input.split()))

    # Ensure all numbers are positive
    if all(num > 0 for num in array):
        result = find_second_largest(array)
        print("Second largest element is:", result)
    else:
        print("Please enter only positive integers.")
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
