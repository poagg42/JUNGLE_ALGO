

LCS = []
string_A = "ABCDEF"
string_B = "GBCDFE"

for i in range(len(string_A) + 1):
    for j in range(len(string_B) + 1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

