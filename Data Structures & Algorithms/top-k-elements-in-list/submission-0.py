class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range(len(nums) + 1)] #create arr with len(nums) + 1 sub arrs. + 1 because we want our greatest index to be the len of the array. so 6 arr values, then top index is 6

        #memorize this: way to get frequency of each item to a hashmap!
        for n in nums:
            count[n]  = 1 + count.get(n, 0) #count how many times each number in nums occurs


        for every_number, count in count.items():
            freq[count].append(every_number) #freq is the array holding len(nums)+1 amount of subarrs.
                                
                                # count, which is the frequency of each number in the hashmap, is now the index in the freq list (because smart bucket sort)
                                # every_number, which is the key in the hashmap, is now what we are appending to each frequency's (index) subarr
                                    #so count (the frequency) is the index
                                    # and [nums in sub arr] are the numbers that have that amount of frequency

        res = [] #initalize result arr

        for i in range(len(freq) - 1, 0, -1): #iterating through frequency in descneding order so starting at the top index (which is len(freq) - 1), going to the first index which is 0, indicating descent which is -1
            for n in freq[i]: #since each index has a subarr, we are iterating through each element in the subarr at i index where n represents each element
                res.append(n) #appends the nums in the subarray at i frequency
                
                if len(res) == k: #KEY: it finds k most freq elements by stopping at len(res) because if we want to find 2 most freq elements, then len of the arr we're going to return is going to have 2 values
                    return res #guaranteed to execute
        
#this was O(n) time & space, idk how tho