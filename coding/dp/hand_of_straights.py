# On Leetcode: https://leetcode.com/problems/hand-of-straights/

class Solution(object):
    def rearrange(self, hand, w, rearranged, idx=0, subset=[]):
        if len(subset) == w:                # size is reached, time to add, clear and return
            rearranged.append(list(subset))
            subset.clear()
            return

        card = hand[idx]
        if card != -1:
            if not subset or subset[-1] != card:
                subset.append(card)         # add to current subset
                hand[idx] = -1              # not to be checked anymore
        
        self.rearrange(hand, w, rearranged, idx + 1, subset)

    def is_straight_hand(self, hand, w):
        """
        To verify that the hand is straight, it is required to rearrange the cards
        according to the subsets of the given size.
        In order to achieve that, a main loop drives the recursive process of 
        building valid subsets, after the array is sorted in ascending order.
        """
        if len(hand) % w != 0:              # check whether the subsetting is viable
            return False
        
        hand.sort()                         # sort to create ascending order

        rearranged = []
        for i, card in enumerate(hand):     # run through all elements
            if card != - 1:
                self.rearrange(hand, w, rearranged, i, [])
        
        return len(rearranged) == int(len(hand) / w)

def main():
    s = Solution()

    hand = [1,2,3,6,2,3,4,7,8]
    w = 3
    print(s.is_straight_hand(hand, w))      # True

    hand = [1,2,3,4,5]
    w = 4
    print(s.is_straight_hand(hand, w))      # False

if __name__ == '__main__':
    main()
