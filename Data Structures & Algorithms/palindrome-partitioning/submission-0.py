class Solution:
    def _is_palindrome(self, s:str) -> bool:
        return s == s[::-1]
        
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(idx, path):
            if idx == len(s):
                result.append(path[::])
                return
            
            for next_idx in range(idx+1, len(s)+1):
                next_partition = s[idx:next_idx]
                if self._is_palindrome(next_partition):
                    path.append(next_partition)
                    backtrack(next_idx, path)
                    path.pop()
        backtrack(0, [])
        return result


    