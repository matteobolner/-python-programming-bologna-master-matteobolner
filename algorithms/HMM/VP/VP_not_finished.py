#INPUT

SEQ = "AGCGCGTAATCTG"

STATES = ["B","Y","N","E"]

TRANS = {"B":{"Y":0.2, "N":0.8}, 
		 "Y":{"Y":0.7, "N":0.2, "E":0.1},
		 "N":{"Y":0.1, "N":0.8, "E":0.1}
		}

EMIS = {"Y":{"A":0.1, "C":0.4, "T":0.1, "G":0.4},
		"N":{"A":0.25, "C":0.25, "T":0.25, "G": 0.25}
		}

#INITIALIZATION

r = len(STATES)
c = len(SEQ) + 2

V = [[0 for col in range(c)] for row in range(r)]
PATH = [[0 for col in range(1)] for row in range(r-2)]
V[0][0] = 1.0
for row in range(1, r-1):
	V[row][1] = V[0][0]*TRANS["B"][STATES[row]]*EMIS[STATES[row]][SEQ[0]]
for col in range(2, c-1):
	for row in range(1, r-1):
		SCORES = []
		for state in range(1,r-1):
			SCORE = V[state][col-1]*TRANS[STATES[state]][STATES[row]]
			SCORES.append(SCORE)
		MAX_SCORE = -float("inf")
		MAX_STATE = ""
		for index in range(0,len(SCORES)):
			if SCORES[index] > MAX_SCORE:
				MAXSCORE = SCORES[index]
				MAX_STATE = STATES[index+1]	
		V[row][col] = MAX_SCORE*EMIS[STATES[row]][SEQ[col-1]]
		PATH[row-1].append(MAX_STATE)
FINAL_SCORE = -float("inf")
BEST_PATH = ""
for row in range(1,r-1):
	if V[row][c-2]*TRANS[STATES[row]]["E"] > FINAL_SCORE:
		V[r-1][c-1] = V[row][c-2]*TRANS[STATES[row]][E]
		FINAL_SCORE = V[row][c-2]*TRANS[STATES[row]][E]
		PATH[row-1].append(STATES[row])
print(PATH)

