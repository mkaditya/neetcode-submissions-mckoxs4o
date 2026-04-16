class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for prev_course, curr_course in relations:
            graph[prev_course].append(curr_course)
            in_degree[curr_course] += 1
        
        q = deque()
        for idx in range(1, n+1):
            if in_degree[idx] == 0:
                q.append(idx)
        
        semesters = 0
        courses_taken = 0
        while q:
            semesters += 1
            courses_this_semester = len(q)
            for _ in range(courses_this_semester):
                current_course = q.popleft()
                courses_taken += 1

                for dependent_course in graph[current_course]:
                    in_degree[dependent_course] -= 1
                    if in_degree[dependent_course] == 0:
                        q.append(dependent_course)
        return semesters if courses_taken == n else -1