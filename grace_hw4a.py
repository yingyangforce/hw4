#+-------------------------------+
#| File: grace_hw4a.py           |
#| Author: Isaiah Grace          |
#| Date: 2022/3/2                |
#| Lab Section: Tuesday          |
#| Email: isaiah.grace@maine.edu |
#| Description: Walmart Greeter  |
#| Collabs: N/a                  |
#+-------------------------------+

user_name = input("Please enter a name: ")

while user_name != 'q':
    print(f"Pleased to meet you, {user_name}")
    user_name = input("Please enter a name: ")

print("Goodbye")

