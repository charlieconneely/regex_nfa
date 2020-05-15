# Overview of my 3rd year Graph Theory project
## Charlie Conneely - G00348887

The purpose of this Python application is to create a Non-Deterministic Finite Automata (NFA) from a regular expression and then use this NFA to check if any given string of text matches the regular expression. 

To understand exactly what that means, first let's ask:
**What is a Finite Automata?** 
A finite automaton (FA) is a simple idealized machine used to recognize patterns within input taken from some character set (or alphabet) C. So, simply put, an FA is a machine that will take in an input character and tell us if it is a match. 
The difference between a Deterministic and a *Non* Deterministic FA is simply that with a DFA, from each state, you are certain of what the following state will be. Where as with an NFA, the following state can vary depending on context.

For more information on NFA's click [here](https://www.tutorialspoint.com/automata_theory/non_deterministic_finite_automaton.htm)

The NFA is created *from* the regular expression. So...
**What is a regular expression?**  
A regular expression (regex for short) is a special text string for describing a search pattern. For example, the regex "a*|b", when ran against a string of text, will check if the text is contains any amount of a characters *or* the b character. This is because the special character * represents *zero or any amount of* and | represents *or*.

To become more familiar with regular expressions click [here](https://www.regular-expressions.info/quickstart.html) 
