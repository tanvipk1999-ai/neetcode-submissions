class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                t = stack.pop()
                res[t] = i-t
            stack.append(i)
        return res