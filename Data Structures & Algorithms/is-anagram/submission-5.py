class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False    
        for index in range(len(s)):
            sDict[s[index]] = sDict.get(s[index], 0) + 1
            tDict[t[index]] = tDict.get(t[index], 0) + 1

        return sDict == tDict