class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_top_temp, stack_top_ind = stack.pop() 
                res[stack_top_ind] = index - stack_top_ind
            stack.append([temperature, index])

        return res