class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for num in count.keys():
            #pushing the (frequency, actual number) to the heap
            # min heap is parent is smallest, and children are bigger
            # min heap arr = left child = parent index * 2, right child = parent * 2 + 1 for 1 based indexing
            #this is probably sorting based on frequency. whichever has the least frequency stays at top?
            
            #top of heap is num with least frequency
            #bottom of heap is num with greater frequencys
            heapq.heappush(heap, (count[num], num))

            # only keep k amount of tuples in the heap, this is the top K frequent elements
            if len(heap) > k:
                heapq.heappop(heap) #remember that elements are added to the bottom. so a number with the least frequency will be added to the bottom/end of the array, then it will be compared with its parents and continue to bubble upwards
            
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

