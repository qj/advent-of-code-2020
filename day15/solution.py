class Solution:

    def solve(self, input, N):
        spoken_map, last_spoken = {}, None
        for i in range(len(input)):
            spoken_map[input[i]] = i + 1,
        n = len(input)
        last_spoken = input[n - 1]
        while n < N:
            n += 1
            if len(spoken_map[last_spoken]) == 1:
                # new number
                last_spoken = 0
            else:
                last_spoken = spoken_map[last_spoken][1] - spoken_map[last_spoken][0]
            if last_spoken not in spoken_map:
                spoken_map[last_spoken] = n,
            elif len(spoken_map[last_spoken]) == 1:
                spoken_map[last_spoken] = spoken_map[last_spoken][0], n
            else:
                spoken_map[last_spoken] = spoken_map[last_spoken][1], n
        return last_spoken
    
if __name__ == '__main__':
    s = Solution()
    input = [20,9,11,0,1,2]
    print(s.solve(input, 2020))
    print(s.solve(input, 30000000))