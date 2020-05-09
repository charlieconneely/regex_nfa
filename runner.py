# Charlie Conneely
# Runner program 

import argparse
import nfa

parser = argparse.ArgumentParser()
parser.add_argument("text", help="The string of text", type=str)
parser.add_argument("regex", help="The regular expression", type=str)

args = parser.parse_args()

#text = input("Please enter your string of text: ")
#regex = input("Please enter your regular expression: ")
result = nfa.match(args.regex, args.text)

print(result)
