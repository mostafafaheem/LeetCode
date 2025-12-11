class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return None
        n = len(heights)
        mononxt, monoprev = [], []
        nxt, prev = [n] * n, [0] * n
        iterator = range(n)
        maximum = 0
        for i in iterator:
            while mononxt and heights[mononxt[-1]] > heights[i]:
                nxt[mononxt.pop()] = i
            mononxt.append(i)
        for i in reversed(iterator):
            while monoprev and heights[monoprev[-1]] > heights[i]:
                prev[monoprev.pop()] = i + 1
            monoprev.append(i)
        for i in iterator:
            maximum = max(maximum, (nxt[i] - prev[i]) * heights[i])
        return maximum
