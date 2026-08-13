class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 

        res = 0
        l, r = 0, len(height) - 1
        leftMax_sofar, rightMax_sofar = height[l], height[r]


        while l < r:
            
            if leftMax_sofar < rightMax_sofar:
                #the height at the position we are calculating canNOt be more than the minimum bar, so disregard the greater bar
                #update the current pointer so we can check if we have a new MAX bar on the left side
                l += 1

                leftMax_sofar = max(leftMax_sofar, height[l])

                #we are ITERATIVELY doing it, so we are adding the amount of water at the CURRENT position
                res += leftMax_sofar - height[l]
            
            elif leftMax_sofar > rightMax_sofar or rightMax_sofar == leftMax_sofar:
                r -= 1
                rightMax_sofar = max(rightMax_sofar, height[r])


                #don't understand HOW
                res += rightMax_sofar - height[r]
        
        return res