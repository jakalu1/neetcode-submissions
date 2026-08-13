class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for c in tokens:
            if c == '+':    #top_num + under top_num
                stack.append(stack.pop() + stack.pop())
            elif c == '-': 
                top_num, under_top = stack.pop(), stack.pop()
                stack.append(under_top - top_num)
            elif c == '*': 
                stack.append(stack.pop() * stack.pop())
            elif c == '/': 
                top_num, under_top = stack.pop(), stack.pop()
                stack.append(int(under_top / top_num))
            else: #c = int
                stack.append(int(c))

        return stack[-1]
    