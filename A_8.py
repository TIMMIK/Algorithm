# Stack(en):
# A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
# In stack, a new element is added at one end and an element is removed from that end only.
# The insert and delete operations are often called push and pop.

# Stack(ru):
# Стек — это линейная структура данных, в которой элементы хранятся в порядке «последний пришел — первый вышел» (LIFO) или «первый пришел — вышел последним» (FILO).
# В стеке новый элемент добавляется с одного конца, а элемент удаляется только с этого конца.
# Операции вставки и удаления часто называют push и pop.

# LIFO(en):
# A stack follows the LIFO (Last In First Out) principle, i.e., the element inserted at the last is the first element to come out

# LIFO(ru):
# Стек следует принципу LIFO (Last In First Out), т. е. элемент, вставленный последним, выходит первым.

# Stack always works with(en):
# push - add element
# pop - item extraction
# isEmpty - check if the collection is empty 
# isFull - check if the collection is full
# peek - see the value of the first element

# стек всегда работает с(ru):
# push - добавить элемент
# pop - извлечение предмета
# isEmpty - проверить, пуста ли коллекция
# isFull - проверить, заполнена ли коллекция
# peek - посмотреть значение первого элемента

# Code --- >

class Stack:
   def __init__(self):
      self.stack = []

   def add(self, dataval):
      # Use list append method to add element
      # Используйте метод добавления списка для добавления элемента
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
   # Use peek to look at the top of the stack
   # Используйте просмотр, чтобы посмотреть на вершину стека
   def peek(self):     
	   return self.stack[-1]

   # Use list pop method to remove element
   # Использовать метод всплывающего списка для удаления элемента
   def remove(self):
      if len(self.stack) <= 0:
         return ("No element in the Stack")
      else:
         return self.stack.pop()

stack = Stack()
stack.add("Monday")
stack.add("Tuesday")
stack.add("Friday")
stack.add("Wednesday")
# peek - посмотреть значение первого элемента
print(stack.peek()) # Output: Wednesday
# Delete items
# Удалить элементы
print(stack.remove())
print(stack.remove())
print(stack.remove())
print(stack.remove())
print(stack.remove())