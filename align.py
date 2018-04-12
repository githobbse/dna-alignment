#######################################################################################################################################################################
# Description: A dynamic program to find the highest-scoring alignment for any arbitrary DNA sequences X & &.
# File: align.py
#######################################################################################################################################################################

import sys

def score(iLetter, jLetter):
    # Score matrix.
    s = [[2, -5, -5, -1, -5],
         [-5, 2, -1, -5, -5],
         [-5, -1, 2, -5, -5],
         [-1, -5, -5, 2, -5],
         [-5, -5, -5, -5, -5]]

    # Letter position.
    l = ['A', 'C', 'G', 'T', '-']

    # Calculates score for given iLetter and jLetter.
    score = s[l.index(jLetter)][l.index(iLetter)]
    
    return score

def opt(X, Y):
    m, n = len(X) + 1, len(Y) + 1
    g = -5
    M, N = [], []

    # Instantiates the matrix M given the size of X and Y.
    M = [[0 for x in range(0, m)] for x in range(0, n)]
    
    # Fills first row and column of the matrix M.
    for i in range(1, m):
        M[0][i] = g * i     # Note that in Python it's [row, column].
    for j in range(1, n):
        M[j][0] = g * j

    # Calculate the score of an optimal-scoring sequence alignment via recurrence.
    for i in range(1, m):
        for j in range(1,n):
            M[j][i] = max(M[j-1][i-1] + score(X[i-1], Y[j-1]),
                          M[j][i-1] + g,
                          M[j-1][i] + g)

    return M

def traceback(X, Y, M):
    xAlign, yAlign = '', ''
    g = -5
    i, j = len(X), len(Y)
    
    # Traces back to start of matrix M to find alignment.
    while (i > 0 or j > 0):
        current = M[j][i]

        # Letter from X aligns to nothing (deletion).
        if (i > 0 and current == M[j][i-1] + g):
              xAlign += X[i-1]
              yAlign += '-'
              i -= 1

        # Letter from Y aligns to nothing (insertion).
        elif (j > 0 and current == M[j-1][i] + g):
              xAlign += '-'
              yAlign += Y[j-1]
              j -= 1

        # Aligned pair of letters (match). 
        else:
            xAlign += X[i-1]
            yAlign += Y[j-1]
            i -= 1
            j -= 1

    # Reverse the sequences.
    xAlign = xAlign[::-1]
    yAlign = yAlign[::-1]
            
    return xAlign, yAlign

def main():
    X, Y = '', ''
    i = 0
    
    # Inputs file from command line and sets X as the first sequence and Y as the second.
    file = open(sys.argv[1], 'r')
    for sequence in file:
        if i == 0:
            X = sequence.strip()
        elif i == 1:
            Y = sequence.strip()
        else:
            sys.stdout.write('Please input a file with two valid sequences.')
            main()
        i += 1

    # Build matrix of alignment scores.
    M = opt(X, Y)
    optScore = M[len(Y)][len(X)]

    # Traceback to find the alignment that gives the optScore.
    xAlign, yAlign = traceback(X, Y, M)
    
    # Output results to stdout.
    sys.stdout.write('Score: ' + str(optScore) + '\n')
    sys.stdout.write(str(xAlign) + '\n')
    sys.stdout.write(str(yAlign) + '\n')

main()

