
# On Leetcode: https://leetcode.com/problems/course-schedule/

class Solution(object):
    def visit(self, visiting, prereq, prereqs):
        course = prereq[0]
        dep = prereq[1]
        if dep in visiting:
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
