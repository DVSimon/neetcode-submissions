class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        curMax = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            curMax = max(curMax, freq[s[r]])

            if (r-l+1) - curMax > k:
                freq[s[l]] = freq[s[l]] - 1
                l += 1
            res = max(res, r-l+1)
        return res