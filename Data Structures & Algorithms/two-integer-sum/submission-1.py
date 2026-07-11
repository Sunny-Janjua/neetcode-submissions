class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict={}

        for i,num in enumerate(nums):
            completele=target-num

            if completele in numDict:
                return [numDict[completele],i]
            
            numDict[num]=i