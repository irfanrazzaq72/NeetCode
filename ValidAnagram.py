"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}
        for num in range(len(s)):
            countS[s[num]] = 1 + countS.get(s[num],0)
            countT[t[num]] = 1 + countT.get(t[num],0)

        for count in countS:
            if countS[count] != countT.get(count,0):
                return False
        return True

        
