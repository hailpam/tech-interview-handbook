
# On Leetcode: https://leetcode.com/problems/task-scheduler/

class Solution(object):
    def get_next_max(self, frequency):
        """
        Helper method to retrieve the next max frequency item from the mapping.

        NOTE this might be managed with a priority queue as well to avoid
        a systematic linear search.
        """
        max_cnt = 0
        max_el = None
        for item in frequency:
            if frequency[item] > max_cnt:
                max_el = item
                max_cnt = frequency[item]
        
        del frequency[max_el]

        return max_el, max_cnt

    def build_schedule(self, max_el, max_cnt, n):
        """
        Helper method to build the most recurrent tasks interleaved by idle slots.
        """
        schedule = []
        while max_cnt > 1:
            schedule.append(max_el)
            for _ in range(n):
                schedule.append('_')
            max_cnt -= 1
        schedule.append(max_el)

        return schedule

    def is_idle_slot(self, idx, schedule):
        """
        Helper function to check whether the right side is equale to the left side.
        """
        if schedule[idx + 1] != '_':
            right = []
            i, j = idx + 1, idx - 1
            while True:
                if schedule[i] == '_' or i >= len(schedule) - 1:
                    break
                right.append(schedule[i])
                i += 1
            left = []
            while True:
                if schedule[j] == '_' or j >= 0:
                    break
                left.schedule(schedule[j])
                j -= 1
            if not left and not right:
                return False
            
            return ''.join(right) == ''.join(left[::-1])    # got same sequence, got to pause
        
        return False                                        # got to continue

    def fillup_schedule(self, max_el, max_cnt, schedule):
        """
        Helper function to fill up the schedule according to the scheduling rules.
        """
        if '_' in schedule:
            for idx, slot in enumerate(schedule):
                if slot == '_' and max_cnt > 0:
                    if max_el != schedule[idx - 1] and not self.is_idle_slot(idx, schedule):
                        schedule[idx] = max_el
                        max_cnt -= 1
        for _ in range(max_cnt):
            schedule.append(max_el)

    def find_least_interval(self, tasks, n, debug=True):
        """
        To disambiguate, the main idea of this algorithm is to find an efficient ordering
        of the tasks.
        Two similar tasks need to be spaced by an idle time which is defined and reported. 

        The main idea to solve this problem consists in detemining the most recurrent tasks
        and start scheduling those with idle intervals. Once done, it is possible to fit the
        remaining taks into the idle slots. A typical slots fitting problem.

        Example: AAABBB, 2 -> 8
        step 0:
        A _ _ A _ _ A

        step 1:
        A B _ A B _ A B
        """
        frequency = {}
        for task in tasks:                                      # got to count the frequency
            if task not in frequency:
                frequency[task] = 0
            frequency[task] += 1
        
        max_el, max_cnt = self.get_next_max(frequency)
        schedule = self.build_schedule(max_el, max_cnt, n)      # got to prepare the schedule

        if debug:
            print(schedule)

        while len(frequency) > 0:
            max_el, max_cnt = self.get_next_max(frequency)
            self.fillup_schedule(max_el, max_cnt, schedule)     # got to fill up the schedule

        if debug:
            print(schedule)

        return len(schedule)

def main():
    s = Solution()

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(s.find_least_interval(tasks, n))  # 7

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    print(s.find_least_interval(tasks, n))  # 6

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(s.find_least_interval(tasks, n))  # 16

if __name__ == '__main__':
    main()
