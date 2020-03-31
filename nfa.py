# Charlie Conneely
# Functions/Algorithms necessary to compare a string to a regex
# using a non-deterministic finite automaton

# Import classes for Thompson's Construction
from thompsons import *

def shunt(infix):
    """
    Create an postfix regular expression from it's infix."
  
    Parameters:
    arg1 (String): Infix regular expression.

    Returns:
    String: The postfix equivalent.
    """

    # Convert input to a stack like list 
    infix = list(infix)[::-1]

    # Operator stack
    opers = []

    # Output list
    postfix = []

    # Operator precedence
    prec = {'*': 100, '.': 90, '+': 80, '|': 60, ')': 40, '(': 20}

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
            # push the character to the output 
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # convert output list to string
    postfix = ''.join(postfix)
    return postfix


def regex_compile(infix):
    """
    Create an NFA fragment representing the infix regular expression."
  
    Parameters:
    arg1 (String): Infix regular expression.

    Returns:
    Fragment: NFA fragment representing the regular expression
    """
    
    # Convert the infix to postfix
    postfix = shunt(infix)
    # Create a stack from the postfix 
    postfix = list(postfix)[::-1]
    # Stack for NFA fragments
    nfa_stack = []
    
    # Run through postfix stack
    while postfix:
        # Pop a character from postfix 
        c = postfix.pop()
        if c == '.':
            # append
            # pop 2 fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)
            # new start state is frag2's start
            start = frag2.start
            # new accept state is frag1's accept
            accept = frag1.accept
        elif c == '|':
            # or
            # Pop 2 fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()

            # Create new start and accept states 
            accept = State()
            start = State(edges = [frag2.start, frag1.start])
            # Point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
        elif c == '*':
            # Pop a single fragment off the stack 
            frag = nfa_stack.pop()
            # create new start and accept states
            accept = State() 
            start = State(edges=[frag.start, accept])
            # point the arrows
            frag.accept.edges = [frag.start, accept]
        elif c == '+':
            # link to diagram example of + nfa  
            # https://medium.com/@phanindramoganti/regex-under-the-hood-implementing-a-simple-regex-compiler-in-go-ef2af5c6079
            # One or more
            # so far working but no different from * fragment 
            frag = nfa_stack.pop()
            # create new start and accept states
            accept = State()
            start = State(edges=[frag.start])
            frag.accept.edges = [frag.start, accept]           
        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # Create new instance of Fragment to represent the new NFA 
        newFrag = Fragment(start, accept)
        # Push the new NFA to the stack 
        nfa_stack.append(newFrag)

    # NFA should contain just one NFA 
    return nfa_stack.pop()

def loopForEpsilons(state, current):
    """
    Loop through NFA for edges marked Epsilon and add them to a set

    Parameters:
    arg1 (Fragment): Collection of NFA Fragments.
    arg2 (set): Set containing States that have been checked

    """
    # check if state hasn't already been looped through
    if state not in current:
        current.add(state)
        if state.label is None:
            for moreEdges in state.edges:
                loopForEpsilons(moreEdges, current)


def loopForMatches(prev, current, c):
    """
    Loop through NFA for labels that match the current character 
    and add that state to a set

    Parameters:
    arg1 (Fragment): Collection of NFA Fragments.
    arg2 (set): Set containing States that have been checked
    arg3 (char): A single character from the string of text

    """
    for state in prev:
        if state.label is not None:
            if state.label == c:
                loopForEpsilons(state.edges[0], current)

def compareStringToNFA(nfa, s):
    """
    Run through NFA to check if it matches the string

    Parameters:
    arg1 (Fragment): Collection of NFA Fragments.
    arg2 (String): String to be checked against regular expression

    Returns:
    bool: True if the string suits the regular expression - False otherwise
    """

    result = False
    # create list of chars from string
    text = list(s)[::-1]
    current = set()
    prev = set()
    allStates = set()
 
    # run through epsilons and add all states to set 
    loopForEpsilons(nfa.start, current)  
    
    # run through char list
    while text:
        prev = current
        current = set()
        # pop one off the top
        c = text.pop()

        # search from beginning for matching labels
        loopForMatches(prev, current, c)


    if nfa.accept in current:
        result = True

    return result   


def match(regex, s):
    """
    Convert regular expression to an nfa using the regex_compile method
    Return result by calling a method to check if the string fits the nfa 

    Parameters:
    arg1 (String): The regular expression
    arg2 (String): The text to be executed against the regular expression

    Returns:
    bool: True if the string suits the regular expression - False otherwise
    """
    # returns true if regex matches the text
    # returns false otherwise

    # compile regex into NFA
    nfa = regex_compile(regex)
    # check if nfa matches string s 
    # function to run the text through the nfa
    result = compareStringToNFA(nfa, s)
    return result

if __name__ == "__main__":
    print("Please run the runner.py file if \
you would like to execute this program.")

    print(match("a.b|b*", "bbb"))

