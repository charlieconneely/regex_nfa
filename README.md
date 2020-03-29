# GraphTheoryProject 

This repo contains a project (written in python) that will create a Non-Deterministic Finite Automaton (NFA),
 cabable of comparing a string of text to a regular expression (both entered as input by the user).

The program will:
- Parse the regular expression from postfix to infix notation.
- Build a series of small non-deterministic finite automaton (NFA) for parts of the regular expression.
- Combine these small NFA's to create the over all NFA.
- Implement a series of functions to compare each character in the string of text to the NFA to see if it is a match.

Dependencies needed in development:
- VI 8.1
- Python 2.7.16
- git version 2.20.1
- gcc (Debian 8.3.0-6) 8.3.0
- Wget 1.20.1

Running the program from VI:
- CD into the GraphTheoryProject folder container the necessary files.
- Enter "python3 runner.py"
- The program will then ask you to enter the string of text eg "aaab"
- Next you will be asked to enter the regular expression eg "a*"
- The program will then return True of False depending on whether you're string matches 
the regular expression. 

Testing the program:
 

