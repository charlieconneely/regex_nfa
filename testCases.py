# Charlie Conneely
# Test Cases for the NFA 

import nfa

# Test cases for the match function
matchTests = [
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

# Test cases for the shunt function
shuntTests = [
    ["a.b", "ab."],
    ["a|b", "ab|"],
    ["(a?)|b", "a?b|"],
    ["(a+).b", "a+b."],
    ["a.(b|c)", "abc|."],
    ["(a|b).b+", "ab|b.+"],
    ["(a?)|(a+)", "a?a+|"],
    ["((a|b).(a?))|((a+).(a.b))", "ab|a?.a+ab..|"]
]

# loop through test cases and assert each
# nfa.match
for test in matchTests:
    assert nfa.match(test[0], test[1]) == test[2], test[0] + (" should match  " \
            if test[2] else " should not match ") + test[1]
# nfa.shunt
for test in shuntTests:
    assert nfa.shunt(test[0]) == test[1] 

