class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #remove characters from the other, if there are duplicates or characters that
        #dont exist, then return false
        for char in s:
            if char in t:
                t = t.replace(char,"",1)
                s = s.replace(char,"",1)

        if s or t:
            return False
        return True