# 4.Write a python program to maintain Student details like roll_no, name, section and
# implement all the operations PUSH, POP, PEEK, SEARCH, LIST using stack data-
# structure (list).


stack = []
# structure of stack:
# [roll_no, name, section]


def push(stack):
    roll_no = input("Enter Roll No.: ")
    name = input("Enter Name: ")
    section = input("Enter section: ")
    stack.append([roll_no, name, section])
    print("\n\n## PUSHED ##\n\n")
def pop(stack):
    popped_element = stack.pop()
    print(f"\n\n##POPPED: {popped_element} ##\n\n")
def peek(stack):
    peek = stack[-1]
    print(f"\n\n##TOP: {peek} ##\n\n")
def search(stack):
    found = False
    roll_no = input("Enter Roll No.: ")
    for i in stack:
        if i[0] == roll_no:
            found = True 
            print(f'''\n\n FOUND! 
Roll No.: {i[0]}
Name: {i[1]}
section: {i[2]}''')
    if found == False: print("Student Not Found \n\n")



def list_entries(stack):
    print("\n\nENTRIES: ")
    for i in stack:
        print(i)


while True:
    print('''\t## Student Details ##
1. Push
2. Pop
3. Peek
4. Search
5. List
6. Exit''')
    ch = input("Enter Choice: ")
    if ch == '1': push(stack)
    elif ch == '2': pop(stack)
    elif ch == '3': peek(stack)
    elif ch == '4': search(stack)
    elif ch == '5': list_entries(stack)
    elif ch == '6': break  


        
