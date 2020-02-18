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

# ========================
# Thompsons's Classes 18/02
# ========================

class State:
    edges = []
    # label for arrows - None = epsilon
    label = None

    # Constructor
    def __init__(self, label=None, edges=[]):
        self.label = label
        self.edges = edges


class Frag:
    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# test instances
instance1 = State(label='a', edges=[1])
instance2 = State(label='b', edges=[instance1])
frag1 = Frag(instance1, instance2)

print(instance1.label)
print(instance2.edges[0])
print(frag1)

# =================
# Thompson's Classes
# =================
