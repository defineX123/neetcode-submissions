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