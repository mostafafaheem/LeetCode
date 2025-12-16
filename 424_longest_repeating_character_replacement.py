class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency, iterator, max_count, left, maxlen = [0] * 26, range(len(s)), 0, 0, 0
        for right in iterator:
            idx = ord(s[right]) - ord("A")
            frequency[idx] += 1
            max_count = max(frequency[idx], max_count)
            if right - left + 1 - max_count > k:
                frequency[ord(s[left]) - ord("A")] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen
