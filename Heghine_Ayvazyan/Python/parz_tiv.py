m = raw_input("m = ")
n = raw_input("n= ")
m = int(m)
n = int(n)

while n !=0:
	r = m % n
	m, n = n, r

print(m)

