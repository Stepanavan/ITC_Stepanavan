x = raw_input("Enter your name")
if x=="Test":
	print "True"
else:
	print "False"
y = raw_input ("Enter number")

if int(y)>10:
	print "y>10"
	if int(y) == 15:
		print "y=15"
	else:
		print "y!=15"
elif int(y) < -10:
	print "y<-10"
else:
	print"else"

