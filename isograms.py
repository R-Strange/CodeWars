"""An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false"""

from collections import Counter

def is_isogram(string):
    string = string.lower()
    counted_string = Counter(string)
    if any(value > 1 for value in counted_string.values()):
        return False
    return True