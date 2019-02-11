##INPUT
seq1_input = "ACCA"
seq2_input = "ACTGG"

match_score = 2
mismatch_score = 1
gap_score = 2

##INITIALIZATION

r = len(seq1_input)+1
c = len(seq2_input)+1
seq1 = "-" + seq1_input
seq2 = "-" + seq2_input

print(seq1_input)
print(seq2_input)
print(seq1)
print(seq2)

M = [[0 for col in range(c)] for row in range(r)]
T = [["0" for col in range(c)] for row in range(r)]


for row in range(r):
	M[row][0] = 2*row
for col in range(c):
	M[0][col] = 2*col


for row in range(1,r):
	for col in range(1,c):
		up_score = M[row-1][col] - gap_score
		left_score = M[row][col-1] - gap_score
		if seq1[row-1] == seq2[col-1]:
			diag_score = M[row-1][col-1] + match_score
		else:
			diag_score = M[row-1][col-1] - mismatch_score
		scores = [up_score, left_score, diag_score]
		M[row][col] = max(scores)
		if max(scores) == up_score:
			T[row][col] = "up"
		elif max(scores) == left_score:
			T[row][col] = "left"
		else:
			T[row][col] = "diag"
print(M)
print(T)
align1 = ""
align2 = ""

ROW = r-1
COL = c-1
print(seq1)
print(seq2)



while M[ROW][COL] != 0:
	if T[ROW][COL] == "diag":
		align1 += seq1[ROW]
		align2 += seq2[COL]
		ROW -= 1
		COL -= 1
	elif T[ROW][COL] == "up":
		align1 += seq1[ROW]
		align2 += "-"
		ROW -= 1
	else:
		align1 += "-"
		align2 += seq2[COL]
		COL -= 1
print(align1[::-1])
print(align2[::-1])
