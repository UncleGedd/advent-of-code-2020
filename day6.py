from collections import defaultdict
data = open('day6.data', 'r').read()
groups = [d.split('\n') for d in data.split('\n\n')]
common_answers = 0
for group in groups:
    group_dict = defaultdict(lambda: 0)
    for person in group:
        for answer in person:
            group_dict[answer] += 1
    for _, v in group_dict.items():
        if v == len(group):
            common_answers += 1

print(common_answers)
