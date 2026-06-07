class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res prefilled with 0s — days with no warmer future day stay 0
        stack = []
        res = [0] * len(temperatures)

        # iterate by index so we can calculate distance between days
        for temp in range(len(temperatures)):
            # while stack has indices AND current temp is warmer than top of stack
            # keep popping and resolving — one warmer day can resolve multiple past days
            while stack and temperatures[stack[-1]] < temperatures[temp]:
                smallerTemp = stack.pop()
                # smallerTemp is the earlier (cooler) day, temp is the later (warmer) day
                res[smallerTemp] = temp - smallerTemp
            # push current index — it's still waiting for something warmer
            stack.append(temp)

        # any indices still in stack never found a warmer day, res stays 0 for them
        return res