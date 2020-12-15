class Solution:

    def __init__(self):
        # self.input = [20,9,11,0,1,2]
        self.input = [20,9,11,0,1,2]

    def solve_part_1(self, N):
        spoken_map, last_spoken = {}, None
        for i in range(len(self.input)):
            spoken_map[self.input[i]] = [i + 1]
            last_spoken = self.input[i]
        n = len(self.input)
        while n < N:
            if len(spoken_map[last_spoken]) == 1:
                # new number
                last_spoken = 0
                if last_spoken in spoken_map:
                    spoken_map[0].append(n + 1)
                else:
                    spoken_map[0] = [n + 1] 
            else:
                last_spoken = spoken_map[last_spoken][-1] - spoken_map[last_spoken][-2]
                if last_spoken in spoken_map:
                    spoken_map[last_spoken].append(n + 1)
                else:
                    spoken_map[last_spoken] = [n + 1]
            n += 1
        return last_spoken

    def solve_part_2(self):
        return self.solve_part_1(30000000)
    

if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1(2020))
    print(s.solve_part_2())