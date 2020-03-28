# Charlie Conneely
# Runner program 

import nfa

text = input("Please enter your string of text: ")
regex = input("Please enter your regular expression: ")


print(nfa.match(regex, text))
