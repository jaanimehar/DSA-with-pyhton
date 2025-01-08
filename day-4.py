arr=[1,2,3,4,5,6]
n=len(arr)
d=2
print(arr)
for i in range(d):
    k=0
    temp=arr[k]

    for j in range(n-1):
        arr[j]=arr[j+1]
    arr[n-1]=temp
print(arr)    