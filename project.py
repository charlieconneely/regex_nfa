#! /usr/bin/env python3

# input
infix = "(a|b).c*"
#infix  = "a.b|c|b*"
print("Input is:",infix)
print("Expected output: ab|c*.")

# Convert input to a stack like list 
infix = list(infix)[::-1]

# Operator stack
opers = []

# Output list
postfix = []

# Operator precedence
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

# Loop through the input one character at a time
while infix:
    # pop a character from the input 
    c = infix.pop()

    # Decide precedence
    if c == '(':
        opers.append(c)
    elif c == ')':
        # pop the opers stack until you find the )
        while opers[-1] != '(':
            postfix.append(opers.pop())
        # Get rid of the '('
        opers.pop()
    elif c in prec:
        # push any ops on the opers stack with higher prec to the output
        while opers and prec[c] < prec[opers[-1]]:
            postfix.append(opers.pop())
        # Push c to the opers stack
        opers.append(c)
    else:
        postfix.append(c)

# Pop all operators to the output
while opers:
    postfix.append(opers.pop())

# convert output list to string
postfix = ''.join(postfix)

# print the result
print("Output is:", postfix)


