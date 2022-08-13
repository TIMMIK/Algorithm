from A_5 import Node, LinkedList
# Create LinkedList
# Создаём  LinkedList
link_list = LinkedList()
# We make three Nodes(tugun)
# Делаем три узла (тугун)
link_list.headval = Node("Monday")
tuesday = Node("Tuesday")
wednesday = Node("Wednesday")
# Связать первый узел со вторым узлом
# Link first Node to second node
link_list.headval.nextval = tuesday
# Link second Node to third node
# Связать второй узел с третьим узлом
tuesday.nextval = wednesday
# display the next link
# показать следующую ссылку
print(link_list.headval.dataval)
# output the last link
# выводим последнюю ссылку
print(tuesday.nextval.dataval)
# ---------------------------------------
# We'll print LinkedList to console
# Мы выведем LinkedList на консоль
print(link_list.printList())
# Add a new node to the beginning of the list
# Добавляем новый узел в начало списка
link_list.push('Sunday')
# We'll print LinkedList to console
# Мы выведем LinkedList на консоль
print(link_list.printList())
# Added this Friday to the middle of our elements
# Добавили данную Пятница на середину наших элементов 
link_list.insertAfter(link_list.headval.nextval,'Friday')
print(link_list.printList())
# List of connected nodes and connections
# Добавили узел в конец списка
link_list.append('First day')
link_list.append('Second day')
link_list.append('Third day')
print(link_list.printList())
# Remove from the list of nodes 'Tuesday','Second day','Monday'
# Удаляем из списка узлы 'Tuesday','Second day','Monday'
print(link_list.deleteNode('Tuesday' and 'Second day' and 'Monday'))
print(link_list.printList())