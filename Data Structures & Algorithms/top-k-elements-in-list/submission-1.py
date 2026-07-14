class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return heapq.nlargest(k, counter.keys(), key = counter.get)

                