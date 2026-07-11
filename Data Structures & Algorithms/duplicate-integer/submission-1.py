class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnumber=set()
        for num in nums:
            if num in newnumber:
                return True
            newnumber.add(num)
        return False
