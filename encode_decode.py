class Solution:

    def encode(self, strs: List[str]) -> str:
        #append each string to one using -
        final = ""
        for i in range(0,len(strs)):
            final = final + "-" + strs[i]
        return final

    def decode(self, s: str) -> List[str]:
        #break the string apart based on -
        string = s.split("-") [1:]
        return string
#commit test