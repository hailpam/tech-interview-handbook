# On Leetcode: https://leetcode.com/problems/exam-room/

class ExamRoom(object):
    def __init__(self, n):
        self.seats = [0 for _ in range(n)]
        self.nr_seats = len(self.seats)
        self.last_seat = -1
    
    def search_seat(self, l_idx, r_idx):
        if r_idx <= l_idx:                              # definitely, not found it
            return -1
        
        pivot = int((r_idx - l_idx) / 2)
        if self.seats[l_idx + pivot] == 0:
            self.seats[l_idx + pivot] = 1
            return l_idx + pivot
        
        l_pivot = self.search_seat(l_idx, pivot)
        if l_pivot != -1:                               # search left subarray
            return l_pivot
        r_pivot = self.search_seat(pivot + 1, r_idx)
        if r_pivot != -1:                               # search right subarray
            return r_pivot

    def seat(self):
        first = self.seats[0] != 0
        if not first:
            self.seats[0] = 1
            return
        last = self.seats[-1] != 0
        if not last:
            self.seats[-1] = 1
            return
        
        if self.last_seat == -1:                        # got to go wild on the array
            self.last_seat = self.search_seat(0, self.nr_seats - 1)
        else:                                           # got to drive the search, according to the distance
            # the search should always happend in the subarray with the maximum
            # availability in terms of slots so to maximize the distance between
            # the seats
            if self.nr_seats - self.last_seat - 2 > self.last_seat:
                self.last_seat = self.search_seat(self.last_seat + 1, self.nr_seats - 1)
            else:
                self.last_seat = self.search_seat(0, self.last_seat)

    def leave(self, p):
        if p < len(self.seats):
            self.seats[p] = 0

def main():
    e = ExamRoom(10)
                        # [0 0 0 0 0 0 0 0 0 0]
    e.seat()            # at 0, no one else already sitting
    print(e.seats)
                        # [1 0 0 0 0 0 0 0 0 0]
    e.seat()            # at 9, to maximize the distance
    print(e.seats)
                        # [1 0 0 0 0 0 0 0 0 1]
    e.seat()            # at 4, between 0 and 9
    print(e.seats)
                        # [1 0 0 0 1 0 0 0 0 1]
    e.seat()            # at 2, between 0 and 4
    print(e.seats)
                        # [1 0 1 0 1 0 0 0 0 1]
    e.leave(4)          # free up seat 4
    print(e.seats)
                        # [1 0 1 0 0 0 0 0 0 1]
    e.seat()            # at 5, between 2 and 9
    print(e.seats)
                        # [1 0 1 0 0 1 0 0 0 1]

if __name__ == '__main__':
    main()
