import os 
import sys

# Hacky

class Int(int):

    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return Int(self.v * other.v)

    def __mul__(self, other):
        return Int(self.v + other.v)

    def __repr__(self):
        return f"Int({self.v})"

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = ["".join(line.split(" ")) for line in f.read().splitlines()]

    def solve(self, line, index):
        operand_stack, operation_stack, i = [], [], 0
        while index < len(line):
            c = line[index]
            if c.isdigit():
                operand_stack.append(int(c))
            elif c == '+' or c == '*':
                operation_stack.append(c)
            elif c == '(':
                index, eval_subexpr = self.solve(line, index + 1)
                operand_stack.append(eval_subexpr)
            else:
                # c == ')'
                return index, operand_stack.pop()
            index += 1
            if len(operand_stack) == 2:
                op = operation_stack.pop()
                opd1, opd2 = operand_stack.pop(), operand_stack.pop()
                operand_stack.append(opd1 + opd2 if op == '+' else opd1 * opd2) 
        assert len(operation_stack) == 0
        assert len(operand_stack) == 1
        return operand_stack.pop()


    def solve_part_1(self):
        return sum(self.solve(line, 0) for line in self.input)
    
    def solve_part_2(self):
        replaced_input = []
        for line in self.input:
            new_line = ""
            for i, c in enumerate(line):
                if c.isdigit():
                    new_line += f"Int({c})"
                elif c == '+':
                    new_line += '*'
                elif c == '*':
                    new_line += '+'
                else:
                    new_line += c
            replaced_input.append(new_line)
        return sum(int(eval(s)) for s in replaced_input)


if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1())
    print(s.solve_part_2())