class Solution:
    def minMoves(self, nums: List[int]) -> int:

        sol = 0
        mn = min(nums)
        for nm in nums:
            sol +=  nm - mn
        return sol