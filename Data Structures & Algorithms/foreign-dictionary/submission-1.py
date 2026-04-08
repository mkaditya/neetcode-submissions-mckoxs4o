class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = {c:0 for word in words for c in word}

        for idx in range(1, len(words)):
            w1, w2 = words[idx - 1], words[idx]
            min_len = min(len(w1), len(w2))  

            # very specific condition to problem.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for c_idx in range(min_len):
                if w1[c_idx] != w2[c_idx]:
                    adj[w1[c_idx]].append(w2[c_idx])    
                    indegree[w2[c_idx]] += 1
                    break # only first differen matters
        
        q = deque()
        order = []
        for k in indegree:
            if indegree[k] == 0:
                q.append(k)

        while q:
            c = q.popleft()
            order.append(c)

            for unlocked in adj[c]:
                indegree[unlocked] -= 1
                if indegree[unlocked] == 0:
                    q.append(unlocked)
        
        return "".join(order) if len(order) == len(indegree) else ""

