first_sequence = input("Insert first sequence")
second_sequence = input("Insert second sequence")
list_second = list(second_sequence)
compl_first = ""
for i in first_sequence:
	if i == "A":
		compl_first+="T"
	elif i == "T":
		compl_first+="A"
	elif i == "C":
		compl_first+="G"
	elif i == "G":
		compl_first+="C"
rev_seq=compl_first[::-1]
big_list = zip (list_second,rev_seq)
print(first_sequence)
check_sequence = ""
for i,j in big_list:
	if i == j :
		check_sequence+= "|"
	else :
		check_sequence+= "X"
print(check_sequence)
print(rev_seq)
print("\n Number of bp not complementary: " + str(check_sequence.count("X")))	
