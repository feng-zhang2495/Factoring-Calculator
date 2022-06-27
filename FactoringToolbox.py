#Import math library
from math import *

#Main function
def factorTrinomial(abcValues):
	
	
	#Sets the a, b, c variables to its value 
	a = int(abcValues[0])
	b = int(abcValues[1])
	c = int(abcValues[2])

	
	#Puts equation into the quadratic formula
	result1 = quadraticFormula(a,b,c,"plus")
	result2 = quadraticFormula(a,b,c,"minus")


	#If the expression is impossible through the quadratic formula
	if result1 == "Error" or result2 == "Error":
		print("Can't be factored")
		
	
	#If the expression is possible through the quadratic formula
	else:

		#If the trinomial does not have a c term
		if c == 0 and b >= 1:

			#If a is positive 
			if a > 0:
				CF = GCD(a, b)

				#If the trinomial cannot be common factored 
				if CF == 1:
					
					if b >= 1:
						print(f'x(x+{b})')

					else:
						print(f'x(x{b})')
				
				#If the trinomial can be common factored 
				else:

					#If the coefficient of a isn't 1 after dividing by the common factor 
					if a//CF > 1:

						if b//CF > 0:
							print(f'{CF}x({a//CF}x+{b//CF})')
						else:
							print(f'{CF}x({a//CF}x{b//CF})')

					#If the coefficient of a is 1
					else:

						if b//CF > 0:
							print(f'{CF}x(x+{b//CF})')
						
						else:
							print(f'{CF}x(x{b//CF})')

			#If a is negative 
			else:
				CF = GCD(-a, b)

				#If the trinomial can not be common factored 
				if CF == 1:

					if b >= 1:
						print(f'-x(x+{b})')

					else:
						print(f'-x(x{b})')
				
					
					#If b term is positive 
					if b//CF > 0:
							print(f'-{CF}x({-a//CF}x+{-b//CF})')

					#If b term is negative 
					else:
							print(f'-{CF}x({-a//CF}x{-b//CF})')

				
				#If the trinomial can be common factored 
				else:

					#If b term is positive
					if -b//CF > 0:
						print(f'-{CF}x({-a//CF}x+{b//CF})')
					
					#If b term is negative 
					else:
						print(f'-{CF}x({-a//CF}x-{b//CF})')


		#FACTORING A COMPLEX TRINOMIAL (a coefficient isnt 1)
		if abs(a) > 1 and abs(b) >= 1 and abs(c) >= 1:
			

			#Finding greatest common factor of the all coefficients 
			gcdAB = GCD(abs(a),abs(b))

			gcdABC = GCD(gcdAB, abs(c))
			
			#If the common factor is 1
			if gcdABC == 1:
				commonFactor = 1
			

			#If the common factor isnt 1 divide a,b,c by the common factor 
			else:
				commonFactor = gcdABC
				a //= gcdABC
				b //= gcdABC
				c //= gcdABC 

				#This is a variable used later to check if the complex trinomial can be further factored
				done = False

				
			#Arrays of all the possible factors of the coefficient of a and c
			a1 = []
			a2 = []
			c1 = []
			c2 = []

			
			#Finds all the possible factors of a 
			for x in range(1, a+1):
				if float(a/x).is_integer() == True:
					a1.append(x)
					a2.append(int(a/x))
			

			#Finds all the possible factors of c
			if c < 0:
				for y in range(c, 1):
					if y == 0:
						pass 

					elif float(c/y).is_integer() == True:
						c1.append(y)
						c2.append(int(c/y))

			
			#Finds all the possible factors of c
			else:
				for y in range(1, c+1):
					if float(c/y).is_integer() == True:
						c1.append(y)
						c2.append(int(c/y))
						c1.append(-y)
						c2.append(int(-c/y))


			#Nested for loop to find which multiples of a and c add up to b
			for i in range(len(a1)):

				for j in range(len(c1)):
					one = a1[i] * c1[j]
					two = a2[i] * c2[j]

					#If the factors add up to the coefficient of b
					if int(one) + int(two) == b:
						roots = properEnding(c2[j], c1[j])
						
						#Creates the correct coefficients for the output
						if a1[i] == 1:
							first = ""
						else:
							first = a1[i]
						if a2[i] == 1:
							second = ""
						else:
							second = a2[i]
						
						#Done switch set to true 
						done = True

						#Outputs
						if commonFactor != 1:
							print(f'{commonFactor}({first}x{roots[0]})({second}x{roots[1]})')
						
						else:
							print(f'({first}x{roots[0]})({second}x{roots[1]})')
							
						break
						
				if int(one) + int(two) == b:
					break

			
			#If the result can't be factored (basically if the for loops didnt find any values that add up to b)
			if done == False:

				#If a is negative then multiply all the other coefficients by -1
				if a < 1:
					commonFactor = -commonFactor 
				
					a = -a
					b = -b
					c = -c


				#ALL CORRECT ENDINGS FOR THE OUTPUT STRING 
				if a == 1 or a == -1:
					aEnd = ''
					
				else:
					aEnd = a
				
				if a < 0:
					aEnd = str(aEnd)
					


				if b == 1 and b == -1:
					bEnd = ''
					
				else:
					bEnd = b
				
				bEnd = str(bEnd)
				if b > 0:
					bEnd = '+' + bEnd

				

				if c == 1 and c==-1:
					cEnd = ''
					
				else:
					cEnd = c
				
				cEnd = str(cEnd)
				if c > 0:
					cEnd = '+' + cEnd
				

				#OUTPUT
				print(f'{commonFactor}({aEnd}x^2{bEnd}x{cEnd})')


		#FACTOR COMMON TRINOMIAL  
		elif a == 1 and abs(b) > 1 and abs(c) > 1:
			resultPos = quadraticFormula(a,b,c, "plus")
			resultNeg = quadraticFormula(a,b,c, "minus")

			#If the quadratic formula returns two integers 
			if resultPos != "Error" and resultNeg != "Error" and resultPos != False and resultNeg != False:

				#Finds the proper endings using the roots -resultNeg and -resultPos (negative because its flipped in the factored form)
				res = properEnding(-resultNeg, -resultPos)

				#OUTPUT
				print(f'(x{res[0]})(x{res[1]})')
			
			else:
				print("Can't be factored")
			
		#Difference of Squares
		if b == 0:
			print(diffOfSquares(a,-c))


