match_score = +1
mismatch_score = -1		#scores
gap_score = -2

seq1 = "-AGTCT"			#sequences
seq2 = "-AGCT"

##INITIALIZATION

R1 = len(seq1) + 1		#number of rows in the matrices
C2 = len(seq2) + 1		#number of columns in the matrices

M = [[0 for col in range(C2)] for row in range(R1)]		#scoring matrix
T = [["0" for col in range(C2)] for row in range(R1)]		#traceback matrix

T_DIRS = ["UP", "LEFT", "DIAG", "STOP"]

##POPULATION

for col in range(1,C2):
	for row in range(1,R1):
		UPSCORE = M[row-1][col] + gap_score
		LEFTSCORE = M[row][col-1] + gap_score
		if seq1[row-1] == seq2[col-1]:
			DIAGSCORE = M[row-1][col-1] + match_score
		else:
			DIAGSCORE = M[row-1][col-1] + mismatch_score
		SCORES = [UPSCORE, LEFTSCORE, DIAGSCORE, 0]
		M[row][col] = max(SCORES)
		for index in range(len(SCORES)):
			if SCORES[index] == max(SCORES):
				T[row][col] = T_DIRS[index]
print(M)	
#ALIGNMENT
MAX = 0
MAXROW = ""
MAXCOL = ""
for col in range(1,C2):
	for row in range(1,R1):
		if M[row][col] >= MAX :
			MAX = M[row][col]
			MAXROW = row
			MAXCOL = col
'''print(MAX)
print(MAXROW)
print(MAXCOL)
print(M)
print(M[MAXROW][MAXCOL])'''

align1 = ""
align2 = ""


while M[MAXROW][MAXCOL] != 0 :
	if T[MAXROW][MAXCOL] == "DIAG" :
		align1 += seq1[MAXROW-1]
		align2 += seq2[MAXCOL-1]
		MAXROW -= 1
		MAXCOL -= 1
	elif T[MAXROW][MAXCOL] == "UP":
		align1 += "-"
		align2 += seq2[MAXCOL-1]
		MAXCOL -= 1
	else:
		align1 += seq1[MAXROW-1]
		align2 += "-"
		MAXROW -= 1
	
print(align1[::-1])
print(align2[::-1])


