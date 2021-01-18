
# On Leetcode: https://evelynn.gitbooks.io/google-interview/content/moving_average_from_data_stream.html

class MovingAverage(object):
    """
    A naive implementation based on a queue. An alternative implementation
    may be based on a circular list (it keeps erasing the oldest elements).
    """

    def __init__(self, win_size=5):
        self.win_size = win_size
        self.queue = []
    
    def next(self, val):
        self.queue.append(val)
        if len(self.queue) > self.win_size:     # got to remove the oldest ones
            how_many = len(self.queue) - self.win_size
            for _ in range(how_many):
                self.queue.pop(0)
        elem_sum = 0
        for elem in self.queue:
            elem_sum += elem
        
        return elem_sum / len(self.queue)

def main():
    ma = MovingAverage()

    print(ma.next(1))      # 1
    print(ma.next(10))     # (1 + 10) / 2 = 5.5
    print(ma.next(3))      # (1 + 10 + 3) / 3 = 4.6
    print(ma.next(5))      # (10 + 3 + 5 + 1) / 4 = 4.75
    print(ma.next(11))     # (11 + 5 + 3 + 10 + 1) / 5 = 6
    print(ma.next(20))     # (20 + 11 + 5 + 3 + 10) / 5 = 9.8
    print(ma.next(13))     # (13 + 20 + 11 + 5 + 3) / 5 = 10.4

if __name__ == '__main__':
    main()
