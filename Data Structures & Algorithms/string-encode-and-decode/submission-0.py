# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         new_str = ''
#         for s in strs:
#             new_str += s
#             new_str += '#'
#         return new_str

#     def decode(self, s: str) -> List[str]:
#         #the key to decoding is knowing which were the original array of strings. how do we know this
#         str_arr = s.split('#')
#         # for i in range (len(str_arr)):
#         #     str_arr[i] = str_arr[i][1:]
#         return str_arr[:-1]        

class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        for i in range(len(strs)):
            enc_str += str(len(strs[i]))
            enc_str += '#'
            enc_str += strs[i]

        return enc_str
    
    # def decode(self, s: str) -> List[str]:
    #     strs = []
    #     for i in range(len(s)):
    #         if s[i] == '#':
    #             str_len = int(s[i-1])
    #         strs.append[s[i+1]:s[i+str_len+1]]
    #     return strs

    # correct one 
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #i is an index

        while i < len(s): #iterate through each char in s
            j = i #initialize another index j
            while s[j] != '#': #while we are still at an integer char
                j += 1 #keep incrementing j til it reaches a # char
            
            str_len = int(s[i:j])

            res.append(s[j+1:j+str_len+1])

            i = j + 1 + str_len # start index at first letter of next word. just happens to be the same as the ending slice because ending slice is exclusive

        
        return res