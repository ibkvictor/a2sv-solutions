import math
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = -math.inf
        # max_height = -math.inf
        # for i in range(len(height) - 1):
        #     if height[i] < max_height:
        #         continue
        #     for j in range(i + 1, len(height)):
        #         max_height = min(height[j], height[i])
        #         if height[j] < max_height:
        #             continue

        #         max_area = max(min(height[j], height[i]) * (j - i), max_area)

        # return max_area
        
        # i = 0
        # j = len(height) - 1
        # max_height = min(height[j], height[i])
        # max_area = max_height * (j - 1)
        # print(j - i)
        # print(max_height)
        # switch = 0

        # while i < j:
        #     if switch % 2 == 0:
        #         if height[i] <= max_height:
        #             i += 1
        #             continue

        #         else:
        #             switch = 1
        #             max_area = max((min(height[j], height[i]) * (j - i)), max_area)
        #             max_height = min(height[j], height[i])
        #             continue

        #     else:
        #         if height[j] <= max_height:
        #             j -= 1
        #             continue

        #         else:
        #             switch = 0
        #             max_area = max((min(height[j], height[i]) * (j - i)), max_area)
        #             max_height = min(height[j], height[i])
        #             continue

        # return max_area
        i = 0
        j = len(height) - 1
        max_area = -math.inf

        while i < j:
            max_area = max(max_area, (min(height[j], height[i]) * (j - i)))
            if height[i] < height[j]:
                i += 1

            else:
                j -= 1
        return max_area