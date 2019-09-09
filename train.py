import csv

matrix_input = []
vector_t = []
# Get 12 examples from a csv file and the truth for each one
with open("train.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 2
    for row in csv_reader:
        if line_count%2 == 0:
            matrix_input.append(row)
        else:
            vector_t.append(row[0])
        line_count += 1

# Create vector with zeros for weight
vector_weight = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n = 0.05
find_error = True
while (find_error == True):
    find_error = False
    for i, example in enumerate(matrix_input):
        s_out = 0
        print("Vector of weights:")
        print(vector_weight)
        print("Truth:")
        print(vector_t[i])
        for j in range(len(example)):
            s_out += int(example[j])*vector_weight[j]
        print("S out:")
        print(s_out)
        erro = int(vector_t[i]) - s_out
        # print(str(erro)+"="+vector_t[i]+"-"+str(s_out))
        if erro != 0:
            find_error = True
            j = 0
            for j in range(len(vector_weight)):
                vector_weight[j] += n*erro*int(example[j])

with open("weights.csv", "w") as f:
    for item in vector_weight:
        f.write(str(item)+",")

        


