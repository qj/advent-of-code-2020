import os 
import sys
from collections import defaultdict

class Solution:

    def __init__(self, tdata: bool):
        file_name = "test.txt" if tdata else "input.txt"
        with open(os.path.join(sys.path[0], file_name), "r") as f:
            self.input = f.read().splitlines()
        self.rules = self.generate_rules()

    def generate_rules(self):
        rules = {}
        for r in self.input:
            k, v = r.split(" contain ")
            rules[k.replace(" bags", "")] = [b.replace(" bags", "").replace(" bag", "") for b in v[:-1].split(", ")]
        return rules 
    
    def solve_part_1(self):
        from collections import deque

        q = deque()
        q.append('shiny gold')
        bags, visited = set(), {}

        while q:
            to_search = q.popleft()
            if to_search in visited:
                continue
            for bag, rules in self.rules.items():
                if any([to_search in r for r in rules]):
                    q.append(bag)
                    bags.add(bag)
            visited[to_search] = True
        
        return len(bags)

    def solve_part_2(self, start_bag):
        def subbags(bag, num_subbags):
            if bag in num_subbags:
                return num_subbags[bag]
            for b in self.rules[bag]:
                if b == 'no other':
                    num_subbags[bag] = 0
                    return 0
                quantity, colour = b.split(' ', 1)
                num_subbags[bag] += int(quantity) * (1 + subbags(colour, num_subbags))
            return num_subbags[bag]
        return subbags(start_bag, defaultdict(int))

if __name__ == '__main__':
    s = Solution(False)
    print(s.solve_part_1())
    print(s.solve_part_2('shiny gold'))