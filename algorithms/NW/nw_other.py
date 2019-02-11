
#INPUT

seq1_input = "ACCA"
seq2_input = "ACTGG"

BASES = ["A", "C", "T", "G"]

SCORES = {"A":{"A":2, "C":-1, "T":-1, "G":0},
		  "C":{"A":-1, "C":2, "T":0, "G":-1},
		  "T":{"A":-1, "C":0, "T":2, "G":-1},
		  "G":{"A":0, "C":-1, "T":-1, "G":2}
		  }

GAP = -2

#INITIALIZATION
seq1 = "-" + seq1_input 
seq2 = "-" + seq2_input 
print(seq1)
r = len(seq1)
c = len(seq2)

M = [[0 for col in range(c)] for row in range(r)]

T = [["0" for col in range(c)] for row in range(r)]

M[0][0] = 0
for row in range(1,r):
	M[row][0] += -2*row
for col in range(1,c):
	M[0][col] += -2*col
	
#ITERATION

for row in range(1,r):
	for col in range(1,c):
		UP_SCORE = M[row-1][col] + GAP
		LEFT_SCORE = M[row][col-1] + GAP
		DIAG_SCORE = M[row-1][col-1] + SCORES[seq1[row]][seq2[col]]
		scorelist = [UP_SCORE, LEFT_SCORE, DIAG_SCORE]
		M[row][col] = max(scorelist)
		
		if max(scorelist) == UP_SCORE:
			T[row][col] = "UP"
		elif max(scorelist) == LEFT_SCORE:
			T[row][col] = "LEFT"
		else:
			T[row][col] = "DIAG"

print(M)
print(T)			
align1 = ""
align2 = ""

ROW = r-1
COL = c-1

while M[ROW][COL] != 0:
	if T[ROW][COL] == "UP":
		align1 += seq1[ROW]
		align2 += "-"
		ROW -= 1
	elif T[ROW][COL] == "LEFT":
		align1 += "-"
		align2 += seq2[COL]
		COL -= 1
	else:
		align1 += seq1[ROW]
		align2 += seq2[COL]
		ROW -= 1
		COL -= 1		
print(align1[::-1])
print(align2[::-1])
