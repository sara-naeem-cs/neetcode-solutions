class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxProd = 1
        minProd = 1

        for num in nums:
            if num == 0:
                #Reset max and min prods to 1:
                maxProd = 1
                minProd = 1
            else:
                tmp = maxProd
                maxProd = max(num, maxProd*num, minProd*num)
                minProd = min(num, tmp*num, minProd*num)
                res = max(res, maxProd) #this is global max value
        
        return res


        