class Solution:
    def maxArea(self, height: List[int]) -> int:
        # for i, h in enumerate(height):
        max_area = -inf
        l, r = 0, len(height) - 1
        while l < r:
            # awel w akher atwal lines?
            # msh shart, momken el vertical distance teb'a consequential aktar
            # only proceed law next line atwal?
            max_area = max(min(height[l], height[r]) * (r - l), max_area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area
