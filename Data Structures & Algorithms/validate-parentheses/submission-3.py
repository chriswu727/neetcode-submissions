class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashS = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in hashS:
                if stack and stack[-1] == hashS[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False