# Charlie Conneely
# Runner program 

import argparse
import nfa

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

# --verbose - for a more descriptive answer 
group.add_argument("-v", "--verbose", action="store_true")
# -- quiet - for a quick answer (just True or False)
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("text", help="The string of text", type=str)
parser.add_argument("regex", help="The regular expression", type=str)

args = parser.parse_args()

result = nfa.match(args.regex, args.text)

if args.verbose:
    if result == False:
        print("The text " + args.text + \
            " does not match the regular expression " + args.regex)
    else:
        print("The text " + args.text + \
                " matches the regular expression " + args.regex)
elif args.quiet:
    print(str(result))
else:
    print("nfa.match(" + args.text + "," + args.regex + ") = " + str(result))

