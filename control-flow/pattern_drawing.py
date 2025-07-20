#Utilize while loops and nested for loops
#to draw a simple text-based pattern.

#Prompy user to input a positive integer representing size of pattern
size_shape = int(input("Enter the size of the pattern: "))

#Draw the pattern
outer_pattern = 1

while outer_pattern < (size_shape + 1):

    inner_pattern = 1
    while inner_pattern <= (size_shape + 1):
        print("*",end="")
        inner_pattern += 1
    print()
    outer_pattern += 1
