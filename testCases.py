# Charlie Conneely
# Test Cases for the NFA 

import nfa

tests = [
    ["a.b|b*", "bbbbb", True],
    ["a.b|b*", "bbx", False],
    ["a.b", "ab", True],
    ["b**", "b", True],
    ["b+", "aa", False],
    ["b+", "b", True]
]

for test in tests:
    assert nfa.match(test[0], test[1]) == test[2], test[0] + (" should match  " \
            if test[2] else " should not match ") + test[1]


