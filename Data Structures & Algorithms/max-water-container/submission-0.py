# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         ovr_max = 0

#         for i in range(len(heights)):


#             for j in range(i, len(heights)):
#                 distance = j-i

#                 min_bar = min(heights[i], heights[j])

#                 curr_water_amt =  min_bar * distance

#                 if (curr_water_amt > ovr_max):
#                     ovr_max = curr_water_amt

#         return ovr_max

# # class Solution:
# #     def maxArea(self, heights: List[int]) -> int:
# #         ovr_max = 0

# #         p1, p2 = 0, len(heights) - 1

# #         while p1 < p2:
# #             curr_max = 0
# #             distance = p2 - p1

# #             min_bar = min(heights[p1], heights[p2])

# #             curr_max = min_bar * distance             
# #             if curr_max > ovr_max:
# #                 ovr_max = curr_max
            

# #             if heights[p1 + 1] > heights[p1]:
# #                 p1 += 1
# #             elif heights[p2 - 1] > heights[p2]:
# #                 p2 -= 1
# #             else:
# #                 return ovr_max



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ovr_max = 0

        p1, p2 = 0, len(heights) - 1

        while p1 < p2:
            min_bar = min(heights[p1], heights[p2])
            curr_max =  min_bar * (p2-p1)

            ovr_max = max(ovr_max, curr_max)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else: #elif heights[p1] < heights[p2] or heights[p2] == heights[p1]
                p1 += 1 
        return ovr_max
