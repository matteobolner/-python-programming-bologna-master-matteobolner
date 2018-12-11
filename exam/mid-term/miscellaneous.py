# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

'''L = list(range(21,40))
print("These are the even numbers in the list L: \n")
for i in L:
	if (int(i)%2) == 0 :
		print(i)
print("\nThese are the multiples of 3 in the list L: \n")
for i in L:
	if (int(i)%3) == 0 :
		print(i)'''


# Exercise 2
# Print the last two elements of L 

#print(L[-2:])

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

'''L = ['1', '2', '3']
for i in range(10):
	if str(i) in L:
		print(str(i) + " is in the list")
	else:
		print(str(i) + " not found")'''    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 

'''ex_file = open("sprot_prot.fasta" , "r")
first_line = (ex_file.readline())
splitted_line = first_line.split("OS=")
second_element = splitted_line[1]
print(second_element)'''

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
'''splitted_second_el = second_element.split()
concatenated_elements_of_splitted = splitted_second_el[0] + splitted_second_el[1]
print(concatenated_elements_of_splitted)'''


# Exercise 6
# reverse the string 'asor rosa'
'''forward_string = "asor rosa"
reverse_string = forward_string[::-1]
print(reverse_string)'''

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
'''L = [1, 7, 3, 9]
L.sort()'''

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

'''L = [1, 7, 3, 9]
new_L = sorted(L)'''

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

'''table_file = open("table.txt" , "w")
table_file.write("2 4\n3 6")'''
