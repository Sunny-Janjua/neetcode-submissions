class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}          # number -> frequency
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]   # index = frequency

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result