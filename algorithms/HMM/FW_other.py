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

M = [[0 for row in range(1,r)] for col in range(1,c)]

M[0][0] = 1.0

for row in range(1,r-1):
	M[row][1] = M[0][0] * TRANS["B"][STATES[row]]*EMIS[STATES[row]][seq[0]]

for col in range(2,c):
	for row in range(1,r-1):
		score = 0.0
		for state in range(1,r-1):
			score += M[state][col-1]*TRANS[STATES[state]][STATES[row]]*EMIS[STATES[row]][seq[col-1]]
		M[row][col] = score

#TERMINATION
endscore = 0.0
for row in range(1,r-1):
	endscore += M[r-1][c-1] + M[row][c-1]*TRANS[STATES[row]]["E"]
print(endscore)			
