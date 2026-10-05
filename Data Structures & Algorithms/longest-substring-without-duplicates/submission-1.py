class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        curMax = 0
        res = 0
        left = 0
        for right in range(len(s)):

            while s[right] in freq:
                freq.remove(s[left])        
                curMax -= 1
                left += 1

            # add right char
            freq.add(s[right])
            curMax += 1
            res = max(curMax, res)
        return res




