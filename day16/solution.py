import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()

    def construct_intervals(self):
        # field_name: [(a, b), (c, d)]
        # e.g. field_name = "row", (a, b) is the 1st interval, (c, d) is the 2nd (after the or)
        ret = {}
        for line in self.input[:self.input.index('')]:
            field_name, intervals = line.split(': ')
            ret[field_name] = []
            i, j = intervals.split(" or ")
            ret[field_name].append((int(i.split("-")[0]), int(i.split("-")[1])))
            ret[field_name].append((int(j.split("-")[0]), int(j.split("-")[1])))
        return ret
    
    def is_in_intervals(self, intervals, value):
        for (minimum, maximum) in intervals:
            if value >= minimum and value <= maximum:
                return True
        return False

    def solve_part_1(self):
        intervals_map = self.construct_intervals()
        intervals = [i for ivls in intervals_map.values() for i in ivls]
        invalid_values = 0
        self.valid_tickets = []
        for line in self.input[self.input.index('nearby tickets:') + 1:]:
            values = [int(v) for v in line.split(',')]
            if all(self.is_in_intervals(intervals, v) for v in values):
                self.valid_tickets.append(values)
            for v in values:
                if not self.is_in_intervals(intervals, v):
                    invalid_values += v
        return invalid_values

    def solve_possible_matches(self, all_possible_matches, num_fields):
        matches = {}
        while len(matches) < num_fields:
            for possible_matches in all_possible_matches:
                filtered = list(filter(lambda x: x[0] not in matches, possible_matches))
                if len(filtered) == 1:
                    matches[filtered[0][0]] = filtered[0][1]
        return matches

    def solve_part_2(self):
        import functools
        all_possible_matches = []
        intervals_map = self.construct_intervals()
        for i in range(len(s.valid_tickets[0])):
            column = []
            for ticket in self.valid_tickets:
                column.append(ticket[i])
            possible_matches = []
            for name, intervals in intervals_map.items():
                if all(self.is_in_intervals(intervals, v) for v in column):
                    possible_matches.append((name, i))
            all_possible_matches.append(possible_matches)
        mapping = self.solve_possible_matches(all_possible_matches, len(intervals_map))
        my_ticket = [int(v) for v in self.input[self.input.index('your ticket:') + 1].split(',')]
        return functools.reduce(lambda x, y: x * y, [my_ticket[i] for k, i in mapping.items() if k.startswith("departure")] , 1)

if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)