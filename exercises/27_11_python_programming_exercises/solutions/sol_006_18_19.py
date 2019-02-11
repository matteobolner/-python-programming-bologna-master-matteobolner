first_string = input("Input the first string")
second_string = input("Input the second string")
compl_first = ""
for i in first_string:
	if i == "A":
		compl_first+="T"
	elif i == "T":
		compl_first+="A"
	elif i == "C":
		compl_first+="G"
	elif i == "G":
		compl_first+="C"

'''compl_second = ""
for j in second_string:
	if j == "A":
		compl_second+="T"
	elif j == "T":
		compl_second+="A"
	elif j == "C":
		compl_second+="G"
	elif j == "G":
		compl_second+="C"'''

if compl_first == second_string:
	print("The sequences are complementary")
else:
	print("The sequences are not complementary")
