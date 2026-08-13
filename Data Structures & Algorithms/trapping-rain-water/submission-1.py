class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        
        while l < r:
            #move the left pointer to the right because we have to find a greater bar on the left side bceause left side's bar is smaller rigt now
            if leftMax < rightMax:
                #move it to the right
                l += 1
                #update the greater bar on the left side
                leftMax = max(leftMax, height[l])

                #now calculate the amount of water above that position
                res += (leftMax - height[l])

            else: # if rightmax and leftmax are equal or leftmax is greater
                r -= 1
                rightMax = max(rightMax, height[r])
                res += (rightMax - height[r])
        
        return res
