import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = []
        nums = sorted(nums)
        ln = len(nums)
        prf = [0] * (ln + 1)
        prf[0] = 0
        for i in range(ln):
            prf[i + 1] = prf[i] + nums[i]
        for m in queries:
            l, r = 0, ln - 1
            bstIdx = 0

            bstIdx = bisect.bisect_left(nums, m)
            answer.append(
                abs(prf[bstIdx] - m * (bstIdx))
                + abs((prf[ln] - prf[bstIdx]) - m * (ln - bstIdx))
            )
        return answer
