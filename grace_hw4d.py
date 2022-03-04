#+-------------------------------+
#| File: grace_hw4d.py           |
#| Author: Isaiah Grace          |
#| Date: 2022/3/2                |
#| Lab Section: Tuesday          |
#| Email: isaiah.grace@maine.edu |
#| Description: squarer          |
#| Collabs: N/a                  |
#+-------------------------------+


numList = (4,11,18,25,32,39,46,53,60)

def squareNumber(val):
    return val**2 if val**2 % 2 == 0 else "odd"
        
for i in range(len(numList)):
    print(f"Value {i} is {squareNumber(numList[i])}!")

