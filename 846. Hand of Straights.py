from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for card in sorted(count):
            while count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False
        return True
