import csv

matrix_input = []
vector_t = []
# Get 12 examples from a csv file and the truth for each one
with open("test.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 2
    for row in csv_reader:
        if line_count%2 == 0:
            matrix_input.append(row)
        else:
            vector_t.append(row[0])
        line_count += 1

vector_weight = []
with open("weights.csv", "r") as weights_csv:
    csv_reader = csv.reader(weights_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        vector_weight = row

for i, example in enumerate(matrix_input):
    s_out = 0
    for j in range(len(example)):
        s_out += int(example[j])*float(vector_weight[j])
    print("Resposta para exemplo "+str(i)+": "+str(s_out))
    print("Verdade para exemplo "+str(i)+": "+str(vector_t[i]))