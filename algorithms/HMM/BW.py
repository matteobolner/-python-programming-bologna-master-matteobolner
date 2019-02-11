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

#INITIALIZATION

r = len(STATES)
c = len(seq) + 2

M = [[0 for col in range(c)] for row in range(r)]

for state in range(1,r-1):
	M[state][len(seq)] = TRANS[STATES[state]]["E"]

#ITERATION

for row in range(1,r-1):
	for col in range(len(seq)-1,0,-1):
		score = 0
		for state in range(1,r-1):
			score+= M[state][col+1]*TRANS[STATES[row]][STATES[state]]*EMIS[STATES[state]][seq[col]]
		M[row][col] = score

#TERMINATION

score = 0.0
for state in range(1,r-1):
	score+= M[state][1]*TRANS["B"][STATES[state]]*EMIS[STATES[state]][seq[0]]
	M[0][0] = score
	
print(M)


