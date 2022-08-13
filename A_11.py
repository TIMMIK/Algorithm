# Buble Sort(en):
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 

# Buble Sort(en):
# Пузырьковая сортировка — это простейший алгоритм сортировки, который многократно меняет местами соседние элементы, если они расположены в неправильном порядке.

# Code --- >

def bubbleSort(array:list) -> list :
    for i in range(len(array)):
       for j in range(len(array) - i - 1):
          if array[j] > array[j + 1]:
             array[j], array[j + 1] = array[j + 1], array[j]
          print(array)
if  __name__ =='__main__':
    array=[5,2,3,8,0,4,6,7,1]
    print(array)
    bubbleSort(array)
    print(array)