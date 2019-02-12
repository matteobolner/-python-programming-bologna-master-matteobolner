# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code:
1)create a function that asks the user to input 10 values, which will be added to a list
3)create a function that given a list calculates the average of the values inside it (sum of all values divided by the number of values, in this case 10)
4)print the two function returns
'''
vector_string = input(("Write 10 numbers separated by a comma(,):"))

def vector_input(vector_string):
	vector_list = vector_string.split(",")
	
vector_input(vector_string)

vector_list = vector_string.split(",")

def average(vector_list):
	sum_values = 0
	for k in vector_list:
		sum_values+=float(k)
	avg = float((sum_values)/len(vector_list))
	print("the average of the values of the vector you inserted is: " + str(avg))
		
average(vector_list)
