import os
import sys 

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()

    def construct_deck(self):
        split = self.input.index('')
        player_1 = [int(i) for i in self.input[1: self.input.index('')]]
        player_2 = [int(i) for i in self.input[split + 2:]]
        return player_1, player_2

    
    def solve_part_1(self):
        player_1, player_2 = self.construct_deck()
        while player_1 and player_2:
            p1_top, p2_top = player_1[0], player_2[0]
            player_1, player_2 = player_1[1:], player_2[1:]
            if p1_top > p2_top:
                player_1 += [p1_top, p2_top]
            else:
                player_2 += [p2_top, p1_top]
        
        winner = player_1 if player_1 else player_2

        count = 0

        for i in range(len(winner)):
            count += (len(winner) - i) * winner[i]
        
        return count

    def solve_part_2(self):
        player_1, player_2 = s.construct_deck()

        def recurse(p1, p2):
            history = set()
            while p1 and p2:
                if (tuple(p1), tuple(p2)) in history:
                    return True, p1
                history.add((tuple(p1), tuple(p2)))
                p1_top, p2_top = p1.pop(0), p2.pop(0)
                if len(p1) >= p1_top and len(p2) >= p2_top:
                    # recursive game
                    p1_won, _ = recurse(p1[:p1_top], p2[:p2_top]) 
                    if p1_won:
                        p1 += [p1_top, p2_top]
                    else:
                        p2 += [p2_top, p1_top]
                else:
                    if p1_top > p2_top:
                        p1 += [p1_top, p2_top]
                    else:
                        p2 += [p2_top, p1_top]
            
            if p1:
                return True, p1
            else:
                return False, p2 

        _, cards = recurse(player_1, player_2)

        count = 0

        for i in range(len(cards)):
            count += (len(cards) - i) * cards[i]
        
        return count
        

if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1())
    print(s.solve_part_2())