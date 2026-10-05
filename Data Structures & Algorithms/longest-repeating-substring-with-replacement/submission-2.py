class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # This time instead of looping all the way through twice, we loop once with a window
        # if the window is too big we need to decrement count of left pointer vari then
        # incr3ease counters of left
        res = 0

        curMax, freq = 0, {}
        l = 0
        for r in range(len(s)):
            # get t he frequency of right pointer and set in dict(def 0) increment 1
            freq[s[r]] = freq.get(s[r], 0) + 1
            # Set the max as the max between frequency of letter and the curMax
            # set curmax as max of curmax or freq of letter
            curMax = max(curMax, freq[s[r]])

            # if window - current max > k; we need to move left pointer over
            # decrement left pointer value from freq counter
            # increment left
            if (r-l+1) - curMax > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

            # Set max to max between result and window
            res = max(res, (r-l+1))
        return res

