sequence_file = open("ex_23.txt" , "r")
seq_line = sequence_file.readline(0)
seq_list = []
for seq_line in sequence_file :
	if seq_line[0] == ("A") or seq_line[0] =="T" or seq_line[0] == "C" or seq_line[0] == "G" :
		seq_list += [seq_line[0:-1]]
#print(seq_list)		

compl_list_undivided = "clu"
clu = ""
for i in seq_list:
	for j in i:
		if j == "A":
			clu+="T"
		elif  j == "T":
			clu+="A"
		elif j == "C":
			clu+="G"
		elif j == "G":
			clu+="C"
	clu+= ","
	
compl_list_divided = "cld"
cld =clu.split(",")
#print(cld)
print(seq_list)
for 	


'''check_sequence = ""

for i,j in zip (seq_list, cld) :
	for z,y in enumerate(zip(seq_list,cld)):
		print(i,j)
		if z == y :
			check_sequence+= "|"
		else :
			check_sequence+= "X"
	
print(check_sequence)
print("\n Number of bp not complementary: " + str(check_sequence.count("X")))'''
