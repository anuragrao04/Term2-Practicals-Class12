# 2. Write a program to input a line of text from the input terminal into stack and output the
# string in the reveres order, each character appearing twice. (Eg. the string a b c d e should
# be ee dd cc bb aa)

string = input("Enter String to invert: ")[::-1]
print("Reversed string(twice): ")
for i in string: print(i*2, end = "")
