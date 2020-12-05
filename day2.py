f = open('day2.data', 'r')
data = f.readlines()

valid_pws = 0
for line in data:
    line = line.split(':')
    policy_str = line[0].split()
    letter = policy_str[1]
    pOne = int(policy_str[0].split('-')[0])
    pTwo = int(policy_str[0].split('-')[1])
    pw = line[1].rstrip()

    if pw[pOne] == letter and pw[pTwo] == letter:
        continue
    elif pw[pOne] == letter:
        valid_pws += 1
    elif pw[pTwo] == letter:
        valid_pws += 1

print(valid_pws)
