class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for curr_word in strs:
            count = [0] * 26
            
            for each_char in curr_word:

                count[ord(each_char) - ord('a')] += 1

            res[tuple(count)].append(curr_word)

        return list(res.values())