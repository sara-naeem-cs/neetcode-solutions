class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #First sort
        people.sort()
        #Pointers on both ends
        l = 0
        r = len(people)-1
        #boats = []
        num_boats = 0

        #See if r + l is < limit, id not then boat with one person
        while l < r:
            if people[l]+people[r] <= limit:
                #The boat has both people
                boats.append([people[l], people[r]])
                num_boats = num_boats + 1
                r = r - 1
                l = l + 1
            else:
                #Only right person gets a boat
                r = r - 1
                num_boats = num_boats + 1
        
        return num_boats



