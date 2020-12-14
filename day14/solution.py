import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()
        self.memory_map = {}

    def set_bit(self, value, bit):
        return value | (1 << bit)
    
    def clear_bit(self, value, bit):
        return value & ~(1 << bit)

    def applyMask(self, value):
        new_value = ""
        for i in range(36):
            if self.mask[i] == 'X':
                new_value += str(value >> (35 - i) & 1)
            else:
                new_value += self.mask[i]
        return int(new_value, 2)

    def applyMaskFloat(self, key, value):
        masked, floats = "", []        
        for i in range(36):
            if self.mask[i] == 'X':
                floats.append(i)
                masked += "X"
            elif self.mask[i] == '0':
                masked += str(key >> (35 - i) & 1)
            else:
                masked += "1"

        def recurse(index, cur_key):
            if index == len(floats):
                self.memory_map[int(cur_key, 2)] = value
            else:
                recurse(index + 1, cur_key[0: floats[index]] + "0" + cur_key[floats[index] + 1:])
                recurse(index + 1, cur_key[0: floats[index]] + "1" + cur_key[floats[index] + 1:])
    
        recurse(0, masked)

    def solve_part_1(self):  
        for instr in self.input:
            if instr.startswith("ma"):
                self.mask = instr.split(" = ")[1]
            else:
                mem_key, mem_value = instr.split(" = ")
                mem_key = int(mem_key[mem_key.index('[') + 1: mem_key.index(']')])
                mem_value = int(mem_value)
                self.memory_map[mem_key] = self.applyMask(mem_value)
        return sum(self.memory_map.values())
        
    
    def solve_part_2(self):
        self.memory_map = {}
        for instr in self.input:
            if instr.startswith("ma"):
                self.mask = instr.split(" = ")[1]
            else:
                mem_key, mem_value = instr.split(" = ")
                mem_key = int(mem_key[mem_key.index('[') + 1: mem_key.index(']')])
                mem_value = int(mem_value)
                self.applyMaskFloat(mem_key, mem_value)
        return sum(self.memory_map.values())


if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)