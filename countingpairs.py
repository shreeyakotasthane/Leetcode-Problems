def getPairsCount(arr, k): 
      
    count = 0 # Initialize result 
    map = {}
    for i in range(len(arr)):
        if arr[i] not in map:
            map[arr[i]] = True

    for i in range(len(arr)):
        if (arr[i] + k) in map:
            count +=1
        if (arr[i] - k) in map:
            count +=1
        del map[arr[i]]      
    return count 

arr = [8, 12, 16, 4, 0, 20]
k = 4
print(getPairsCount(arr,k))
