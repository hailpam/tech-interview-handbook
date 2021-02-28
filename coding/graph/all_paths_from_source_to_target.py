# On Leetcode: https://leetcode.com/problems/all-paths-from-source-to-target/
class Solution(object):
    def visit(self, graph, paths, idx=0, path=[]):
        if not graph[idx]:
            paths.append(list(path))
            paths[-1].append(idx)
            return
        
        for edge in graph[idx]:
            path.append(idx)
            self.visit(graph, paths, edge, path)
            path.pop()

    def all_paths_source_target(self, graph):
        """
        The main idea of this algorithm is to visit recursively the graph,
        as provided, jumping as the edges require. 

        Exeample: [[1,3],[2],[3],[]]
        [1,3]
         ^
          1
            2
              3
                -
        (0,1,2,3)

        [1,3]
           ^
            3
              -
        (0,3)

        According to the reachability, the only two paths are (0,1,2,3) and (0,3).
        """
        paths = []
        self.visit(graph, paths)

        return paths

def main():
    s = Solution()

    graph = [
        [1,2],  # all nodes visitable form 0
        [3],    # all nodes visitable from 1
        [3],    # all nodes visitable from 2
        []      # all nodes visitable from 3
    ]
    print(s.all_paths_source_target(graph))

    graph = [
        [4,3,1],
        [3,2,4],
        [3],
        [4],
        []
    ]
    print(s.all_paths_source_target(graph))

    graph = [
        [1,2,3],
        [2],
        [3],
        []
    ]
    print(s.all_paths_source_target(graph))

    graph = [
        [1,3],
        [2],
        [3],
        []
    ]
    print(s.all_paths_source_target(graph))

if __name__ == '__main__':
    main()
