import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split('\n')
    
    def is_valid_passport_by_keys(self, passport):
        return len(passport) == 8 or passport.keys() == {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    def is_valid_passport_by_values(self, passport):

        import re 

        def byr():
            return int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002

        def iyr():
            return int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
        
        def eyr():
            return int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

        def hgt():
            if passport['hgt'].endswith('cm'):
                return int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193
            elif passport['hgt'].endswith('in'):
                return int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76
            else:
                return False

        def hcl():
            return re.match('^#([a-f\d]){6}$', passport['hcl'])

        def ecl():
            return passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

        def pid():
            return re.match('^(\d{9})$', passport['pid'])

        return byr() and iyr() and eyr() and hgt() and hcl() and ecl() and pid() 

    
    def count_valid(self):
        i, passport, cnt = 0, {}, 0
        while i < len(self.input):
            if not self.input[i]:
                if self.is_valid_passport_by_keys(passport) and self.is_valid_passport_by_values(passport):
                    cnt += 1
                passport = {}
            else:
                kvpairs = self.input[i].split()
                for pair in kvpairs:
                    k, v = pair.split(':')
                    passport[k] = v
            i += 1
        print(cnt)
        return cnt



if __name__ == '__main__':
    s = Solution()
    s.count_valid()
    