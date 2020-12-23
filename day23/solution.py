import os
import sys 

class Cup:

    def __init__(self, label: int):
        self.label = label
        self.next = None
    
    def __repr__(self):
        return f"Cup {self.label}"

class Solution:

    def __init__(self, tdata: bool):
        self.input = "389125467" if tdata else "562893147"
        self.input = [int(i) for i in self.input]
    
    def calc_destination(self, n):
        if n == 1:
            return 9
        else:
            return n - 1

    def solve_part_1(self):
        iterations, curr, length = 0, 0, len(self.input)

        while iterations < 100:
            current = self.input[curr]
            removed_indices = [(curr + 1) % length, (curr + 2) % length, (curr + 3) % length]
            three_adj = [self.input[(curr + 1) % length], self.input[(curr + 2) % length], self.input[(curr + 3) % length]]
            target = self.calc_destination(current)
            while self.input.index(target) in removed_indices:
                target = self.calc_destination(target)
            self.input = [x for x in self.input if x not in three_adj]
            for i, c in enumerate(three_adj):
                self.input.insert(self.input.index(target) + i + 1, c)
            curr = (self.input.index(current) + 1) % length
            iterations += 1
        
        index_of_one = self.input.index(1)

        return "".join(str(c) for c in self.input[(index_of_one + 1) % length:] + self.input[:index_of_one])

    def solve_part_2(self, num_cups: int, num_iterations: int, tdata: bool):
        if tdata:
            input = "389125467"
        else:
            input = "562893147"

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
    s = Solution(True)
    print(s.solve_part_1())
    print(s.solve_part_2(1000000, 10000000, False))