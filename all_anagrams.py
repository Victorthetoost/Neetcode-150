class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s,t): 
            print("s",s,"t",t)
            for char in s:
                if char in t:
                    t = t.replace(char,"",1)
                    s = s.replace(char,"",1)

            if s or t:
                return False
            return True


        #have a return list and just append the list of anagrams to it
        # do this for every word and remove words after runnign to 
        # prevent duplicates
        return_list = []
        while strs:
            
            for i in range(0,len(strs)):
                temp = []
                if strs[i] == "fuck":
                    continue
                for j in range(i+1,len(strs)):
                    print(is_anagram(strs[i],strs[j]), strs[i], strs[j])
                    if is_anagram(strs[i],strs[j]) and not strs[j] == "fuck":
                        temp.append(strs[j])
                        print(temp)
                        strs[j] = "fuck"
                temp.append(strs[i])
                strs[i] = "fuck"
                return_list.append(temp)
            strs.remove("fuck")
        if return_list == []:
            return [[""]]
        return return_list

        