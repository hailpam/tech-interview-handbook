# On Leetcode: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution(object):
    def nr_days(self, events):
        """
        Determine the number of days available to be used in distributing the events.
        """
        return max(events)[1]                               # determine the days available

    def max_events(self, events):
        """
        The main idea behind the algorithm is to dispose the events over the days
        using the lower and upper bounds, with the latter as fallback.

        Example: [[3,4], [1,2], [2,3], [1,2]]

            sorted [[1,2], [1,2], [2,3], [3,4]]
            days   [None, None, None, None]
        
            [1,2] -> [[1,2], None, None, None
            [1,2] -> [[1,2], [1,2], None, None]
            [2,3] -> 2 is busy, so go on 3 -> [[1,2], [1,2], [2,3], None]
            [3,4] -> 3 is busy, so go on 4 -> [[1,2], [1,2], [2,3], [3,4]]
        
        In case of busy slot, it falls back using the second end time and tries to
        fit with the respective day.
        """
        days = [None for _ in range(self.nr_days(events))]  # available days

        events.sort()                                       # sort in ascending order, first events first

        attendance = 0
        for event in events:                                # fit events with respective days
            if not days[event[0] - 1]:
                days[event[0] - 1] = event
                attendance += 1
                continue
            if not days[event[1] - 1]:
                days[event[1] - 1] = event
                attendance += 1
                continue
        
        return attendance

def main():
    s = Solution()

    events = [[1,2],[2,3],[3,4]]
    print(s.max_events(events))     # 3

    events= [[1,2],[2,3],[3,4],[1,2]]
    print(s.max_events(events))     # 4

    events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    print(s.max_events(events))     # 4

    events = [[1,100000]]
    print(s.max_events(events))     # 1

    events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    print(s.max_events(events))     # 7

if __name__ == '__main__':
    main()
