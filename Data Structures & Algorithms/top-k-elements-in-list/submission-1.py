class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_dict = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res