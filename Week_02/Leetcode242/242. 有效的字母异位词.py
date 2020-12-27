#!/usr/bin/env python
# solution1 hash table
class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        for i in range(s):
            counts[ord(s[i]) - ord("a")] += 1 # ord():Given a string representing one Unicode character,
                                              # return an integer representing the Unicode code point of
                                              # that character.
            counts[ord(t[i]) - ord("a")] -= 1
        for i in counts:
            if i != 0:
                return False
        return True
# time:O(n) n is the length of s. Space:O(S) S为字符集大小，此处 S=26S=26。
