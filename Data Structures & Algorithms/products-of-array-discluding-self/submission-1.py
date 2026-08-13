class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        res = []

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num 

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)


        for index, val in enumerate(nums):
            if zero_count == 1:
                if val == 0:
                    res[index] = prod  
                else:
                    res[index] = 0
            else:
                res[index] = (prod//val)  
        
        return res