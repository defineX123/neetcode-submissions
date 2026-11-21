class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        container = {} # or just use defaultdict

        for i in range(len(s)):
            container[s[i]] = container.get(s[i], 0) + 1
            container[t[i]] = container.get(t[i], 0) - 1

        if all(v == 0 for v in container.values()):
            return True
        else: 
            return False

        


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         forS = {}
#         forT = {}

#         for i in s:
#             forS[i] = forS.get(i, 0) + 1

#         for i in t:
#             forT[i] = forT.get(i, 0) + 1

#         return forS == forT




        