def isValid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False 
            top = stack.pop()
            if pairs[char] != top:
                return False

    return len(stack) == 0


# Test cases
print(isValid("()"))       # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([)]"))     # False
print(isValid("([])"))     # True
