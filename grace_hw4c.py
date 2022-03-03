#+-------------------------------+
#| File: grace_hw4c.py           |
#| Author: Isaiah Grace          |
#| Date: 2022/3/2                |
#| Lab Section: Tuesday          |
#| Email: isaiah.grace@maine.edu |
#| Description: averager         |
#| Collabs: N/a                  |
#+-------------------------------+

name = input("Please enter a valid name: ")

while name != 'q':
    while len(name) < 1:
        user_name = input("Please enter a valid name: ")

    num_in = input(f"Hi {name}, please enter a number: ")

    num_sum = 0
    in_count = 0

    while int(num_in) != -1:
        num_sum += int(num_in)
        in_count += 1
        num_in = input(f"Hi {name}, please enter a number: ")

    if num_sum == 0:
        print(f"{name}, your average is 0.")
    else:
        print(f"{name}, your average is {num_sum / in_count}")

    name = input("Please enter a valid name: ")

print("Goodbye")
