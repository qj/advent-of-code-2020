import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split()
            # direction vector, N, E are +ve
            self.position, self.direction = (0, 0), (0, 1)

    def rotate_clockwise(self, degrees):
        degrees = degrees % 360 
        possible_directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        curr_direction_index = possible_directions.index(self.direction)
        return possible_directions[(curr_direction_index + degrees // 90) % 4]

    def rotate_waypoint_clockwise(self, direction, degrees):
        degrees = degrees % 360
        cur_direction = direction
        for _ in range(degrees // 90):
            n, e = cur_direction
            if n >= 0 and e >= 0:
                cur_direction = (-cur_direction[1], cur_direction[0])
            elif n < 0 and e > 0:
                cur_direction = (-cur_direction[1], cur_direction[0])
            elif n < 0 and e < 0:
                cur_direction = (abs(cur_direction[1]), cur_direction[0])
            else:
                cur_direction = (abs(cur_direction[1]), cur_direction[0])
        return cur_direction
        

    def solve_part_1(self):  
        for ins in self.input:
            direction, steps = ins[0], int(ins[1:])
            
            if direction == 'F':
                self.position = (self.position[0] + steps * self.direction[0], self.position[1] + steps * self.direction[1])
            elif direction == 'E':
                self.position = (self.position[0], self.position[1] + steps)
            elif direction == 'W':
                self.position = (self.position[0], self.position[1] - steps)
            elif direction == 'N':
                self.position = (self.position[0] + steps, self.position[1])
            elif direction == 'S':
                self.position = (self.position[0] - steps, self.position[1])
            elif direction == 'R':
                self.direction = self.rotate_clockwise(steps)
            elif direction == 'L':
                self.direction = self.rotate_clockwise(360 - steps % 360)
        return abs(self.position[0]) + abs(self.position[1])
    
    def solve_part_2(self):
        waypoint_direction, self.position = (1, 10), (0, 0)
        for ins in self.input:
            direction, steps = ins[0], int(ins[1:])

            if direction == 'F':
                self.position = (self.position[0] + steps * waypoint_direction[0], self.position[1] + steps * waypoint_direction[1])
            elif direction == 'E':
                waypoint_direction = (waypoint_direction[0], waypoint_direction[1] + steps)
            elif direction == 'W':
                waypoint_direction = (waypoint_direction[0], waypoint_direction[1] - steps)
            elif direction == 'N':
                waypoint_direction = (waypoint_direction[0] + steps, waypoint_direction[1])
            elif direction == 'S':
                waypoint_direction = (waypoint_direction[0] - steps, waypoint_direction[1])
            elif direction == 'R':
                waypoint_direction = self.rotate_waypoint_clockwise(waypoint_direction, steps)
            elif direction == 'L':
                waypoint_direction = self.rotate_waypoint_clockwise(waypoint_direction, 360 - steps % 360)
        return abs(self.position[0]) + abs(self.position[1])


if __name__ == '__main__':
    s = Solution()
    part_1 = s.solve_part_1()
    print(part_1)
    part_2 = s.solve_part_2()
    print(part_2)