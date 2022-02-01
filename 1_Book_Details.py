# 1.Write a Python program to maintain Book details like book_code, book_name, price and
# implement all the operations PUSH, POP, PEEK, SEARCH, LIST using stack data-
# structure (list).


stack = []
# structure of stack:
# [book_code, book_name, price]


def push(stack):
    book_code = input("Enter Book Code: ")
    book_name = input("Enter Book Name: ")
    price = input("Enter Price: ")
    stack.append([book_code, book_name, price])
    print("\n\n## PUSHED ##\n\n")
def pop(stack):
    try:
        popped_element = stack.pop()
        print(f"\n\n##POPPED: {popped_element} ##\n\n")
    except: print("## UNDERFLOW ##")
def peek(stack):
    peek = stack[-1]
    print(f"\n\n##TOP: {peek} ##\n\n")
def search(stack):
    found = False
    book_code = input("Enter Book Code: ")
    for i in stack:
        if i[0] == book_code:
            found = True 
            print(f'''\n\n FOUND! 
Book Code: {i[0]}
Book Name: {i[1]}
Price: {i[2]}''')
    if found == False: print("Book Not Found \n\n")



def list_entries(stack):
    print("\n\nENTRIES: ")
    for i in stack:
        print(i)


while True:
    print('''\t## STACK OPERATIONS ##
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


        
