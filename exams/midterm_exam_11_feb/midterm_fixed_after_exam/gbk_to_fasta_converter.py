gbk_file = open("insulin.gbk", "r")
fasta_file = open("insulin.fasta", "w")

flag = 0

for line in gbk_file:
	if line[0:9] == "ACCESSION":
		splitted_accession = line.split()
		header_accession = splitted_accession[1].strip()
		fasta_file.write(">" + header_accession + "|")	
	if "ORGANISM" in line:
		splitted_organism = line.split()
		header_organism1 = splitted_organism[1].strip()
		header_organism2 = splitted_organism[2].strip()
		fasta_file.write(header_organism1)
		fasta_file.write(" " +header_organism2 + "\n")
	if "ORIGIN" in line:
		flag = 1
		continue
	if flag == 1:
		columns = line.split()
		if columns != []:
			sequence = "".join(columns[1::])			#a small typo caused the numbers to be printed with the sequence => join(columns)[1:]
			fasta_file.write(sequence.upper() + "\n")	#added .upper() after sequence to print the sequence in uppercase letters
			
gbk_file.close()
fasta_file.close()
