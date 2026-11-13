class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1
            if cnt[c] % 2 == 0:
                res += 2

        for cnt in cnt.values():
            if cnt % 2 == 1:
                res +=1
                break
        return res
