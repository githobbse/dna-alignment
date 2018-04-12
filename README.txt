####################################################################################
# Description: A dynamic program to find the highest-scoring alignment for any arbitrary 
#		DNA sequences X & &.
# File: README.txt
####################################################################################

PURPOSE
The purpose of align.py is to find the highest-scoring alignment for any arbitrary DNA sequences X and Y, using dynamic programming.


DESCRIPTION
The program uses a recursive solution to calculate the score of an optimal-scoring sequence alignment. With the recursive solution, three possibilities are considered: (1) the optimal alignment ends with an aligned pair of letters, extending an optimal alignment of the prefixes of both X and Y, (2) the optimal alignment ends with a letter from X aligned to nothing (a deletion), and (3) the optimal alignment ends with a letter from Y aligned to nothing (an insertion).

After the optimal score is determined, the program then traces back to determine the alignment that produces said score. The score and the alignment are the results of this program.


EXECUTION INSTRUCTIONS
To compile/run the align.py file, one must simply navigate to the directory containing the program, and run the following command:

"python align.py fileName.fa"

Where fileName.fa is the input file containing two DNA sequences, with X on the first line and Y on the second. An example of a valid input file is as follows:

"ACGTAACT
CCTACTGG"

Upon executing the command above with a valid input file, the program will output the score of the optimal-scoring alignment, followed by the alignment of the two sequences.