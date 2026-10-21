class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # We sort our cards so that later we can go through it, min to max.
        hand.sort()

        cardCounts = {}

        for card in hand:
            if card not in cardCounts:
                cardCounts[card] = 0
            cardCounts[card] = cardCounts[card] + 1

        # Start at the min card and build a group until we hit groupSize.
        # When we start making the next group, iterate through hand and look for the min.

        for card in hand:
            # This is not the start of a group, so keep going
            if cardCounts[card] == 0:
                continue

            # card is the start of a group.
            # for each value from card to card + groupSize - 1:
            for i in range(groupSize):
                if card + i not in cardCounts or cardCounts[card + i] == 0:
                    return False
                    
            #- otherwise use up one copy of it
                cardCounts[card + i] = cardCounts[card + i] - 1

        return True
