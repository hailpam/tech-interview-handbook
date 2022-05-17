
def find_days(revenues, milestones):
    acc = 0
    # build the array with monotonically increasing revenue values
    for i, revenue in enumerate(revenues):          # O(N)
        acc += revenue
        revenues[i] = acc
    # let's find the days when the revenues are first reached
    days = []
    for milestone in milestones:                    # O(M)
        for i, revenue in enumerate(revenues):      # O(N), in reality, very unlikely goes to the full scan
            # a hit, let's record and exit the loop immediately
            if revenue >= milestone:
                days.append(i + 1)
                break
    return days

def main():
    revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    milestones = [100, 200, 500]
    print('[4, 6, 10]', find_days(revenues, milestones))

if __name__ == '__main__':
    main()
