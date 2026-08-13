class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 #longest sequence


        for n in nums:
            #check if n is start of a sequence
            if (n - 1) not in numSet: #remember n is a copy of the actual value in the array, not an index
                length = 0 #initialize length of this sequence
                
                #get each consecutive number and check if it exists in numSet
                while (n + length) in numSet:
                    length += 1 
                
                longest = max(length, longest) #max function takes the greater of the 2 passed parameters. longest is reassinged to current length if current length is greater than longest
        return longest
    