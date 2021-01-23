
# On Leetcode: https://leetcode.com/problems/network-delay-time/

class Solution(object):
    def build_adj_list(self, times, n):
        """
        Helper method to build an adjacency list which provides a constant-time lookup
        for the nodes of the graph.
        """
        adj_list = {}
        for x in range(1, n + 1):
            adj_list[x] = []
        for time in times:
            src = time[0]
            dst = time[1]
            latency = time[2]
            adj_list[src].append((dst, latency))
        
        return adj_list

    def visit(self, adj_list, k, delay):
        """
        Helper method to implement a visit returning the max delay time experienced 
        propagating over the tree.
        """
        lcl_delay = delay
        for edge in adj_list[k]:
            dst = edge[0]
            latency = edge[1]
            lcl_delay = max(lcl_delay, self.visit(adj_list, dst, delay + latency))
        
        return lcl_delay if lcl_delay > 0 else -1

    def network_delay_time(self, times, n, k):
        """
        The main idea behind the algorith is to search using a deptch first approach
        reporting, for each branch of the graph, systematically the maximum.
        """
        adj_list = self.build_adj_list(times, n)
        
        return self.visit(adj_list, k, 0)

def main():
    s = Solution()

    times = [
        [2, 1, 1],
        [2, 3, 1],
        [3, 4, 1]
    ]
    n = 4
    k = 2
    print(s.network_delay_time(times, n, k))    # 2

    times = [
        [1,2,1]
    ]
    n = 2
    k = 1
    print(s.network_delay_time(times, n, k))    # 1

    times = [
        [1,2,1]
    ]
    n = 2
    k = 2
    print(s.network_delay_time(times, n, k))    # -1

if __name__ == '__main__':
    main()
