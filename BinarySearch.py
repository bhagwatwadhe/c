..
def BinarySearch (array, l, r, key):
    if r >= l:
        mid =int(l + (r - l)/2)
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return BinarySearch(array, l, mid-1, key)
        else:
            return BinarySearch(array, mid+1, r, key)
    else:
        return -1

arraySize = input("Enter array size ")
array = []
for i in range(0,int(arraySize)):
    array.append(input("Enter array element "))

print("Sorting the array")
array.sort()
print("Sorted Array is")
print(array)
key = input("Enter key to be Searched ")

# Function call
result = BinarySearch(array, 0, len(array)-1, key)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")