# # Code --- >
class Node:
   def __init__(self, dataval):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None
  # ---------------------------------------------------------
   """For quick withdrawal """
   """Для быстрого вывода """
   def printList(self):
    variable = self.headval
    while variable:
      print(variable.dataval)
      variable = variable.nextval
  # ---------------------------------------------------------
   """ Adding a node to the beginning of a list"""
   """Добавление узла в начало списка"""
   def push(self,new_dataval):
       # create a new_Node
       # создать новый_узел
       new_Node = Node(new_dataval)
       # Move the beginning of the list to the next position
       # Переместить начало списка на следующую позицию
       new_Node.nextval = self.headval
       # Put the new node at the top of the list
       # Поместите новый узел в начало списка
       self.headval = new_Node
  # ---------------------------------------------------------
   """Adding a node in the middle of our nodes in the LinkedList"""
   """Добавляем узел на середину наших узлов находяшегося в LinkedList"""
   def insertAfter(self,prev_Node,new_dataval):
    # Add node after node
    # Добавить узел после узла
    if prev_Node is None:
        print("Узел не существует")
        return
    # Add a new node
    # Добавляем новый узел
    new_Node = Node(new_dataval)
    # Connect the new node to the next node
    # Соединяем новый узел со следующим узлом
    new_Node.nextval = prev_Node.nextval
    # We connect the previous node to the new node
    # Соединяем предыдущий узел с новым узлом
    prev_Node.nextval = new_Node
  # ---------------------------------------------------------
   """Add node to end of list"""
   """Добавить узел в конец списка"""
   def append(self,new_dataval):
    # We create a new node
    # Создаем новый узел
    new_Node = Node(new_dataval)
    # Check that List is not empty
    # Проверяем, что список не пуст
    if self.headval is None:
        #If empty, the new node is the beginning of the list
        #Если пусто, новый узел является началом списка
        self.head = new_Node
        return
    # Otherwise we go to the end of the List
    # Иначе переходим в конец списка
    lastval = self.headval
    while lastval.nextval:
        lastval = lastval.nextval
    lastval.nextval = new_Node

   """Delete a value from a list"""
   """Удалить значение из списка"""
   def deleteNode(self,key):
    # # We find the beginning of the list
    # Находим начало списка
    variable = self.headval
    # Let's check the first node
    # Проверим первый узел
    if(variable and variable.dataval == key):
        self.headval = variable.nextval
        variable = None
        return
    # Otherwise, look at the next nodes
    # В противном случае посмотрите на следующие узлы
    while variable:
        if variable.dataval == key:
          break
        prev_Node = variable
        variable = variable.nextval
    # If no value is found
    # Если значение не найдено
    if variable == None:
        return
    # Delete the node from the list
    # Удалить узел из списка
    prev_Node.nextval = variable.nextval
    variable = None
