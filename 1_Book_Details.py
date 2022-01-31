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
    popped_element = stack.pop()
    print(f"\n\n##POPPED: {popped_element} ##\n\n")
def peek(stack):
    peek = stack[-1]
    print(f"\n\n##TOP: {peek} ##\n\n")
def search(stack):
    to_search_by = input('''Enter category to search by:
1. Book Code
2. Book Name
3. Price
Enter Choice: 
''')
    if to_search_by == '1':
        book_code = input("Enter Book Code: ")
        for i in stack:
            if i[0] == book_code:
                print(f'''\n\n FOUND! 
Book Name: {i[1]}
Price: {i[2]}''')

    elif to_search_by == '2':
        book_name = input("Enter Book Name: ")
        for i in stack:
            if i[1] == book_name:
                print(f'''\n\n FOUND! 
Book Code: {i[0]}
Price: {i[2]}''')
    elif to_search_by == '3':
        book_price = input("Enter Book Price: ")
        for i in stack:
            if i[2] == book_price:
                print(f'''\n\n FOUND! 
Book Code: {i[0]}
Book Name: {i[1]}''')
    else:
        print("##INVALID##")

def list(stack):
    print("\n\nENTRIES: ")
    for i in stack:
        print(i)

def main():
    while True:
        print('''\t## STACK OPERATIONS ##
1. Push
2. Pop
3. Peek
4. Search
5 List
6. Exit''')
        ch = input("Enter Choice: ")
        if ch == '1': push(stack)
        elif ch == '2': pop(stack)
        elif ch == '3': peek(stack)
        elif ch == '4': search(stack)
        elif ch == '5': list(stack)
        elif ch == '6': break  

if __name__ == '__main__':
    main()
        
