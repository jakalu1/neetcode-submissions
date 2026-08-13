class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set, longest = set(nums), 0
        
        for num in num_set:
            if (num-1) not in nums:
                length = 1
                while (num + length) in num_set:
                    length += 1

                longest = max(length, longest)
    
        return longest