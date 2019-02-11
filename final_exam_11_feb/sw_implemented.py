#INPUT

seqA = "ATTAA"
seqB = "ACTCT"

SCORES = {"A":{"A":2, "C":-1, "T":-1, "G":0},
		  "C":{"A":-1, "C":2, "T":0, "G":-1},
		  "T":{"A":-1, "C":0, "T":2, "G":-1}, 
		  "G":{"A":0, "C":-1, "T":-1, "G":2}
		  }
GAP_SCORE = -2

#INITIALIZATION
def smith_water(seqA, seqB, SCORES, GAP_SCORE):
	r = len(seqA) + 1
	c = len(seqB) + 1

	M = [[0 for col in range(c)] for row in range(r)]
	T = [[0 for col in range(c)] for row in range(r)]

	#ITERATION
	MAX_SCORE = -float("inf")
	MAX_ROW = 0
	MAX_COL = 0
	for row in range(1,r):
		for col in range(1,c):
			print(row,col)
			UP_SCORE = M[row-1][col] + GAP_SCORE
			LEFT_SCORE = M[row][col-1] + GAP_SCORE
			DIAG_SCORE = M[row-1][col-1] + SCORES[seqA[row-1]][seqB[col-1]]
			SCORE_LIST = [UP_SCORE, LEFT_SCORE, DIAG_SCORE, 0]
			M[row][col] = max(SCORE_LIST)
			
			if M[row][col] == 0:
				T[row][col] = "STOP"
			elif M[row][col] == UP_SCORE:
				T[row][col] = "UP"
			elif M[row][col] == LEFT_SCORE:
				T[row][col] = "LEFT"
			else:
				T[row][col] = "DIAG"
			if M[row][col] >= MAX_SCORE:
				MAX_ROW = row
				MAX_COL = col
				MAX_SCORE = M[row][col]
	return(M, T, MAX_SCORE, MAX_ROW, MAX_COL)

print(smith_water(seqA, seqB, SCORES, GAP_SCORE))
