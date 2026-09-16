class Solution:
    def isValid(self, s: str) -> bool:
        charList = []
        for character in s:
            if character == "(" or character == "[" or character == "{":
                charList.append(character)
            elif character == ")":
                if charList and charList[-1] == "(":
                    charList.pop()
                else:
                    return False
            elif character == "]":
                if charList and charList[-1] == "[":
                    charList.pop()
                else:
                    return False
            elif character == "}":
                if charList and charList[-1] == "{":
                    charList.pop()
                else:
                    return False
        if not charList:
            return True
        else:
            return False 