class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array, then check for the largest consecutive 
        # +1s
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)
        Mcount = 0
        Ccount = 0
        
        if not nums:
            return 0
        current_val = nums[0]
        for i in range(1, len(nums)):
            print(nums[i]-current_val, current_val)
            if abs(nums[i] - current_val) == 1:
                print("got there")
                Ccount = Ccount+1
                current_val = nums[i]
            else:
                Ccount = 0
                current_val = nums[i]
            print("counts",Ccount, Mcount)
            if Ccount > Mcount:
                Mcount = Ccount
        return Mcount + 1
