# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if sorted(s) == sorted(t):
#             return True
#         return False

#traversing both lists once
#O(1) space complexity is where the extra space created is constant no matter how big arr sizes
#start time 8:26
#end time: 

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         hash_map_s = {}
#         hash_map_t = {}

#         for each_letter in s:
#             if each_letter in hash_map_s:
#                 hash_map_s[each_letter] += 1
#             else:
#                 hash_map_s[each_letter] = 1
#         print("Hash Map S:", hash_map_s)

#         for each_letter in t:
#             if each_letter in hash_map_t:
#                 hash_map_t[each_letter] += 1
#             else:
#                 hash_map_t[each_letter] = 1
#         print("Hash Map T: ", hash_map_t)

#         if hash_map_s == hash_map_t:
#             return True
#         else:
#             return False
            
#Leetcode's solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check length of both strs first
        if len(s) != len(t):
            return False

        countS, countT = {}, {} #create 2 hashmaps

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #key: s[i], value: 1 + existing value. if no existing value, 0 is default value

            countT[t[i]] = 1 + countT.get(t[i], 0)

        for each_key in countS:
            if countS[each_key] != countT.get(each_key, 0): #use get() to throw default value in case key doesn't exist in countT
                return False
        return True
