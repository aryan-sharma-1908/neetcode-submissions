class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = deque()
        for c in s:
            if(c == '(' or c == '{' or c == '['):
                stack.append(c)
            if(c == ')'):
                if(len(stack) == 0 or stack.pop() != '('):
                    return False
            if(c == ']'):
                if(len(stack) == 0 or stack.pop() != '['):
                    return False
            if(c == '}'):
                if(len(stack) == 0 or stack.pop() != '{'):
                    return False

        if len(stack) != 0:
            return False
        else:
            return True





