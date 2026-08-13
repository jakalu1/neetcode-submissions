class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: #here we have to handle the case where there is nothing in the list
            return 0
        res = 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r] #initially set it to the beginning nums that the two pointers are pointing to

        while l < r:
            if leftMax < rightMax: #increment the left pointer by 1 if the left max is smaller
                l += 1
                leftMax = max(leftMax, height[l]) #height[l] is current left pointer, while leftMax is the max so FAR on the left side

                res += leftMax - height[l] #dont have to check if its negative because it would never be negative because we are updating the leftMax BEFORE doing this subtraction. so if leftMax is already the greater number, then leftMax will stay greater and we wont get a negative number. if height[l] is greater, then it will update to leftMax and we will get 0 at most
            else:  #rightMax < leftMax: #if the right max is smaller than the leftMax or if they are == increment the right pointer by 1
                r -= 1
                rightMax = max(rightMax, height[r])

                res += rightMax - height[r]

        return res