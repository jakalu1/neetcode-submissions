
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #giving each value an initial value of 1

        prefix = 1 #first doing prefixes

        #so what this is doing is appending all of the prefix values to res by setting res[i] = to prefix, then updating the prefix var to include the numbers in num as the product
            #so it updates res[i] as prefix after the product is taken
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        #so what this is doing is a reverse loop starting at the end and going to the beginning
        #it *= the existing prefixes at res[i] because we want to multiply our postfix that we get from the iteration prior (we used the same algorithm that we did for our prefixes)
        postfix = 1
        for i in range(len(nums) -1, -1,-1): #why is the stop index -1? because its exclusive
            res[i] *= postfix
            postfix *= nums[i]


        return res #now this holds the array of all the values of the product of the numbers except itself which was our goal, done by multiplying the prefixes and the postfixes