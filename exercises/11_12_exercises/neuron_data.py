data_file = open("neuron_data-2.txt", "r") #open the file in reading mode

L1 = []		#initialize list 1
L2 = []		#initialize list 2
for line in data_file:
	splitted_line = line.split()	#split line over blank spaces
	if splitted_line[0] == "1":
		L1.append(splitted_line[1])	
	else:
		L2.append(splitted_line[1])
print(L1,L2)
def average(vector):
    s = 0
    for i in vector:
        s+=float(i)
    avg=s/((len(vector)))
    return avg

average(L1)

average(L2)

