# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code:
1)first, i have to open the file in order for it to be read
2)then i have to create an empty file ready to be written to
3)then i must read the sprot_prot.fasta file line by line ; if a line starts with ">" and doesnt contain "Homo sapiens" i will write it in the empty file; then, the program must keep writing the sequence to the new file until it  ends
4) i must split the header and recover the part containing the name of the organism
'''
sequences = open("sprot_prot.fasta" , "r") #open the fasta file
selected_sequences = open("selected_sequences.txt" , "w") #open a new empty file
sec = ""
for line in sequences:
	if line.startswith(">"):
		sec = ""
		if "Homo sapiens" not in line:
			selected_sequences.write(line)
			sec = line
	elif line[0] != ">" and sec :
		selected_sequences.write(line)
selected_sequences.close()

#second part
selected_sequences = open("selected_sequences.txt" , "r")
first_line = (selected_sequences.readline())
if ">" in first_line:
	splitted_line = first_line.split("OS=")
	second_element = splitted_line[1]
	b = second_element.split("GN")
	print(b[0])
	
second_line =(selected_sequences.readline()) #need to find out the line with tthe second header
if ">" in second_line:
	splitted_line2 = second_line.split("OS=")
	second_element = splitted_line2[1]
	c = second_element.split("GN")
	print(c[0])
#this works only for the first header
#i couldnt add the sequence counting part because of time constraints
