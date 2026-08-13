class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
        #once nums is greater than 0, everything after it is also positive and greater than 0 since nums is sorted
            if nums[i] > 0:
                break
            
        #this duplicate check makes sure theres no duplicates among the fixed numbers
            #checks the i > 0 to make sure that this isn't the beginning of the array
            #we don't want to compare this when i is 0!
            if i > 0 and nums[i] == nums[i-1]:
                continue

            fixed = nums[i]
            l = i+1
            r = len(nums) - 1


            while (l < r):
                sums = fixed + nums[l] + nums[r]
                if (sums == 0):
                    res.append([fixed, nums[l], nums[r]])
                    #move left and right inwards to skip duplicates but keep fixed ones the same
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif (sums < 0):
                    l += 1
                else: # (sums > 0):
                    r -= 1
        return res