class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #mapping charCount to list of Anagrams
        res = defaultdict(list) #defaultdict() makes all values of the created keys in this dictionary a list. sometimes it needs an import to work. 

        for s in strs:
            count = [0] * 26 #0 for each letter in alphabet, from a-z. so index 0 = the letter a, and index 25 = amount of zs

            for c in s: #c represents each letter in the word s
                #so to increase each letters occurrence at the correct index of letter c
                count[ord(c) - ord("a")] += 1 #finds c's index in the alpabet by subtracting the ascii val of c by the ascii val of a

            res[tuple(count)].append(s) #since res is dict, then we add to the keys' arr value by doing dict_name[key].append(valuetoapp)
            #it adds each word with the same count array pattern to count's arr value to keep track of all words with the same letters
            #in python, keys cant be mutable, so we change count key from being a list to being a tuple

        return list(res.values()) #this returns a list of all of the hashmap's values, which are each their own respective lists of anagrams

        #sometimes u can just say res.values() to return a list of values, but sometimes it .values() returns an view object or something like that