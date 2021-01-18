
# On Leetcode: https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter(object):
    def __init__(self):
        self.pings = []

    def ping(self, t):
        self.pings.append(t)
        
        lower_bound = t - 3000              # by default, upper bound is always t as it's monotonically increasing
        while True:                         # using a list as a queue, remove the first inserted
            if self.pings[0] < lower_bound:
                self.pings.pop(0)
            else:
                break                       # got to break as the ping if within the interval
        
        return len(self.pings)


def main():
    rc = RecentCounter()

    print(rc.ping(1))      # requests = [1], range is [-2999,1], return 1
    print(rc.ping(100))    # requests = [1, 100], range is [-2900,100], return 2
    print(rc.ping(3001))   # requests = [1, 100, 3001], range is [1,3001], return 3
    print(rc.ping(3002))   # requests = [1, 100, 3001, 3002], range is [2,3002], return 3

if __name__ == '__main__':
    main()
