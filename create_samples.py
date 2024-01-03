import random
import csv

values = []
with open("medium_data.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        values.append(row[7])

print(values)

sample_1 = [[values[0]]]
sample_2 = [[values[0]]]
sample_3 = [[values[0]]]
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index= random.radint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.main(dataset)
    random main

for i in range(100):
    sample_1.append([random.choice(values)])

for i in range(100):
    sample_2.append([random.choice(values)])

for i in range(100):
    sample_3.append([random.choice(values)])

with open("sample_1.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_1)

with open("sample_2.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_2)

with open("sample_3.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample_3)