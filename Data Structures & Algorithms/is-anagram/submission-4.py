class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dictS, dictT = {}, {}
            for c in s:
                dictS[c] = dictS.get(c, 0) + 1
            for ch in t:
                dictT[ch] = dictT.get(ch, 0) + 1
            return dictS == dictT
