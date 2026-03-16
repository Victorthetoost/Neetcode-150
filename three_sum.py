class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #like 2 sum but 3 pointers jumping around
        solutions = [[]]
        solutions.pop()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        sol = [nums[i],nums[j],nums[k]]
                        sol.sort()
                        if not sol in solutions:
                            solutions.append(sol)

        return solutions