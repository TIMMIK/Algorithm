# EN --- > 
# Algorithm:
# An algorithm is a process or set of rules that must be followed in calculations 
# or other problem-solving operations, especially by a computer.

# Time and space complexity:
# Time complexity is the time taken by the algorithm to execute each set of instructions. It is always better to select the most efficient algorithm when a simple problem can solve with different methods.
# Space complexity is usually referred to as the amount of memory consumed by the algorithm.

# 1) Stack:
# A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
# In stack, a new element is added at one end and an element is removed from that end only.
# The insert and delete operations are often called push and pop.

# Code --- >

stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

# 2) Queue:
# Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. 
# With a queue the least recently added item is removed first. 
# A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

# Code --- >

# Python program to 
# demonstrate queue implementation
# using list
  
# Initializing a queue
queue = []
  
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)

# 3) Graph:
# A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links.
# The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

# Code --- >

# Create the dictionary with graph elements
graph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
# Print the graph 		 
print(graph)

# 4) Tree:
# A Tree is a Data structure in which data items are connected using references in a hierarchical manner. 
# Each Tree consists of a root node from which we can access each element of the tree.

# Code --- >

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
print(root)

# 5) Hash:
# Hash method in Python is a module that is used to return the hash value of an object. 
# In programming, the hash method is used to return integer values that are used to compare dictionary keys using a dictionary look up feature.

# Code --- >

# Declare a dictionary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print (dict['Name'] , dict['Name'])
print (dict['Age'] , dict['Age'])

# 6) Heap:
# Heap is a special tree structure in which each parent node is less than or equal to its child node. 
# Then it is called a Min Heap. 
# If each parent node is greater than or equal to its child node then it is called a max heap.

# Code --- >

import heapq

H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,8)
print(H)

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

# RU --- > 
# Алгоритм:
# Алгоритм процесс или набор правил, которым необходимо следовать при вычислениях 
# или других операциях по решению задач, особенно с помощью компьютера.

# Сложность времени и пространства:
# Временная сложность — это время, необходимое алгоритму для выполнения каждого набора инструкций. Всегда лучше выбрать наиболее эффективный алгоритм, когда простую задачу можно решить разными методами. 
# Под пространственной сложностью обычно понимают объем памяти, потребляемый алгоритмом.

# 1) Stack - Куча:
# Стек — это линейная структура данных, в которой элементы хранятся в порядке «последний пришел — первый вышел» (LIFO) или «первый пришел — вышел последним» (FILO).
# В стеке новый элемент добавляется с одного конца, а элемент удаляется только с этого конца.
# Операции вставки и удаления часто называют push и pop.

# Код --- >
stack = []
 
# функция append() для отправки
# элемент в стеке
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Начальный стек')
print(stack)
 
# функция pop() для всплывающего окна
# элемент из стека в
# заказ ЛИФО
print('\nЭлементы выскочили из стека:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nСтек после извлечения элементов:')
print(stack)

# 2) Queue - Очередь:
# Как и стек, очередь представляет собой линейную структуру данных, в которой элементы хранятся в порядке поступления (FIFO).
# В очереди наименее добавленный элемент удаляется первым. 
# Хорошим примером очереди является любая очередь потребителей ресурса, в которой потребитель, пришедший первым, обслуживается первым.
 
# Код --- >

# Программа Python для
# продемонстрируем реализацию очереди
# использование списка

# Инициализация очереди
queue = []
  
# Добавление элементов в очередь
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Начальная очередь")
print(queue)
  
# Удаление элементов из очереди
print("\nЭлементы удалены из очереди")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nОчередь после удаления элементов")
print(queue)
 
# 3) Graph - Граф: 
# Граф — это графическое представление набора объектов, где некоторые пары объектов связаны ссылками. 
# Взаимосвязанные объекты представлены точками, называемыми вершинами, а связи, соединяющие вершины, называются ребрами.

# Код --- >

# Создаем словарь с элементами графа
graph = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
# Распечатать график
print(graph)

# 4) Дерево - Tree:
# Дерево — это структура данных, в которой элементы данных связаны с помощью ссылок иерархическим образом. 
# Каждое дерево состоит из корневого узла, из которого мы можем получить доступ к каждому элементу дерева.

# Код --- >

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
print(root)

# 5) Hash - Хеш:
# Метод хеширования в Python — это модуль, который используется для возврата хеш-значения объекта. 
# В программировании метод хеширования используется для возврата целочисленных значений, которые используются для сравнения ключей словаря с использованием функции поиска в словаре.

# Код --- >

# Объявить словарь
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Доступ к словарю по его ключу
print (dict['Name'] , dict['Name'])
print (dict['Age'] , dict['Age'])

# 6) Heap - Куча:
# Куча — это особая древовидная структура, в которой каждый родительский узел меньше или равен своему дочернему узлу. 
# Тогда это называется Min Heap. 
# Если каждый родительский узел больше или равен своему дочернему узлу, то он называется Max Heap.

# Код --- >

import heapq

H = [21,1,45,78,3,5]
# Скрыть до кучи
heapq.heapify(H)
print(H)

# Добавить элемент
heapq.heappush(H,8)
print(H)