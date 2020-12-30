
# On Leetcode: https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def get_key(self, s):
        return ''.join(sorted(s))

    def group_anagrams(self, strs):
        grouping = {}
        for s in strs:
            key = self.get_key(s)
            if key not in grouping:
                grouping[key] = []
            grouping[key].append(s)

        groups = []
        dedup = set()
        for s in strs:
            key = self.get_key(s)
            if key not in dedup:
                groups.append(grouping[key])
                dedup.add(key)
            
        return groups

def main():
    x = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(x.group_anagrams(strs))
    strs = [""]
    print(x.group_anagrams(strs))
    strs = ["a"]
    print(x.group_anagrams(strs))

if __name__ == '__main__':
    main()
