class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(0,0,n,[],res)
        return res

    def backtrack(self, open_count:int, closed_count:int, n:int, stack:List[str], res:List[str]):
        if open_count == closed_count == n:
            res.append("".join(stack))
            return res
        
        if open_count < n:
            stack.append("(")
            self.backtrack(open_count + 1 , closed_count, n, stack, res)
            stack.pop()
        
        if closed_count < open_count:
            stack.append(")")
            self.backtrack(open_count, closed_count + 1, n , stack, res)
            stack.pop()
