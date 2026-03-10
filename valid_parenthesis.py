class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #basically add to the stack while its open, when there is a close we see if
        # it closes on the opposyte symbol
        for symbol in s:
            if symbol == "(" or symbol == "{" or symbol == "[":
                stack.append(symbol)
            elif stack:
                if symbol == ")":
                    open_bracket = stack.pop()
                    if not open_bracket == "(":
                        return False
                if symbol == "}":
                    open_bracket = stack.pop()
                    if not open_bracket == "{":
                        return False
                if symbol == "]":
                    open_bracket = stack.pop()
                    if not open_bracket == "[":
                        return False
            else: 
                return False
        if stack:
            return False
        return True