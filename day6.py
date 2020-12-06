f = open('day6.data', 'r')
data = f.read()
data = data.split('\n\n')
data = [d.split('\n') for d in data]
print(data[0])

answer = 0

for d in data:
    num_people = len(d)


    
print(answer)
# data = [d.replace('\n', '') for d in data]
# data = [''.join(set(d)) for d in data]
# answer = sum(list(map(lambda x: len(x), data)))
# print(answer)