class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # will store indices

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i  
            else:
                res[i] = 0
            
            stack.append(i)
        
        return res