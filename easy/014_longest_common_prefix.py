"""
LeetCode Problem 14: Longest Common Prefix (Easy)

Problem Statement:
------------------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
----------
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
Explanation: The longest common prefix is "fl" as all words start with it.

Example 2:
----------
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
------------
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

Approach:
---------
1️⃣ **Start with the first word** in the list as the initial prefix.
2️⃣ **Compare this prefix** with the second word. If they don’t match, reduce the prefix.
3️⃣ **Continue comparing** with each subsequent word, reducing the prefix if necessary.
4️⃣ **If the prefix becomes empty** at any point, return "".
5️⃣ **Otherwise, return the final common prefix.**
"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(f"Example 1: {longest_common_prefix(['flower', 'flow', 'flight'])}")
print(f"Example 2: {longest_common_prefix(['dog', 'racecar', 'car'])}")
    
    