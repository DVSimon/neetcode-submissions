class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can do the same with two dicts
        # Check dict lens same first
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}
        for x in range(len(s)):
            dictS[s[x]] = dictS.get(s[x], 0) + 1
            dictT[t[x]] = dictT.get(t[x], 0) + 1
        return dictS == dictT