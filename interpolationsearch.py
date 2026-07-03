def interpolationSearch(arr, key):
    low =0 
    high = len(arr) -1
    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            else:
                return -1
        pos = low+((key - arr[low])* (high-low)// (arr[high]-arr[low]))
        
        if arr[pos] == key:
            return pos
        elif arr[pos]<key:
            low = pos+1
        else:
            high = pos -1
    return -1

numlist = [1,2,4,6,7,8,11,24,56,58,61,63,65,67,82]
key = int(input("element to search in array:"))
if(interpolationSearch(numlist,key) != -1):
    print(f'Element {key} found in the array')
else:
    print("element not found")