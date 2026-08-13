class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_elems_map = dict()

        for index, curr_val in enumerate(nums):
            if (target - curr_val) in prev_elems_map:
                return [prev_elems_map[target-curr_val], index]
            else:
                prev_elems_map[curr_val] = index
            
