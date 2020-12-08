import os 
import sys

class Solution:

    def __init__(self):
        self.accum = 0
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()
            print(len(self.input))

    def run_code(self):
        ln, seen = 0, set()

        while ln not in seen:
            if ln == len(self.input):
                return True
            instr = self.input[ln]
            op, arg = instr.split()
            arg = int(arg)

            seen.add(ln)

            if op == 'acc':
                self.accum += arg
                ln += 1
            elif op == 'jmp':
                ln += arg
            else:
                ln += 1
        return None

    def try_to_terminate(self):
        for i in range(len(self.input)):
            instr = self.input[i]
            op, arg = instr.split()

            if op == 'nop':
                self.input[i] = 'jmp %s' % arg 
                if self.run_code():
                    return self.accum
                self.input[i] = 'nop %s' % arg
            elif op == 'jmp':
                self.input[i] = 'nop %s' % arg
                if self.run_code():
                    return self.accum
                self.input[i] = 'jmp %s' % arg

            self.accum = 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.try_to_terminate())