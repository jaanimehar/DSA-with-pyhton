#moves all jeros in right side of an array.
arr= [1,2,0,5,0,7]
print(arr)
j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
        
print(arr)    
