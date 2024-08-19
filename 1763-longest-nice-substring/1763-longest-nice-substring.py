class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(n):
            lst = set()
            for j in range(i, n):
                lst.add(s[j])
                if (all(c.lower() in lst and c.upper() in lst for c in lst)and len(ans) < j - i + 1):
                    ans = s[i : j + 1]
        return ans
        