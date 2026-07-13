class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in close_map:
                if len(stack) > 0 and stack[-1] == close_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0