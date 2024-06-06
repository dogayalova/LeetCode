class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        #first count the cards
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1
                
        #form groups
        for card in hand:
            if card_count[card] > 0:
                for i in range(groupSize):
                    if card+i not in card_count or card_count[card+i] == 0:
                        return False
                    card_count[card+i] -= 1
                    
        return True