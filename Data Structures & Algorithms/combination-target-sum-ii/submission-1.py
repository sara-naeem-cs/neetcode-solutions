
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        candidates.sort()

        def dfs(i, currSoln, currTotal):
            if currTotal == target:
                res.add(tuple(sorted(currSoln))) #Sort list and add to result
                return
            if currTotal > target or i >= len(candidates):
                return

            
            #First try it with the new candidate:
            currSoln.append(candidates[i])
            dfs(i+1, currSoln, currTotal+candidates[i])

            #Now pop it out and try without this number:
            currSoln.pop()

            dfs(i+1, currSoln, currTotal)

        dfs(0, [], 0)

        returnAnswer = []

        for tup in res:
            returnAnswer.append(list(tup))


        return returnAnswer