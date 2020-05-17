# Overview of my 3rd year Graph Theory project
## Charlie Conneely - G00348887

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

