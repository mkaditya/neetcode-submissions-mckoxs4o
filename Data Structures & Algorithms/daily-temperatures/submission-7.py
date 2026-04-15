class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        wait_list = []
        result = [0] * len(temps)
        for idx, temp in enumerate(temps):
            while wait_list and wait_list[-1][1] < temp:
                waited_idx = wait_list.pop()[0]
                result[waited_idx] = idx - waited_idx
            wait_list.append((idx, temp))
        return result

                
