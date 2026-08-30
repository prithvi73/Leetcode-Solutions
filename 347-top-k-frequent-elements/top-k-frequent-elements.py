class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, freq in freq_map.items():
            buckets[freq].append(number)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                result.append(number)
            if len(result) == k:
                return result

        