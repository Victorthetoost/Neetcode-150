class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dictionary that updates the count for each number
        # look at all the counts and select the n top oknes
        dictionary = {}
        for num in nums:
            if num in dictionary:
                total = dictionary.get(num)
                total +=1
                dictionary.update({num:total})
            else:
                dictionary.update({num:1})
        sorteds = dict(sorted(dictionary.items(), key=lambda item: item[1],reverse = True))
        returns = []
        print(sorteds)
        for key in sorteds:
            print(key)
            if k == 0:
                break
            returns.append(key)
            k = k-1
        return returns
