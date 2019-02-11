
#INPUT

seq1_input = "ACCA"
seq2_input = "ACTGG"

SCORES = {"A":{"A":2, "C":-1, "T":-1, "G":0},
		  "C":{"A":-1, "C":2, "T":0, "G":-1},
		  "T":{"A":-1, "C":0, "T":2, "G":-1}, 
		  "G":{"A":0, "C":-1, "T":-1, "G":2}, 
		  "GAP":-2}



#INITIALIZATION
seq1 = "-" + seq1_input
seq2 = "-" + seq2_input
r = len(seq1)
c = len(seq2)

M = [[0 for col in range(c)] for row in range(r)]
T = [["0" for col in range(c)] for row in range(r)]
#POPULATION

for row in range(1,r):
	for col in range(1,c):
	
		UP_SCORE = M[row-1][col] + SCORES["GAP"]
		LEFT_SCORE = M[row][col-1] + SCORES["GAP"]
		DIAG_SCORE = M[row-1][col-1] + SCORES[seq1[row]][seq2[col]]
		M[row][col] = max(UP_SCORE, LEFT_SCORE, DIAG_SCORE)
		
		if M[row][col] == UP_SCORE:
			T[row][col] = "UP"
		elif M[row][col] == LEFT_SCORE:
			T[row][col] = "LEFT"
		else:
			T[row][col] = "DIAG"
			
#TRACEBACK FROM MAX SCORE			
#print(M)
#print(T)
MAXSCORE= -float("inf")
MAXROW = "" 
MAXCOL = ""
for row in range(1,r):
	for col in range(1,c):
		if M[row][col] >= MAXSCORE:
			MAXSCORE = M[row][col]
			MAXROW = row
			MAXCOL = col
			#print(MAXSCORE,MAXROW,MAXCOL)

align1 = ""
align2 = ""

for row in range(MAXROW):
	for col in range(MAXCOL):
		if T[MAXROW][MAXCOL] == "DIAG":
			align1 += seq1[MAXROW]
			align2 += seq2[MAXCOL]
			MAXROW -= 1
			MAXCOL -= 1
		elif T[row][col] == "UP":
			align1 += seq1[MAXROW]
			align2 += "-"
			MAXROW -= 1
		else:
			align1 += "-"
			align2 += seq2[MAXCOL]
			MAXCOL -= 1
		
print(align1[::-1])
print(align2[::-1])

