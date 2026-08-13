# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     if nums[i] > nums[j]:
#                         return [j, i]
#                     else:
#                         return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums): #i is each index and n is each value
            diff = target - n #n is the value
            if diff in prevMap: #checks if diff is one of the prevMap's keys. remember the hashmap is actual num: index
                return [prevMap[diff], i] #prevMap[diff] get's diff's index and i is our current vals index. this is naturally index ascending order because lesser indexes are added to the prevMap first
            prevMap[n] = i
            