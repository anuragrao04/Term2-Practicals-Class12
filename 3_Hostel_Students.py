# 3.Write a python program to PUSH,POP,SEARCH and display the records of hostel using
# list as stack data structure in python. Records should contain: Hostel Room number, Total
# no of students per room. Compute the total number of students in the Hostel and display
# the same.

stack = []
# Stack structure:
# [room number, no_of_students]

def push(stack):
    room_num = input("Enter Room Number: ")
    no_of_studs = input("Enter Number Of Students In Room: ")
    stack.append([room_num, no_of_studs])
    print("\n\n## PUSHED ##\n\n")

def pop(stack):
    popped = stack.pop()
    print(f"\n\n##POPPED: {popped} ##\n\n")

def search(stack):
    found = False
    room_no = input("Enter Room Number To Search: ")
    for i in stack:
        if i[0] == room_no:
            print(f"Room Found. There are {i[1]} students in that room.")
            found = True
    if found == False: print("Room not found")
    
def compute_total(stack):
    sum = 0
    for i in stack:
        sum += int(i[1])
    print("Total Number of Students: ", sum)



while True:
    print('''\t## Hostel Rooms ##
1. Push
2. Pop
3. Search
4. Total Number Of Students
5. Exit''')
    ch = input("Enter Choice: ")
    if ch == '1': push(stack)
    elif ch == '2': pop(stack)
    elif ch == '3': search(stack)
    elif ch == '4': compute_total(stack)
    elif ch == '5': break  