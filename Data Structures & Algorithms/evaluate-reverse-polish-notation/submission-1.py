class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+','-','*','/']
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                if len(stack)>=2:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    if t == '+':
                        stack.append(n1+n2)
                    elif t=='-':
                        stack.append(n2-n1)
                    elif t=='*':
                        stack.append(n1*n2)
                    elif t=='/':
                        stack.append(int(n2/n1))
        return stack[-1]


        