#Gets the GCD of two numbers
def GCD(x, y):
	#Finds the max and min number
	max = x
	min = y
	if y > x:
		max = y
		min = x
	
	#Calculates the reminder 
	remainder = max % min
	if remainder == 0:
		return min 

	#Euclidean algorithm
	while remainder != 0:
		remainder = max % min
		max = min
		min = remainder

	return max


#Common Factor of 3 numbers 
def getCommonFactor(a,b,c):

	#If c coefficient is 0
	if c == 0:
		abc = str(GCD(a,b)) + 'x'
	
	#GCD (a, b, c) = gcd(gcd(a,b), c)
	else:
		a,b,c = abs(a),abs(b),abs(c)
		ab = GCD(a,b)
		abc = GCD(ab,c)


	#If the gcd is 1 
	if abc == 1:
		return ""
	
	#Output
	else:
		return abc


#Gets the proper plus or minus signs for the factors 
def properEnding(p, q):
	endProduct = []
	p = int(p)
	q	= int(q)

	#Proper formatting 
	if p > 0:
		endProduct.append(f'+{p}')
	
	else:
		endProduct.append(f'{p}')
	
	if q > 0:
		endProduct.append(f'+{q}')
	
	else:
		endProduct.append(f'{q}')

	#Returns a list of the proper endings
	return endProduct


