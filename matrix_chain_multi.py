n=int(input("No. of matrices : "))
p=[]
for i in range(n+1):
	p.append(int(input("Enter dimension p "+str(i)+" : " )))
 
m=[[0 for i in range(n+1)] for j in range(n+1)] 
s=[[0 for i in range(n)] for j in range(n)]


#MATRIX-CHAIN-ORDER
#difference between i and j is 0
for i in range(1,n+1):
	m[i][i]=0

#difference between i and j is > 0
for l in range(2,n+1):
	for i in range(1,n-l+2):
		j=i+l-1
		m[i][j]=99999999999999999999999999999
		for k in range(i,j):
			q=(m[i][k]+m[k+1][j])+(p[i-1]*p[k]*p[j])
			if(q<m[i][j]):
				m[i][j]=q
				s[i][j-1]=k

print(*m,sep="\n")
print("Min # of multiplication required = ",m[1,n])
print()
print(*s,sep="\n")
print("Parenthesis Locations : ")
print()

"""
Matrix multiplication is associative, and so all parenthesizations yield the same product.

If the chain of matrices is <A1;A2;A3;A4>, then we can fully parenthesize the product A1A2A3A4 in ﬁve distinct ways:

(A1(A2(A3A4)))
(A1(A2A3)A4)) 
((A1A2)(A3A4)) 
((A1(A2A3))A4) 
(((A1A2)A3)A4)

We state the matrix-chain multiplication problem as follows: given a chain <A1;A2;:::;An> of n matrices, where for i=1;2;:::;n, matrix Ai has dimension (pi-1 x pi), fully parenthesize the product A1A2...An in a way that minimizes the number of scalar multiplications. 

Counting the numberof parenthesizations


	Algorithm
Formula : 
c[i][j]=min(c[i][k]+c[k+1][j]+(p[i-1]*p[k]*p[j]))	For all i<=k<j

We will start filling table in such a way that the difference between i and j, 
initially will be 0 and then start increasing gradually.


     m

  0 1 2 . .
0
1
2
.
.

     s

  1 2 . .
0
1
2
.
.

Cost for filling the table= O(n^2)

And
A simple inspection of the nested loop structure of MATRIX-CHAIN-ORDER
yields a running time of O(n^3) for the algorithm. 

The loops are nested three deep, andeach loopindex (l, i,andk)takes on atmost n-1 values.
The running time of this algorithm is in fact also Omega(n^3). 

The algorithm requires Theta(n^2) space to store the m and s tables.

Thus, MATRIX-CHAINORDER is much more efﬁcient than the exponential-time 
method of enumerating all possible parenthesizations and checking each one.

"""