# GraphTheoryProject 

This repo contains a project (written in python) that can create a Non-Deterministic Finite Automaton (NFA) from a regular expression and then use this NFA to check if any given string of text matches the regular expression.

The program will:
- Parse the regular expression from infix to postfix notation.
- Build a series of small non-deterministic finite automaton (NFA) for parts of the regular expression.
- Combine these small NFA's to create the over all NFA.
- Implement a series of functions to compare each character in the string of text to the NFA to see if the regular expression matches the string of text.

Dependencies needed in development:
- VI 8.1
- Python 2.7.16
- git version 2.20.1
- gcc (Debian 8.3.0-6) 8.3.0
- Wget 1.20.1

===================================================================================

Running the program from VI:
- CD into the GraphTheoryProject folder containing the necessary files.
- Enter "python3 runner.py" to execute the runner file.
- The program will then ask you to enter the string of text e.g. "aaab"
- Next you will be asked to enter the regular expression e.g. "a*"
- The program will then return True or False depending on whether your string matches 
the regular expression. 

Testing the program:
- To test the program, I created a seperate python script file called testCases.py
- This file contains an array of test cases.
- Each test case in the array is it's own array in the format [String, String, Boolean].
- The first string in the array represents the regular expression.
- The second string is text to which the regex will be compared.
- And the boolean value represents the expected result.
- The match function was imported from nfa.py
- The match function was then asserted for each test case in the array using a for loop.
- The last param of the assert method is an if/else statement, 
which will indicate to the user if a test case was successful/unsuccessful.

===================================================================================

Before I begin describing how the code works, here is the layout of the files and their contents:

nfa.py:
--------------
(functions)
- shunt()
- regex_compile()
- loopForEpsilons()
- loopForMatches()
- compareStringToNFA()
- match()

- An if statement to determine if nfa.py is run as main.

runner.py:
--------------
This class just contains two variables for the regular expression and the text.
The match function is imported from nfa.py, executed and the result printed to the console.

testCases.py:
--------------
- An array of test cases.
- A for loop to filter through them.
- An assert method to test the match method (imported from nfa).

thompsons.py:
--------------
(classes)
- State - representing the states of an NFA.
- Fragment - representing the fragments of an NFA.


Description of how the program runs (sequentially):

- After the user has entered the string of text and the regular expression,
the match() function is called, which will take in these two parameters.
- The first thing this function will do is call the regex_compile() method,
taking the regular expressioon as a parameter. 
- This method will then call the shunt() method, which will take in the infix 
regular expression, and return the postfix. 
- Next, inside regex_compile, the postfix string will then be converted to a stack.
This stack of characters will then be examined by a series of if/elif statements.
- These if/elif statements will use the characters from the postfix, along with the
 Fragment and State classes to create the over-all NFA. 
- The NFA is then returned to the match method and stored in a variable called 'nfa'.
- Next in the match method, the compareStringToNFA() boolean method is called, taking
the nfa and the string of text as parameters.
- This method first calls the loopForEpsilons method, which takes in the start of the NFA
and a set. It will proceed to loop through the NFA in search of epsilons (labels marked None)
whilst adding these states to a set.
- The compareStringToNFA method will then loop through each character in the string of
text and call upon a function called loopForMatches(). This method will search the NFA
for labels marked with the same character as the current character in execution.
All of these states will also be added to a set.
- After this method, the compareStringToNFA method will then check if the accept state
of the NFA is present in this set. A boolean variable is then returned to the match function,
True if the accept state is present.
- The match function will then return this boolean variable to the user: True if the string is a
match, or False otherwise.


How each component of the program works:

- shunt()
--------------
- 


