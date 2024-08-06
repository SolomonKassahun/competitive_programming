class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backString(S):
            stack = []
            for char in S:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return backString(s) == backString(t)
        
        
        