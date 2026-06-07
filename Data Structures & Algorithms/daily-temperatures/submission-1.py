class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temps -> temp[i] = the daily temp on the ith day
        # result = result[i] days of ith day before the warmer temp appers in the future 
        # stack = []
        # add to the stack until a bigger number += 1 then on res append the number

        stack = []
        res = [0] * len(temperatures)

        for temp in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[temp]:
                smallerTemp = stack.pop()
                res[smallerTemp] = temp - smallerTemp 
            stack.append(temp)
        return res