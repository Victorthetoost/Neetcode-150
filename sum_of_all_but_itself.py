class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = nums.copy()
        total = 1
        for i in range(0, len(nums)):
            total = total*nums[i]
        for i in range(0,len(nums)):
            print(i, nums[i])
            if nums[i] != 0:
                print(nums[i])
                final[i] = int(total/nums[i])
                print("final", final[i])
            else:
                print("i = ", i)
                print("not doing the normal thing")
                totall = 1
                for j in range (0,len(nums)):
                    print(nums)
                    if i != j:
                        totall *= nums[j]
                        print(totall)
                final[i] = totall
                        
        return final