# Search Algorithms in Python:
# 1. - Linear Search.
# 2. - Binary Search.
# 3. - Membership Operators.
# 4. - Jump Search.
# 5. - Fibonacci Search.
# 6. - Exponential Search.
# 7. - Interpolation Search.

# 1. - Linear Search(en):
# Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. 
# It is the simplest searching algorithm.

# 1. Linear Search(ru):
#  Linear Search— это алгоритм последовательного поиска, в котором мы начинаем с одного конца и проверяем каждый элемент списка, пока не будет найден нужный элемент.
# Это простейший алгоритм поиска.

# Code --- >
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print("element found at index "+str(linearsearch(arr,x)))

# 2. - Binary Search(en):
# In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

# 2. - Binary Search(ru):
# В двух словах, этот алгоритм поиска использует набор элементов, который уже отсортирован, игнорируя половину элементов после всего лишь одного сравнения.

# !!!: Чтобы работал Бинарный поиск элементы должны быть сортированными, если элементы несортированные то Бинарный поиск не работает

# Logorithm(en) - Логарифм(ru):
# log2 = (n) ---> n//2
# Ex:log2 = 4 --- > 4//2 = 2

# Code --- >

# Returns index of x in arr if present, else -1(en)
# Возвращает индекс x в arr, если он присутствует, иначе -1(ru)
# 1) way:
def binary_search(arr, low, high, x):
 
    # Check base case(en)
    # Проверить базовый случай(ru)
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself(en)
        # Если элемент присутствует в самой середине(ru)
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only be present in left subarray(en)
        # Если элемент меньше середины, то он может присутствовать только в левом подмассиве(ru)
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray(en)
        # В противном случае элемент может присутствовать только в правом подмассиве        
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        # Элемент отсутствует в массиве
        return -1
 
# Test array
# Тестовый массив
arr = [ 2, 3, 4, 10, 40 ] # arr = 4
x = 10 # x - 3 element in list
 
# Function call
# Вызов функции
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# 2) way:
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        # If x is greater, ignore left half
        # Если x больше, игнорируем левую половину
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        # Если x меньше, игнорируем правую половину
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        # означает, что x присутствует в середине
        else:
            return mid
    # If we reach here, then the element was not present
    # Если мы дойдем до этого места, то элемент отсутствует
    return -1
 
# Test array
# Тестовый массив
arr = [ 2, 3, 4, 10, 40 ]
x = 3
# Function call
# Вызов функции
result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")