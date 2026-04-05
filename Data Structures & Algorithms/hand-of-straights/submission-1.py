class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: # more cards can we distribute
            return False

        count = defaultdict(int)
        for card in hand:
            count[card] += 1
        
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for idx in range(first, first + groupSize):
                if idx not in count:
                    return False
                count[idx] -= 1

                if count[idx] == 0:
                    if idx != min_heap[0]:
                        return False # this means we have 1 card before this, which will break sequence
                    heapq.heappop(min_heap)
        return True