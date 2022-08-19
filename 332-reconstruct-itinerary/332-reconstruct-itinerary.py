class Solution(object):
    """  """
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        self.visitBitmap = {}

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False]*len(itinerary)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)

        return self.result


    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         ticket_dict = {}
#         for ticket in tickets:
#             if ticket[0] not in ticket_dict:
#                 ticket_dict[ticket[0]] = [ticket[1]]
#             else:
#                 ticket_dict[ticket[0]].append(ticket[1])
#         print(ticket_dict)
#         res = []
#         def dfs(node):
#             res.append(node)
#             if node not in ticket_dict:
#                 return res
#             print(res)
#             print(ticket_dict)
            
#             if len(ticket_dict[node]) == 0:
#                 return res
#             else:
#                 print("sort", [ticket_dict[node]].sort())
#                 min_node = min(ticket_dict[node])
#                 print(min_node)
#                 ticket_dict[node].remove(min_node)
#                 print(ticket_dict)
#                 dfs(min_node)
#         dfs('JFK')
#         print(res)
#         return res
            
            