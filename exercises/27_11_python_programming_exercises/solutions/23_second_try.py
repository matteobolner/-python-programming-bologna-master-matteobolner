seqs_file = open("ex_23.txt" , "r")
seq_line_read = seqs_file.readline
seqs_list = []
for line in seqs_file.readlines() :
	if line[0] != ">" and line[0] != "" and line[0] != "\n" :
		if line.endswith("\n"):
			seqs_list.append(line[0:-2])
		else:
			seqs_list.append(line)
seq_couples_list= list(zip(seqs_list[0::2],seqs_list[1::2]))
#print(seq_couples_list)
check_sequence = ""
for i,j in seq_couples_list:
	other_list= zip(i,j)
	for x,z in other_list:
		if x==z :
			check_sequence+= "|"
		else:
			check_sequence+= "X"
	check_sequence+= "\t"*2
a = (seqs_list[::2])
print(a[0]+"\t"*2 +a[1])
#for s in seqs_list:
#	print(s[0])
print(check_sequence)
b=(seqs_list[1::2])
print(b[0]+"\t"*2 + b[1])
