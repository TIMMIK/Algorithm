# Bloom filters(en):
# A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. 
# For example, checking availability of username is set membership problem, where the set is the list of all registered username.

# Bloom filters(ru):
# Фильтр Блума — это малогабаритная вероятностная структура данных, которая используется для проверки того, является ли элемент членом множества. 
# Например, проверка наличия имени пользователя — это проблема членства в наборе, где набор — это список всех зарегистрированных имен пользователей.



# Secure Hash Algorithm(en):
# SHA stands for Secure Hash Algorithms. 
# These are set of cryptographic hash functions. 
# These functions can be used for various applications like passwords etc. 
# The hashlib module of Python is used to implement a common interface to many different secure hash and message digest algorithms.

# Secure Hash Algorithm(ru):
# SHA расшифровывается как Secure Hash Algorithms.
# Это набор криптографических хеш-функций.
# Эти функции можно использовать для различных приложений, таких как пароли и т. д.
# Модуль hashlib Python используется для реализации общего интерфейса для многих различных алгоритмов безопасного хеширования и дайджеста сообщений.



# Diffie Helman Algorithm(en):
# The Diffie–Hellman (DH) Algorithm is a key-exchange protocol that enables two parties communicating over public channel to establish a mutual secret without it being transmitted over the Internet. 
# DH enables the two to use a public key to encrypt and decrypt their conversation or data using symmetric cryptography.

# Diffie Helman Algorithm(ru):
# Алгоритм Диффи-Хеллмана (DH) — это протокол обмена ключами, который позволяет двум сторонам, общающимся по общедоступному каналу, установить общий секрет без его передачи через Интернет. 
# DH позволяет им использовать открытый ключ для шифрования и дешифрования их разговоров или данных с использованием симметричной криптографии.



# Linear programming(en):
# Linear programming is a technique to optimize any problem with multiple variables and constraints. 
# It's a simple but powerful tool every data scientist should master.

# Linear programming(ru):
# Линейное программирование — это метод оптимизации любой задачи с несколькими переменными и ограничениями. 
# Это простой, но мощный инструмент, которым должен овладеть каждый специалист по данным.

# Code --- >

import pulp as p

# Create a LP Minimization problem
# Создать задачу минимизации LP
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables:
# Создаем проблемные переменные:
# 1. Create a variable x >= 0
# 1. Создайте переменную x >= 0
x = p.LpVariable("x", lowBound = 0) 
# 2. Create a variable y >= 0
# 2. Создайте переменную y >= 0
y = p.LpVariable("y", lowBound = 0) 
# Objective Function
# Целевая функция
Lp_prob += 3 * x + 5 * y

# Constraints:
# Ограничения:
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

# Display the problem
# Показать проблему
print(Lp_prob)

status = Lp_prob.solve()
print(p.LpStatus[status])

# Printing the final solution
# Печать окончательного решения
print(p.value(x), p.value(y), p.value(Lp_prob.objective))



