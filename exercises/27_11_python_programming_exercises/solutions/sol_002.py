#1
var1 = "fire and ice"
#2
print(var1[2])
#3
print(var1[5])
#4
print(var1[9],var1[-1],var1[-2])
#5 this script prints the even-numbered characters of a given string
odds = var1[1::2]
for elements in odds:
	print(elements)
#6 this one prints odd characters
odds = var1[0::2]
for elements in odds:
	print(elements)
#7
print(var1[0:len(var1)//2])
#8
var1 = "fire and ice"
print(var1[-1::-1])
#9
print(var1.count("i"))
print(var1.count("e"))
#10
var1 = "fire and ice"
var1.replace("and", "&")
#11
if "fire" in var1:
	print("yes,fire")
#12
if "re and" in var1:
	print("yes, re and")

#13	
if "re &" in var1:
	print("yes, re &")
#14
print(var1.index("e"))
#15
print(var1.rindex("e"))
#16
var2 = "234 4329 7654 8923"
var2_fixed = var2.replace(" ","")
for number in var2_fixed :
	print(int(number) +3)









