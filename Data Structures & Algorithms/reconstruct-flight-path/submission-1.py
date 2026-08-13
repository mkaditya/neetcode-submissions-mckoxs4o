class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj_list = defaultdict(list)
        for ticket in tickets:
            adj_list[ticket[0]].append(ticket[1])
        
        for src in adj_list:
            adj_list[src].sort(reverse=True)

        path = ["JFK"]
        res = []

        while path:
            curr = path[-1]
            if not adj_list[curr]:
                res.append(path.pop())
            else:
                path.append(adj_list[curr].pop())
        
        return res[::-1]



        