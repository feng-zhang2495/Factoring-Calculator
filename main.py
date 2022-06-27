##########################################
# By: Feng Zhang &  Alim Chen
#
# Project: Factoring Toolbox - Python
# Description: Quadratic function gets
# 						 outputted in factored form
# NOTE: Please read the note below before
#				using code. Thank you!
##########################################


#PLEASE NOTE, when using the code, type your input with a ^2 if subscript 2 AND actualy type negatives, because on the copied testcases, the negative was not in the right format, thus messed up the code.  

#   – -    <-- You can see the slight length difference for negatives

#Imported our Library
from FactoringToolbox import *

eqn = [
"x^2 + 18x + 32",
"x^2 + 17x + 32",
"x^2 - 16x + 63",
"x^2 + 5x - 24",
"x^2 - 5x - 24",
"x^2 - 9",
"x^2 - 10",
"x^2 + 9",
"2x^2 + 11x + 5",
"12x^2 - 7x - 10",
"87x^2 - 29x + 143",
"9x^2 - 100",
"9x^2 + 1",
"3x^2 + 12x + 6",
"2x^2 + 10x + 8",
"5x^2 - 500",
"x^2 + 7x",
"-10x^2 + 5x",
"10x^2 - 17x + 3",
"12x^2 - 5x - 3",
]

for x in range(len(eqn)):
	abcVal = getABCvalues(eqn[x])
	factorTrinomial(abcVal)


	
print('\nEND OF PROGRAM\n\n\n\n')
