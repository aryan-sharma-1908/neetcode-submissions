class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if(token == '+' or token == '-' or token == '*' or token == '/'):
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if(token == '-'):
                    stack.append(str(n1 - n2))
                elif(token == '*'):
                    stack.append(str(n1 * n2))
                elif(token == '/'):
                    stack.append(str(int(n1 / n2)))
                else:
                    stack.append(str(n1 + n2))
            else:
                stack.append(token)
        return int(stack.pop())
        