class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Either two dicts an compare
        # Or when inserting to the dict, at each point check other string too?
        # Then check each value in dict is 0?

        # Check len first.
        if len(s) != len(t):
            return False

        anagramCheck = {}
        for index in range(len(s)):
            # if string s character index in it then add it to dict
            # if not in it then set to 1
            if s[index] in anagramCheck:
                anagramCheck[s[index]] += 1
            else:
                anagramCheck[s[index]] = 1
            # if string t character in dict then subtract 1 from value
            # if not in it then set to -1
                pass
            if t[index] in anagramCheck:
                anagramCheck[t[index]] -= 1
            else:
                anagramCheck[t[index]] = -1

        return all(value == 0 for value in anagramCheck.values())