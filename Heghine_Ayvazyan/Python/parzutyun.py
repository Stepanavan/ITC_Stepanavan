n = raw_input("n = ")
n = int(n)

b = True
for k in range (2, n):
	if n % k == 0:
		 b = False
		 
if b:
	 print("Yes")
else:
	 print("No")
