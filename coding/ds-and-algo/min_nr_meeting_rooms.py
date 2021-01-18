
# On the Internet: https://guides.codepath.com/compsci/Scheduling-Meeting-Rooms

class Solution(object):
    def get_minutes(self, time_str):
        hour, minute = time_str.split(':')

        return int(hour) * 60 + int(minute)

    def find_room(self, rooms, slot):
        found = False
        for room in rooms:          # greedy, checking boundaries, if a free room is found, use it
            if slot[0] >= room[-1][1]:
                room.append(slot)
                found = True
                break

        if not found:               # in case of empty rooms, or need of a new one
            rooms.append([slot])

    def min_nr_meeting_rooms(self, meetings):
        slots = []
        for meeting in meetings:    # got to translates to minutes in a day (easier to work with)
            start = self.get_minutes(meeting[0])
            end = self.get_minutes(meeting[1])
            slots.append((start, end))
        
        slots.sort()                # got to sort to make assumptions on ordering
        rooms = []
        for slot in slots:          # for each and every slot, find a room
            self.find_room(rooms, slot)
        return len(rooms)

def main():
    s = Solution()

    meetings = [
        ('7:00', '9:00'),
        ('8:00', '10:00'),
        ('9:00', '9:30'),
        ('9:30', '10:00'),
        ('10:30', '11:30'),
        ('10:00', '12:00')
    ]
    print(s.min_nr_meeting_rooms(meetings))     # 2

    meetings = [
        ('7:00', '8:30'),
        ('8:00', '10:00'),
        ('8:00', '9:30'),
        ('9:30', '10:00'),
        ('10:30', '11:30'),
        ('10:00', '12:00')
    ]
    print(s.min_nr_meeting_rooms(meetings))     # 3

if __name__ == '__main__':
    main()
