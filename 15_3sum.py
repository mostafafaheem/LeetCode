class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i, numm in enumerate(nums):
            if i>0 and nums[i-1] ==numm:
                continue
            l, r= i + 1, len(nums) -1
            while l<r:
                summ = nums[l] + nums[r] + numm
                if summ > 0:
                    r -= 1
                elif summ<0:
                    l+=1
                else:
                    answer.append([nums[l] , nums[r],numm])
                    l+=1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
        return answer