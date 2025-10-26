def rearrange_array():
    n = int(input("Enter number of elements: "))
    
    if n <= 0:
        print("Invalid size of array")
        return
    
    arr = []
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        if num < 0:
            print("Wrong Input (negative number not allowed)")
            return
        arr.append(num)
    
    arr.sort()
    print("Array is:", arr)
    
    # Make all elements unique with minimal increments
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1

    print("Rearranged Array:", arr)
    print("Minimum Sum of array elements:", sum(arr))

rearrange_array()
