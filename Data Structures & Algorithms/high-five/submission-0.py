class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        all_scores = defaultdict(list)

        for item in items:
            student_id, score = item
            heapq.heappush(all_scores[student_id], score)
            if len(all_scores[student_id]) > 5:
                heapq.heappop(all_scores[student_id])
        
        solution = []
        for student_id in sorted(all_scores.keys()):
            total = sum(all_scores[student_id])
            solution.append([student_id, total // 5])

        return solution
        

