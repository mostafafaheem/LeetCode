class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefmax,sufmax ,curmax,summ= [0]*n,[0]*n,-1,0
        
        for i in range(n):
            curmax = max(curmax, height[i])
            prefmax[i] = curmax
        curmax = -1
        for i in reversed(range(n)):
            curmax = max(curmax,height[i])
            sufmax[i]=curmax
        for i in range(n):
            summ+=min(prefmax[i],sufmax[i])-height[i]

        return summ