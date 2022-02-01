# 2. Write a program to input a line of text from the input terminal into stack and output the
# string in the reveres order, each character appearing twice. (Eg. the string a b c d e should
# be ee dd cc bb aa)
stack = []
for i in input("Enter String to invert: ")[::-1]: stack.append(i)
for i in stack: print(i*2, end = "")
