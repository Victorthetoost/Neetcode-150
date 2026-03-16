class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove spaces
        s = s.replace(" ","")
        s = s.replace("?","")
        s = s.replace("'","")
        s = s.replace(",","")
        s = s.replace(".","")
        s = s.replace(":","")
        s = s.lower()
        print(s)
        if len(s) == 2:
            if s[1] == s[0]:
                return True
            return False
        if len(s) == 1:
            return True
        #finds the middle
        #one pointer goes left
        #other goes right from middle
        # if not same return false
        if len(s)%2 == 0:
            middle = int(len(s)/2)
            for i in range(0,middle):
                if not s[middle+i] == s[middle-i-1]:
                    print("not the same:",s[middle+i], s[middle-i-1])
                    return False
        else:
            print("odd?")
            middle = int(len(s)/2)
            print(middle)
            for i in range(0,middle+1):
                print(s[middle+i],s[middle-i], middle, s[middle], i)
                if not s[middle+i] == s[middle-i]:
                    print("not the same:",s[middle+i], s[middle-i])
                    return False
        return True

        