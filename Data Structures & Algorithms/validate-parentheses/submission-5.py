class Solution:
    def isValid(self, s: str) -> bool:
        # charList = []
        # for character in s:
        #     if character == "(" or character == "[" or character == "{":
        #         charList.append(character)
        #     elif character == ")":
        #         if charList and charList[-1] == "(":
        #             charList.pop()
        #         else:
        #             return False
        #     elif character == "]":
        #         if charList and charList[-1] == "[":
        #             charList.pop()
        #         else:
        #             return False
        #     elif character == "}":
        #         if charList and charList[-1] == "{":
        #             charList.pop()
        #         else:
        #             return False
        # if not charList:
        #     return True
        # else:
        #     return False 
        stack = []
        charSet = {")":"(", "}":"{", "]":"["} # dictionary lets us map them efficiently
        for c in s:
            if c in charSet: # if its a closing element
                # if stack isnt empty and prev value in stack is equal to value at key close
                if stack and stack[-1] == charSet[c]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # return true if stack is empty otherwise false since ele still in stack
        return True if not stack else False