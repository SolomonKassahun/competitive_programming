class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lst = list(s)
        for i in range(len(s)):
            for j in range(i):
                if (s[i] == s[j]):
                    return s[i]

            
            
        