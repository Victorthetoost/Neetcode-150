class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # goes through the list
        # when it sees a number smaller than it, it stops
        # goes to the left same thing
        # saves sum if its the biggest
        biggest = 0
        for i in range(0,len(heights)):
            # right:
            j = i
            area = 0
            while j < len(heights):
                if heights[j] >= heights[i]:
                    area = area + heights[i]
                else: break
                j = j + 1
            j = i - 1
            #left:
            while j >= 0 :
                if heights[j] >= heights[i]:
                    area = area + heights[i]
                else: break
                j = j - 1
            if area > biggest:
                biggest = area
        return biggest

