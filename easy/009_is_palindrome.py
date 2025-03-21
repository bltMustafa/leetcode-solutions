"""
LeetCode Problem 9: Palindrome Number (Easy)

Problem Statement:
------------------
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

A number is considered a palindrome if it reads the same forward and backward.

Example 1:
-----------
Input: x = 121
Output: True
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
-----------
Input: x = -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
-----------
Input: x = 10
Output: False
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
------------
-2^31 <= x <= 2^31 - 1

Follow-up:
----------
Can you solve it without converting the integer to a string?
"""

# Math Solution
def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    return x == reversed_half or x == reversed_half // 10

print(f'is_palindrome(121): {is_palindrome(121)}') # True
print(f'is_palindrome(-121): {is_palindrome(-121)}') # False
print(f'is_palindrome(10): {is_palindrome(10)}') # False


# String Solution
def is_palindrome_string(x: int) -> bool:
    return str(x) == str(x)[::-1]

print(f'is_palindrome_string(121): {is_palindrome_string(121)}') # True
print(f'is_palindrome_string(-121): {is_palindrome_string(-121)}') # False
print(f'is_palindrome_string(10): {is_palindrome_string(10)}') # False
