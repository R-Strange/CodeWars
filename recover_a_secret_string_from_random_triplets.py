
"""There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string.
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information
to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

example:secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
"""
from itertools import permutations
# TOO SLOW
def recoverSecretSLOW(triplets):
    # Create a set of all unique letters in the triplets
    letters = set([letter for triplet in triplets for letter in triplet])
    
    # Generate all possible permutations of the letters
    perms = permutations(letters)
    
    # Check each permutation for validity and return the first one that is valid
    for perm in perms:
        valid = True
        for triplet in triplets:
            if not all(perm.index(triplet[i]) < perm.index(triplet[i+1]) for i in range(2)):
                valid = False
                break
        if valid:
            return ''.join(perm)



triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

recoverSecretSLOW(triplets)

# topological sort
from collections import defaultdict

def recoverSecret(triplets):
    graph = defaultdict(list)

    all_letters = set()

    for triplet in triplets:
        graph[triplet[1]].append(triplet[0])
        graph[triplet[2]].append(triplet[1])
        all_letters.update(triplet)
    
    result = []
    while all_letters:
        for letter in all_letters:
            if all(parent not in all_letters for parent in graph[letter]):
                result.append(letter)
                all_letters.remove(letter)
                break
    return ''.join(result)