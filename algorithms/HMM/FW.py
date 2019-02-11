#INPUT

seq = "ATGC"

TRANS = {"B":{"Y":0.2, "N": 0.8},
		 "Y":{"Y":0.7, "N":0.2, "E":0.1},
		 "N":{"Y":0.1, "N": 0.8, "E":0.1}
		 }

EMIS = {"Y":{"A":0.1, "C":0.4, "T":0.1, "G":0.4},
		"N":{"A":0.25, "C":0.25, "T":0.25, "G":0.25}
		}
		
STATES = ["B", "Y", "N", "E"]

r = len(STATES)
c = len(seq) + 1

#INITIALIZATION

M = [[0.0 for col in range(c+1)] for row in range(r)]

M[0][0] = 1.0
for row in range(1,r-1):
	M[row][1] = TRANS["B"][STATES[row]]*EMIS[STATES[row]][seq[0]]

#ITERATION

for col in range(2,c):
	for row in range(1,r-1):
		score = []
		for state in range(1,r-1):
			score += M[state][col-1]*TRANS[STATES[state]][STATES[row]]
		M[row][col] = score*EMIS[STATES[row]][seq[col-1]]
		

#TERMINATION

finalscore = 0.0
for state in range(1,r-1):
	finalscore += M[state][c-2]*TRANS[STATES[state]]["E"]
	M[r-1][c-1] = score
	
for i in range(len(M)):
	print(M[i])
print("The sequence analyzed is: " + seq)
print("P(S|M) = " + str(score))


