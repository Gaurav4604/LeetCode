class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) <= 1):
            return len(s)
        else:
            pointer_start = 0
            pointer_end = 0
            max_len = 0
            char_set = set([])
            while(pointer_end < len(s)):
                if not s[pointer_end] in char_set:
                    char_set.add(s[pointer_end])
                    pointer_end += 1
                    max_len = max(len(list(char_set)), max_len)
                else:
                    char_set.remove(s[pointer_start])
                    pointer_start += 1
            return max_len

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))