#Factors a difference of squares
def diffOfSquares(a,c):
	aNeg = False

	#If the a value is negative 
	if a < 0:
		c = -c
		a = -a
		aNeg = True

	#If a is 1 
	if a == 1:
		try:
			root = sqrt(c)
			aRoot = sqrt(a)


		#If it returns an error
		except Exception:
			return "Can't be factored"


		#If a and c is a perfect square 
		if int(root) ** 2 == c and int(aRoot) ** 2 == int(a):
			return f'(x-{int(root)})(x+{int(root)})'
		

		#If a or c are not perfect squares 
		else:
			return "Can't be factored"
	
	
	if a > 1:
		CommonFact = GCD(a, c)
		root = sqrt(c/CommonFact)

		#If there is a common factor
		if CommonFact != 1:
			a //= CommonFact 
			c //= CommonFact

		aRoot = sqrt(a)

		if aNeg == True:
			CommonFact = -CommonFact
		
		#If a and c is a perfect square
		if (int(root) ** 2) == c and int(aRoot)**2 == int(a):
			aRoot = int(aRoot)

			if CommonFact != 1:
				if aRoot == 1:
					aRoot = ""

					#Output 
				return (f'{CommonFact}({aRoot}x-{int(root)})({aRoot}x+{int(root)})')
			
			else:
				#Output 
				return (f'({aRoot}x-{int(root)})({aRoot}x+{int(root)})')

		#If a or c is not a perfect square 
		else:
			return "Cannot be factored"
	

#Quadratic Formula
def quadraticFormula(a, b, c, condition):

	#If the expression can't be factored
	if b**2-(4*a*c) < 0:
		return "Error"

	#If it can be factored 
	else:
		first = (-b+(sqrt(b**2-(4*a*c))))/2*a
		second  = (-b-(sqrt(b**2-(4*a*c))))/2*a

		#Return the values of x only if they are not decimals 
		if condition == "plus":
			if float(first).is_integer() == False:
				return False

			else:
				return first

		elif condition  == "minus":
			if float(second).is_integer() == False:
				return False
				
			else:
				return second


#Gets the information from input string
def getABCvalues(expressions):

	#Prints out equation
	print(f'\n{expressions}:')

	#Delete unessecary spaces in the input
	expression = expressions.replace(" ", "")
	
	#GETTING NUM OF X's
	Xcount = 0
	for i in range(len(expression)):
		if expression[i] == "x":
			Xcount += 1
	
	#SETTING VARIABLES
	stringList = expression.split('x')
	try:
		if stringList[2] == '':
			stringList.pop(2)
	except Exception:
		pass
	numTerms = len(stringList)
	b = ""
	a = ""
	c = ""

	
	if numTerms == 3:
		#FIND A COEFFICIENT
		if stringList[0] == '':
			a = 1
		elif stringList[0] == "-":
			a = -1
		else:
			a = int(stringList[0])

		#FIND B COEFFICIENT
		try:
			if stringList[1][2] == "-":
				b = int(stringList[1][3:])*(-1)
			else:
				b = int(stringList[1][3:])
		except Exception:
			if stringList[1][2] == "-":
				b = -1
			else:
				b = 1
		#FIND C COEFFICIENT
		if stringList[2][0] == "-":
			c = int(stringList[2][1:])*(-1)
		else:
			c = int(stringList[2][1:])

	if numTerms == 2:
		if Xcount  == 2:
			#FIND A COEFFICIENT
			if stringList[0] == '':
				a = 1
			elif stringList[0] == "-":
				a = -1
			else:
				a = stringList[0]

			#FIND B COEFFICIENT
			try:
				if stringList[1][2] == "-":
					b = int(stringList[1][3:])*(-1)
				else:
					b = int(stringList[1][3:])
			except Exception:
				if stringList[1][2] == "-":
					b = -1
				else:
					b = 1
			c = 0

		elif Xcount == 1:
			#FIND A COEFFICIENT
			if stringList[0] == '':
				a = 1
			elif stringList[0] == "-":
				a = -1
			else:
				a = stringList[0]

			#FIND C COEFFICIENT
			if stringList[1][2] == "-":
				c = int(stringList[1][3:])*(-1)
			else:
				c = int(stringList[1][3:])
			b = 0
	
	if numTerms == 1:
		#FIND A COEFFICIENT
		if stringList[0] == '':
			a = 1
		elif stringList[0] == "-":
			a = -1
		else:
			a = stringList[0]
	
	#Get results
	results = []

	results.append(a) 
	results.append(b) 
	results.append(c) 

	return results