class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            listS = list(s)
            listS.sort()
            listT = list(t)
            listT.sort()
            return listS == listT