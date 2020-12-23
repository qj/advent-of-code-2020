import os
import sys 

class Cup:

    def __init__(self, label: int):
        self.label = label
        self.next = None
    
    def __repr__(self):
        return f"Cup {self.label}"

class Solution:
    
    def calc_destination(self, n):
        if n == 1:
            return 9
        else:
            return n - 1

    def solve_part_1(self, tdata: bool):
        input = "389125467" if tdata else "562893147"
        input = [int(i) for i in input]
        iterations, curr, length = 0, 0, len(input)

        while iterations < 100:
            current = input[curr]
            removed_indices = [(curr + 1) % length, (curr + 2) % length, (curr + 3) % length]
            three_adj = [input[(curr + 1) % length], input[(curr + 2) % length], input[(curr + 3) % length]]
            target = self.calc_destination(current)
            while input.index(target) in removed_indices:
                target = self.calc_destination(target)
            input = [x for x in input if x not in three_adj]
            for i, c in enumerate(three_adj):
                input.insert(input.index(target) + i + 1, c)
            curr = (input.index(current) + 1) % length
            iterations += 1
        
        index_of_one = input.index(1)

        return "".join(str(c) for c in input[(index_of_one + 1) % length:] + input[:index_of_one])

    def solve_part_2(self, num_cups: int, num_iterations: int, tdata: bool):
        input = "389125467" if tdata else "562893147"
        initial_labels = [int(i) for i in input]
        
        cups = {}

        for i in range(1, num_cups + 1):
            cups[i] = Cup(i)

        for i in range(len(initial_labels) + 1, num_cups):
            cups[i].next = cups[(i + 1) % (num_cups + 1)]

        for i in range(len(initial_labels)):
            cups[initial_labels[i]].next = cups[initial_labels[(i + 1) % len(input)]]
        
        cups[initial_labels[-1]].next = cups[len(initial_labels) + 1]

        cups[num_cups].next = cups[initial_labels[0]]

        curr = cups[initial_labels[0]]

        for _ in range(num_iterations):
            selected = curr.next
            curr.next = selected.next.next.next
            target = curr.label - 1 if curr.label > 1 else num_cups
            while target in [selected.label, selected.next.label, selected.next.next.label]:
                target = target - 1 if target > 1 else num_cups
            target_next = cups[target].next
            cups[target].next = selected
            selected.next.next.next = target_next
            curr = curr.next

        return cups[1].next.label * cups[1].next.next.label

        
if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1(False))
    print(s.solve_part_2(1000000, 10000000, False))