class Solution:
    def trap(self, height: List[int]) -> int:
        summ=0
        l,r=0,len(height)-1
        l_max,r_max = height[l],height[r]
        while l<r:
            if height[l]<=height[r]:
                if height[l]<l_max:
                    summ+=l_max-height[l]
                else:
                    l_max=height[l]
                l+=1
            else:
                if height[r]<r_max:
                    summ+=r_max-height[r]
                else:
                    r_max=height[r]
                r-=1

        return summ