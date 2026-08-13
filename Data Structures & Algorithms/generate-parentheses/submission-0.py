class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add a parenthesis if open < n
        #only add a closing parenthesis if closing < open
        #only valid IFF closing == open == n:

#we are doing this recursively & defining a recursive function that creates a valid permutation?


        stack = [] #holds all our parentheses chars
        res = [] #which is going to have our list of valid permutations


        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                res.append("".join(stack)) #join every char from our stack together as a str
                return #because this above is our base case
            
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closedCount)

                stack.pop() #why are we doing this?

            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)

                stack.pop() #why are we doing this? 

        backtrack(0, 0)

        return res
    
