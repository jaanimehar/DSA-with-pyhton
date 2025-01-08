#reverse an array
arr=[1,2,3,4,5]
print(arr)
n=len(arr)
print(f'length:{n}')
for i in range(n//2):
    arr[i], arr[n-i-1]=arr[n-i-1], arr[i]
print(arr)           