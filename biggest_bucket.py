class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #goes through one by one and calculates the volume between any 2 things
        maxx = 0
        for i in range (0,len(heights)):
            for j in range(i+1,len(heights)):
                smallest = min(heights[i],heights[j])
                print(smallest)
                if smallest*(j-i) > maxx:
                    maxx = smallest*(j-i)
                    print("smallest, distance",smallest, j-i)
        return maxx