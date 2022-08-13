# 1.Linear Search(code):
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print("element found at index "+str(linearsearch(arr,x)))

# 1.Binary Search(code):
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 3
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# Big-O(en):
# Big-O notation is a metric used to determine the complexity of an algorithm. 
# Basically, Big-O notation means the relationship between the inputs of an algorithm and the steps required to execute the algorithm.

#  Big-O(ru):
# Нотация Big-O-это метрика, используемая для определения сложности алгоритма. 
# В принципе, обозначение Big-O означает связь между входными данными алгоритма и шагами, необходимыми для выполнения алгоритма.

# Big-O:
# 1.For Linear search: O(n)
# 2.For Binary search: O(log2N)