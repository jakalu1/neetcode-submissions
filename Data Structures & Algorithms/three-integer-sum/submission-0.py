
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        #first loop for the first_value

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #so this skips having a duplicate first number. it first makes sure i > 0 so that the i-1 operation doesn't cause an error
                                        # then it checks if our current value a is = to the previous value in the prev iteration nums[i-1]
                continue #skip this iteration
                
            l, r = i+1, len(nums) - 1

            while l < r:
                # i != l != r and nums[]
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 #update one of the pointers, because the conditions up there will make sure that there is no duplicates with the other indices
                    while nums[l] == nums[l-1] and l < r: 
                        l += 1
        return res