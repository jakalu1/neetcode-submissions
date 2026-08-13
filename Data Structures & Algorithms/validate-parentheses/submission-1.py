class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s:
            #first check if it is a closing parentheses, if it is...
            if char in closeToOpen:

                #check if there are open parentheses in the stack, 
                #and check if that open parentheses at the top of the stack is equal to the KEY of the closed parentheses
                #key of the closed parentheses ) = ( equals that <<
                #if ( is at the top of the stack, and current char is ) then key of ) => (
                #so ( == (
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                #if that equality doesn't work, then its not a match, return false for the whole list
                else:
                    return False

            #if its an OPENing parentheses, add it to the stack
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
        
