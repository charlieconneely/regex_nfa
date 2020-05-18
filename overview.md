## Charlie Conneely - G00348887
## Overview of my 3rd year Graph Theory project

### **Introduction**
The purpose of this Python application is to create a Non-Deterministic Finite Automata (NFA) from a regular expression and then use this NFA to check if any given string of text matches the regular expression. 

To understand exactly what that means, first let's ask: \
**What is a Finite Automata?** \
A finite automaton (FA) is a simple idealized machine used to recognize patterns within input taken from some character set (or alphabet) C. So, simply put, an FA is a machine that will take in an input character and tell us if it is a match. 
The difference between a Deterministic and a *Non* Deterministic FA is simply that with a DFA, from each state, you are certain of what the following state will be. Where as with an NFA, the following state can vary depending on context.

For more information on NFA's click [here](https://www.tutorialspoint.com/automata_theory/non_deterministic_finite_automaton.htm)

The NFA is created *from* the regular expression. So... \
**What is a regular expression?**  \
A regular expression (regex for short) is a special text string for describing a search pattern. For example, the regex "a*|b", when ran against a string of text, will check if the text is contains any amount of a characters *or* the b character. This is because the special character * represents *zero or any amount of* and | represents *or*.

To become more familiar with regular expressions click [here](https://www.regular-expressions.info/quickstart.html) 

Let's consider for a moment that you are walking through a building that has signs at each new corridor that read - if you are so and so, you may/may not go this way *or* you should use this corridor instead. Eventually, if you suit all the conditions on the signs, you'll reach the end. In this analogy, you are the operand (letter/number) and this connection of corridors and signs is the NFA. The conditions and the layout of the corridors will be designed to represent the regular expression. 

***
To simulate an NFA in my application, I needed to create two object classes: One for **States** and the other for **Fragments**.
- Each **Fragment** has a start and end state (as with all NFAs).  
- Each **States** has one or two edges (which lead to other states), if it has zero edges it should be the end state. Those edges have a label which denotes the condition - if the letter matches the label *or* if the label is an epsilon - the next state will be reached.    

Below I provided a diagram of an NFA. You can find their representative objects in the [thompsons.py](./thompsons.py) class.
![nfadiagram](/imgs/nfaDiagram.png)
***
Before we create the NFA from the regular expression, we need to convert the regex from **infix** to **postfix**.   
- **Infix** refers to an expression in the form a op b. When an operator is inbetween every pair of operands.   
- **Postfix** refers to an expression in the form of a b op. When an operator is followed for every pair of operands. 

As humans we prefer to see the operator inbetween the operands (as with infix notation), as it's easier for us to interpret. However, postfix is more convenient for evaluating formulas on computers with stack.  
To see how I converted the infix string to postfix using the shunting yard algorithm, please redirect your attention to the shunt method in the [nfa.py](./nfa.py) class.   
For more info on infix/postfix notation and the shunting yard algorithm, please click [here](https://brilliant.org/wiki/shunting-yard-algorithm/).
***
### **How to run the program**
- When you have your virtual machine set up, the first command to run is "sudo apt update", this will go to the debian package list online for all available packages and download them.   
To upgrade these packages run "sudo apt ugrade" 
- If the command line editor vi is not already installed, you should install VI 8.1. 
- You may also need to install:
  - Python 2.7.16
  - git: sudo apt install git
  - A c compiler: sudo apt install build-essential
  - File downloader: sudo apt install wget 

After this installation process is finished use run "git clone <https://github.com/charlieconneely/GraphTheoryProject>". Next, go into the GraphTheoryProject directory (cd GraphTheoryProject).   
To run the code:
- Run "python3 runner.py" to execute the runner file.
- The program will then ask you to enter the string of text e.g. "aaab"
- Next you will be asked to enter the regular expression e.g. "a*"
- The program will then return True or False depending on whether your string matches the regular expression.
***
### **How to test the program**
- To test the program, I created a seperate python script file called [testCases.py](./testCases.py).
- This file contains 2 arrays of test cases - one array of test cases for the shunt method, and another array of test cases for the match function. 
- Both of these arrays were tested using the assert keyword. To familiarize yourself with the assert keyword click [here](https://www.w3schools.com/python/ref_keyword_assert.asp).
- **Testing the shunt function**:
  - Each test case in the array is it's own array in the format [String, String].
  - The first string in the array represents the regular expression in *infix*.
  - The second string represents what regular expression should look like in *postfix*. 
  - The shunt function was imported from nfa.py. 
  - The shunt function was then asserted for each test case in the array using a for loop.
  - If the returned string from the shunt method matches the expected output, no error message will occur.

- **Testing the match function**: 
  - Each test case in the array is it's own array in the format [String, String, Boolean].
  - The first string in the array represents the regular expression.
  - The second string is text to which the regex will be compared.
  - And the boolean value represents the expected result.
  - The match function was imported from nfa.py
  - The match function was then asserted for each test case in the array using a for loop.
  - The last param of the assert method is an if/else statement, which will indicate to the user if a test case was successful/unsuccessful.
  
  To test out the shunt or match method yourself, simply add a similar object to either array. 
  To run the tests, simply run the command "python3 testCases.py". 
  *** 



