arr = [5,10.15,20]
target =12

for i in range (len(arr)):
    if arr[i] == target:
        print("found at index",arr[i])
        break
else:
    print("Not Found")
