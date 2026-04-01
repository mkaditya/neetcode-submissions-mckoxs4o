class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
       res = [0] * len(temps)
       stack = []

       for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                temp_idx = stack.pop() 
                res[temp_idx] = i - temp_idx
            stack.append(i)
       return res