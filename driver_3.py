from collections import deque 
from copy import deepcopy
import sys 
import timeit


c= set()

#f = open("sudokus_start.txt", "r")
#sudokuL = f.read()
	
grid = sys.argv[1]

let = ['A','B','C','D','E','F','G','H','I']

num= '123456789'

variables = []
sud = {}


for i in range(0,9):
	key = 'A' + str(i+1)
	sud[key] = int(grid[i])
j = 1
for i in range(9,18):
	key = 'B' + str(j)
	j = j+1
	sud[key] = int(grid[i])
j = 1
for i in range(18,27):
	key = 'C' + str(j)
	sud[key] = int(grid[i])
	j = j+1
j = 1
for i in range(27,36):
	key = 'D' + str(j)
	sud[key] = int(grid[i])
	j = j+1

j =1
for i in range(36,45):
	key = 'E' + str(j)
	sud[key] = int(grid[i])
	j = j+1

j = 1
for i in range(45,54):
	key = 'F' + str(j)
	sud[key] = int(grid[i])
	j = j+1

j = 1
for i in range(54,63):
	key = 'G' + str(j)
	sud[key] = int(grid[i])
	j = j+1
	
j = 1	
for i in range(63,72):
	key = 'H' + str(j)
	sud[key] = int(grid[i])
	j = j+1
	
j = 1
for i in range(72,81):
	key = 'I' + str(j)
	sud[key] = int(grid[i])
	j = j+1

class CSP:
	def __init__(self, var, dom, con):
		self.var = var
		self.dom = dom
		self.con = con

for i in let:
	for x in range(1,10):
		string = i + str(x)
		variables.append(string)

d = 1,2,3,4,5,6,7,8,9
# initializing domain
dom = {}
arc = {}
for key in sud:
	dom[key] = []
	arc[key] = []
emptyVar = []
valueVar = []
for key in sud:
	if(sud[key] != 0):
		dom[key].append(sud[key])
		

	if(sud[key] == 0):
		dom[key].append(1)
		dom[key].append(2)
		dom[key].append(3)
		dom[key].append(4)
		dom[key].append(5)
		dom[key].append(6)
		dom[key].append(7)
		dom[key].append(8)
		dom[key].append(9)
	

#for key,value in sud:
#	if(value != 0):
#		print(value)
#		dom[key].append(value)



def arcRC(variables):
	#making every element in a row and column in arc

	for x in variables:
		for y in variables:
			 L1= x[0]
			 L2 =y[0]
			 r1 = x[1]
			 r2 = y[1]
			 #for each row to make an arc besides itself
			 
			 if(L1 == L2 and r1 != r2):
			 	c.add((x,y))

			 #checking for each column
			
			 if(L1 != L2 and r1 == r2):
			 	c.add((x,y))


	# setting up cube restraints
	#block 1
	partvar = []
	for z in range(0,3):
		for d in range(0,3):
			check = str(let[z] + num[d])
			partvar.append(check)
	
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
		
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))

	#block 2
	partvar = []
	for z in range(0,3):
		for d in range(3,6):
			check = str(let[z] + num[d])
			partvar.append(check)

	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))

	#block 3
	partvar = []
	for z in range(0,3):
		for d in range(6,9):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))


	#block 4
	partvar = []
	for z in range(3,6):
		for d in range(0,3):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			 
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))

	#block 5
	partvar = []
	for z in range(3,6):
		for d in range(3,6):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))

	#block 6
	partvar = []
	for z in range(3,6):
		for d in range(6,9):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))


	#block 7
	partvar = []
	for z in range(6,9):
		for d in range(0,3):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			 
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))

		
	#block 8
	partvar = []
	for z in range(6,9):
		for d in range(3,6):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]
			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))



	#block 9
	partvar = []
	for z in range(6,9):
		for d in range(6,9):
			check = str(let[z] + num[d])
			partvar.append(check)
	for i in partvar:
		for j in partvar:
			 V1 = i[0]
			 V2 = j[0]
			 n1 = i[1]
			 n2 = j[1]

			 if(V1 != V2 or n1 != n2):
			 	c.add((i,j))




	return c

totalArcs = arcRC(variables)
for (i,j) in totalArcs:
	for key in arc:
		if(i == key):
			arc[key].append(j)

#print(arc)
dom2 = deepcopy(dom)

def revised(csp, xi, xj):
	i = 0
	revise = False
	d1 = csp.dom[xi]
	d2 = csp.dom[xj]
	for x in d1:
		for y in d2:
			if(len(d2) == 1):
				if(x == y):
					d1.remove(d1[i])
					revise = True
					i -=1
		i +=1
	return revise
	   

cs = CSP(sud,dom, arc)

def AC3(csp):
	q = deque()
	for x in csp.con:
		for y in csp.con[x]:
			q.append((x,y))

	while(len(q) > 0):
		both = q.popleft()
		Xi = both[0]
		Xj = both[1]
		if revised(csp, Xi, Xj):
			for neigh in csp.con[Xi]:
				q.append((neigh,Xi))

		
	for d in csp.dom:
		checklen = len(csp.dom[d])
		if(checklen != 1):
			return False

	return True

def minvalue(csp, assign):
	checkvar = sud
	for key in checkvar:
		if (checkvar[key] == 0):
			sizeDomain = len(domain[key])
			if(sizeDomain < minD):
				minV = key

def complete(assign):
	for d in assign:
		checklen = len(assign[d])
		if(checklen !=1):
			return False
	return True


def forwardCheck(csp, dom, var,v):
	check = True
	arcs = csp.con[var]
	i = 0
	length = len(arcs)
	while(check and length>i):
		elm = arcs[i]
		for d in dom[elm]:
			checklen = len(dom[elm])
			if (v == d):
				if(checklen == 1):
					check = False
					
		i +=1

	return check

def backtrack(assign,csp):
	#start = timeit.default_timer()

	if(complete(assign)):
		sol = []
		for key in assign:
			s = assign[key][0]
			strS = str(s)
			sol.append(strS)
			Ssol = ''.join(sol)
		#stop = timeit.default_timer()
		#time = stop - start
		#print(time)
		return Ssol

	check = len(let) +1
	for key in assign:	
			temp = len(assign[key])		
			if(temp == 0):
				return False
			if (temp <check):
				if(temp>1): 
					check = temp
					var = key

	for v in assign[var]:
		if(forwardCheck(csp, assign, var, v)):
			q = deque()
			secDom = deepcopy(assign)
			addL = []
			addL.append(v)
			secDom[var]= addL

			q = deque()
			for a in csp.con:
				for y in csp.con[a]:
					q.append((a,y))
					
			while (len(q) > 0):
				both = q.popleft()
				Xi = both[0]
				Xj = both[1]
				
				
				cs1 = CSP(sud, secDom, arc)
				if(revised(cs1, Xi,Xj)):
					for nei in csp.con[Xi]:
						q.append((nei,Xi))

			result = backtrack(cs1.dom,csp)
			
			
			if result != False:
				return result
	
	return False



csb = CSP(sud, dom2, arc)
#print(AC3(cs))
answer = backtrack(dom2,csb)
f = open('output.txt', 'w')
f.write(answer)

#print(AC3(cs))

			



	






	

