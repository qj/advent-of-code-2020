import os
import re 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()
            rules_messages_split_index = self.input.index('')
            self.rules = self.parse_rules(self.input[:rules_messages_split_index])
            self.messages = self.input[rules_messages_split_index + 1:]

    def parse_rules(self, rules):
        parsed_rules = {}
        for line in rules:
            i, r = line.split(": ")
            parsed_rules[i] = r.strip('\"')
        return parsed_rules

    def create_or_reset_cache(self):
        self.cache = {}
        for i, r in self.rules.items():
            if r == 'a' or r == 'b':
                self.cache[i] = r

    def contains_only_solved_rules(self, rules):
        for i in rules.split(" "):
            if i.isdigit():
                if i not in self.cache:
                    return False
        return True

    def solve_regex(self, rule_id, regex, level):
        rule = self.rules[rule_id]
        if level > 9 and '42' in self.cache:
            return f"{self.cache['42']}+"
        while not self.contains_only_solved_rules(rule):
            for i in rule.split(" "):
                if i.isdigit():
                    if i in self.cache:
                        regex += self.cache[i]
                    else:
                        self.cache[i] = self.solve_regex(i, regex, level + 1)
        new_rule = "".join(self.cache[i] if i.isdigit() else '|' for i in rule.split(' '))
        self.cache[rule_id] = f"({new_rule})"
        return self.cache[rule_id]


    def solve_part_1(self, start_rule):
        self.create_or_reset_cache()
        regex = re.compile('^' + self.solve_regex(start_rule, "", 0) + '$')
        return len(list(filter(regex.match, self.messages)))

    def solve_part_2(self, start_rule):
        self.rules['8'] = '42 | 42 8'
        self.rules['11'] = '42 31 | 42 11 31'
        self.create_or_reset_cache()
        regex = re.compile('^' + self.solve_regex(start_rule, "", 0) + '$')
        return len(list(filter(regex.match, self.messages)))


if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1("0"))
    print(s.solve_part_2("0"))
