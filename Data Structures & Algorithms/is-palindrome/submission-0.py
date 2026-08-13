# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #remove spaces & all non alpha and make s.lower()
#         # s = s.lower() #time complexity for this function?
#         newS = []

#         for char in s:
#             if char.isalnum():
#                 newS.append(char.lower())
#         newS = ''.join(newS) #this is joining all elements of the list into a string with '' between them

#         p1 = 0
#         p2 = len(newS) - 1
#         while(p1 != p2):
#             if newS[p1] != newS[p2]:
#                 return False
#             p1 += 1
#             p2 -= 1
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

    def alphaNum(self, c: str) -> bool:
        #since ascii characters are contiguous (meaning a is one value less than b), we can manually check if our char is in between A Z, a z, and 0-9 ascii vals, if it is,then it is alpha num
        return ((ord('A') <= ord(c) <= ord('Z')) or
        (ord('a') <= ord(c) <= ord('z')) or
        (ord('0') <= ord(c) <= ord('9')))