class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(set(s))
        mpp = set()
        p1, p2, maxlen = 0, 0, 0
        while p2 < len(s) and p1 <= p2:
            while s[p2] in mpp:
                mpp.remove(s[p1])
                p1 += 1
            mpp.add(s[p2])
            maxlen = max(maxlen, p2 - p1 + 1)
            p2 += 1
        return maxlen
