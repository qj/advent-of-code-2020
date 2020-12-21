import os
import sys 

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().splitlines()

    def construct_mapping(self):
        allergen_map = {}
        self.ingredients = []
        for line in self.input:
            ingredients, allergens = line[:-1].split(" (contains ")
            for i in ingredients.split(" "):
                self.ingredients.append(i)
            for a in allergens.split(", "):
                if a not in allergen_map:
                    allergen_map[a] = set(ingredients.split(" "))
                else:
                    allergen_map[a].intersection_update(set(ingredients.split(" ")))
        return allergen_map

    
    def solve_part_1(self):
        allergen_map = self.construct_mapping()
        self.identified = {}

        while len(self.identified) < len(allergen_map):
            for allergen in allergen_map:
                if len(allergen_map[allergen]) == 1:
                    matched = allergen_map[allergen].pop()
                    self.identified[allergen] = matched
                    for allergen in allergen_map:
                        if matched in allergen_map[allergen]:
                            allergen_map[allergen].remove(matched)

        return len(list(filter(lambda x: x not in self.identified.values(), self.ingredients)))

    def solve_part_2(self):
        return ",".join(self.identified[k] for k in sorted(self.identified))

if __name__ == '__main__':
    s = Solution()
    print(s.solve_part_1())
    print(s.solve_part_2())