# Charlie Conneely
# Test Cases for the NFA 

import nfa

tests = [
    ["a.b|b*", "bbbbb", True],
    ["a.b|b*", "bbx", False],
    ["a.b", "ab", True],
    ["b**", "b", True],
    ["b+", "aa", False],
    ["b+", "b", True],
    ["b+", "bbb", True],
    ["b+", "", False],
    ["a?", "", True],
    ["a?", "a", True],
    ["a?", "aaa", False],
    ["a?", "b", False],
    ["a?", "bbb", False],
    ["(a?)|(a.a.a)", "aaa", True],
    ["(a?)|(ab)", "a", True],
    ["a?", "abc", False]
]

for test in tests:
    assert nfa.match(test[0], test[1]) == test[2], test[0] + (" should match  " \
            if test[2] else " should not match ") + test[1]


