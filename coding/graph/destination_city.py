
# On Leetcode: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution(object):
    def destination_city_by_dest(self, paths, dest=paths[0][1]):
        """
        Follows recursively linking an initial destination to the source, if any.

        New York -> Lima -> Sao Paulo

        It returns upon not finding any match for Sao Paulo (base case).
        """
        for path in paths:
            if path[0] == dest:
                return self.destination_city_follow(self, path, path[1])
        
        return dest

    def destination_city_by_idx(self, paths, idx=0):
        """
        Inspects recursively linking an initial destination to the source, if any.

        B -> C -> A

        It returns up not finding any match for Sao Paulo (base case).
        """
        dest = paths[idx][1]
        for path in paths:
            if path[0] == dest:
                return self.destination_city(paths, idx + 1)
        
        return dest

def main():
    s = Solution()

    paths = [
        ["London","New York"],
        ["New York","Lima"],
        ["Lima","Sao Paulo"]
    ]
    print(s.destination_city_by_idx(paths))
    print(s.destination_city_by_dest(paths))

    paths = [
        ["B","C"],
        ["D","B"],
        ["C","A"]
    ]
    print(s.destination_city_by_idx(paths))
    print(s.destination_city_by_dest(paths))

    paths = [
        ["A","Z"]
    ]
    print(s.destination_city_by_idx(paths))
    print(s.destination_city_by_dest(paths))

if __name__ == '__main__':
    main()
