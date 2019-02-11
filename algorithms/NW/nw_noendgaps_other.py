
#INPUT

seq1 = "ATACCAAAAAAAAAAAAAA"
seq2 = "AAAAAAAAAAAAAACTGA"

BASES = ["A", "C", "T", "G"]

SCORES = {"A":{"A":2, "C":-1, "T":-1, "G":0},
		  "C":{"A":-1, "C":2, "T":0, "G":-1},
		  "T":{"A":-1, "C":0, "T":2, "G":-1},
		  "G":{"A":0, "C":-1, "T":-1, "G":2}
		  }

GAP = -2

#INITIALIZATION

r = len(seq1) + 1
c = len(seq2) + 1 

M = [[0 for col in range(c)] for row in range(r)]
T = [[0 for col in range(c)] for row in range(r)]

#ITERATION

for row in range(1,r):
	for col in range(1,c):
		UP_SCORE = M[row-1][col] + GAP
		LEFT_SCORE = M[row][col-1] + GAP
		DIAG_SCORE = M[row-1][col-1] + SCORES[seq1[row-1]][seq2[col-1]]
		M[row][col] = max(UP_SCORE,LEFT_SCORE,DIAG_SCORE)
		
		if max(UP_SCORE,LEFT_SCORE,DIAG_SCORE) == UP_SCORE:
			T[row][col] = "UP"
		elif max(UP_SCORE,LEFT_SCORE,DIAG_SCORE) == LEFT_SCORE:
			T[row][col] = "LEFT"
		else:
			T[row][col] = "DIAG"
		MAXSCORE = 0
		MAXROW = 0
		MAXCOL = 0
		if M[r-1][col] >= MAXSCORE:
			MAXROW = row
			MAXCOL = col
			MAXSCORE = M[row][col]

align1 = ""
align2 = "" 

finalrow = MAXROW
finalcol = MAXCOL


while MAXROW != 0 and MAXCOL != 0:
	if T[MAXROW][MAXCOL] == "UP":
		align1 += seq1[MAXROW-1]
		align2 += "-"
		MAXROW -= 1
	elif T[MAXROW][MAXCOL] == "LEFT":
		align1 += "-"
		align2 += seq2[MAXCOL-1]
		MAXCOL -= 1
	else:
		align1 += seq1[MAXROW-1]
		align2 += seq2[MAXCOL-1]
		MAXROW -= 1
		MAXCOL -= 1
print(align1[::-1])
print(align2[::-1])

	
