"""
LeetCode Problem 13: Roman to Integer (Easy)

Problem Statement:
------------------
Roman numerals are represented by seven different characters: I, V, X, L, C, D and M.

Symbol       Value
------------------
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written from largest to smallest from left to right. 
However, when a smaller value appears before a larger one, it indicates subtraction.

There are six such special cases:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Your task is to convert a given Roman numeral string to its integer equivalent.

Example 1:
----------
Input: s = "III"
Output: 3
Explanation: III = 1 + 1 + 1 = 3

Example 2:
----------
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3 → 50 + 5 + 3 = 58

Example 3:
----------
Input: s = "MCMXCIV"
Output: 1994
Explanation:
M = 1000, CM = 900, XC = 90, IV = 4
→ 1000 + 900 + 90 + 4 = 1994

Constraints:
------------
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
- It is guaranteed that s is a valid Roman numeral in the range [1, 3999]
"""


def roman_to_integer(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]

    return total


print(f'roman_to_integer("III"): {roman_to_integer("III")}')
print(f'roman_to_integer("MDCLXVI"): {roman_to_integer("LVIII")}')
print(f'roman_to_integer("MCMXCIV"): {roman_to_integer("MCMXCIV")}')


    