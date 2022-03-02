#+-------------------------------+
#| File: grace_hw4b.py           |
#| Author: Isaiah Grace          |
#| Date: 2022/3/2                |
#| Lab Section: Tuesday          |
#| Email: isaiah.grace@maine.edu |
#| Description: Number checker   |
#| Collabs: N/a                  |
#+-------------------------------+

user_number = input("Enter an odd number: ")

while (int(user_number) % 2 == 0) or (int(user_number) == 0):
    user_number = input("Enter an odd number: ")

print("Thanks!")
