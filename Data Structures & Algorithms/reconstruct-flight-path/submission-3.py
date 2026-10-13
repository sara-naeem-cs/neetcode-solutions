from functools import cache

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        trips = {} #Our adjacency list
        for ticket in tickets:
            if ticket[0] not in trips:
                trips[ticket[0]] = []
            trips[ticket[0]].append(ticket[1])

        
        res = ["JFK"]

        #@cache
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in trips:
                return False

            temp = list(trips[src])
            for i, v in enumerate(temp):
                trips[src].pop(i)
                res.append(v)

                if dfs(v): return True
                #Undo the added value
                trips[src].insert(i, v)
                res.pop()
            return False
        
        dfs(res[0])
        return res





        

