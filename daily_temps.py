class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #basically looks for the next warmest date and counts everything inbetween
        count = 0
        return_list = []
        for i in range (0, len(temperatures)):
            count = 0
            for j in range(i, len(temperatures)):
                #if it hits a higher temp
                if temperatures[i]<temperatures[j]:
                    return_list.append(count)
                    count = 0
                    break
                # if its a lower temp
                else:
                    count = count+1
                #if it hits the end of the list without higher temp
            if not count == 0:
                return_list.append(0)
                
        #check the last 2 manually:
        print(temperatures[len(temperatures)-1],temperatures[len(temperatures)-2])

        return return_list
       