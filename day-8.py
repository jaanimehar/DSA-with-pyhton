def maximum_Profit():
    n=int(input("Enter number of elements: "))  # size of array
    arr=[]
    max_profit=0
    min_price=float('inf')
    for i in range(n):
        num=int(input(f"Enter element {i+1}: "))
        arr.append(num)
    print("Array is:", arr)
    
    for i in range(0, n-1):
        min_price=min(min_price, arr[i])
        profit=arr[i]-min_price
        max_profit=max(max_profit, profit)
    print("Maximum Profit:", max_profit)
maximum_Profit()