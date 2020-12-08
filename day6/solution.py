import os 
import sys

class Solution:

    def __init__(self):
        with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
            self.input = f.read().split('\n')

    def sum_counts(self):
        i, answers, cnt = 0, set(), 0

        while i < len(self.input):
            if not self.input[i]:
                cnt += len(answers)
                answers = set()
            else:
                answers.update([c for c in self.input[i]])
            i += 1
        return cnt

    def count_all_yes(self, answers, num_people):
        return len(filter(lambda k: answers[k] == num_people, answers))

    def sum_all_yes_counts(self):
        i, answers, num_people, cnt = 0, {}, 0, 0
        while i < len(self.input):
            if not self.input[i]:
                cnt += self.count_all_yes(answers, num_people)
                answers, num_people = {}, 0
            else:
                for c in self.input[i]:
                    if c in answers:
                        answers[c] += 1
                    else:
                        answers[c] = 1
                num_people += 1
            i += 1

        return cnt  

    

if __name__ == '__main__':
    s = Solution()
    print(s.sum_counts())
    print(s.sum_all_yes_counts())