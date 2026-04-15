class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in t or t[i] not in s or s.count(s[i]) != t.count(s[i]) :
                    return False
                    break
            return True
        return False