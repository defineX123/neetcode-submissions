# counting

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord("a")] += 1
            key = tuple(arr)
            groups[key].append(word)
        return list(groups.values())
                    


# sorting
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list) # a dict where any missing key starts as an empty list

#         for word in strs:
#             key = "".join(sorted(word)) # sort, then glue them back into a hashable string
#             groups[key].append(word) # appends word into buckets

#         return list(groups.values())
