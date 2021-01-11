
# On Leetcode: https://leetcode.com/problems/course-schedule/

class Solution(object):
    def visit(self, visiting, prereq, prereqs):
        """
        Time Complexity: ~O(N^2 + M), where N is the number of prerequisites and M is the number of courses
        Space Complexity: ~O(M), where M is the number of courses

        An optimization for this algorithm might leverage an adjacency list with O(1) access
        reducing the looping on prerequisites, tradding off ~O(N) space.
        """
        course = prereq[0]
        dep = prereq[1]
        if dep in visiting: # if it's the case, there is a loop (pointing back on the path)
            return False
        
        visiting.append(course)
        for prereq in prereqs:
            if prereq[0] == dep:
                if not self.visit(visiting, prereq, prereqs):
                    return False
        visiting.pop()
        
        return True

    
    def can_finish(self, num_courses, prereqs):
        """
        Having a list of edges, the algorithm should detect cycles: e.g. to take
        exam #1 we need to take exame #0 first, and a dependency of exam #0 on 
        exame #1 might reveal a cycle.
        The solution then should find the topological order. If none, then it cannot
        be finished.
        """
        visiting = []
        for prereq in prereqs:
            if not self.visit(visiting, prereq, prereqs):
                return False

        return True

def main():
    s = Solution()

    num_courses = 2
    prereqs = [
        [1, 0]
    ]
    print(s.can_finish(num_courses, prereqs))

    num_courses = 2
    prereqs = [
        [1, 0], 
        [0, 1]
    ]
    print(s.can_finish(num_courses, prereqs))

    num_courses = 3
    prereqs = [
        [1, 0],
        [2, 1]
    ]
    print(s.can_finish(num_courses, prereqs))

    num_courses = 3
    prereqs = [
        [1, 0],
        [2, 1],
        [2, 0]
    ]
    print(s.can_finish(num_courses, prereqs))

if __name__ == '__main__':
    main()
